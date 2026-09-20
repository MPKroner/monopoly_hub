# -*- coding: utf-8 -*-
"""
Harvest all Monopoly editions and real box covers from Monopoly Fandom and Wikipedia.
"""
import urllib.request
import urllib.parse
import json
import re
import os
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://monopoly.fandom.com/'
}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_all_fandom_pages():
    pages = []
    apcontinue = ""
    print("Fetching all article titles from Monopoly Fandom...")
    while True:
        url = "https://monopoly.fandom.com/api.php?action=query&list=allpages&aplimit=500&format=json"
        if apcontinue:
            url += f"&apcontinue={urllib.parse.quote(apcontinue)}"
        data = fetch_json(url)
        if not data:
            break
        batch = data.get('query', {}).get('allpages', [])
        pages.extend(batch)
        print(f"  Fetched {len(batch)} titles (Total so far: {len(pages)})")
        if 'continue' in data and 'apcontinue' in data['continue']:
            apcontinue = data['continue']['apcontinue']
        else:
            break
        time.sleep(0.2)
    return pages

def get_page_details_batch(page_titles):
    results = {}
    # Batch query up to 40 pages at once
    for i in range(0, len(page_titles), 40):
        chunk = page_titles[i:i+40]
        titles_str = "|".join([urllib.parse.quote(t) for t in chunk])
        url = f"https://monopoly.fandom.com/api.php?action=query&titles={titles_str}&prop=pageimages|categories|extracts&pithumbsize=600&exintro=1&explaintext=1&cllimit=50&format=json"
        data = fetch_json(url)
        if data and 'query' in data and 'pages' in data['query']:
            for pid, pdata in data['query']['pages'].items():
                if int(pid) > 0:
                    results[pdata.get('title')] = pdata
        print(f"  Processed {min(i+40, len(page_titles))}/{len(page_titles)} page details...")
        time.sleep(0.2)
    return results

if __name__ == "__main__":
    raw_pages = get_all_fandom_pages()
    print(f"Total raw pages from Fandom: {len(raw_pages)}")
    
    # Filter out non-editions (e.g. general articles like 'Houses', 'Hotels', 'Chance', 'Community Chest', 'Rules', 'List of...')
    ignore_patterns = [
        r"^Category:", r"^File:", r"^Template:", r"^Monopoly Wiki",
        r"^List of", r"^Tokens", r"^Houses", r"^Hotels", r"^Chance", r"^Community Chest",
        r"^Rules", r"^Properties", r"^Money", r"^Dice", r"^Speed Die", r"^Jail",
        r"^Free Parking", r"^Go \("
    ]
    
    candidate_titles = []
    for p in raw_pages:
        title = p['title']
        if any(re.search(pat, title, re.IGNORECASE) for pat in ignore_patterns):
            continue
        candidate_titles.append(title)
        
    print(f"Candidate edition titles: {len(candidate_titles)}")
    with open("scratch/fandom_candidate_titles.json", "w", encoding="utf-8") as f:
        json.dump(candidate_titles, f, ensure_ascii=False, indent=2)
