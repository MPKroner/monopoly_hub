# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import time
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://monopoly.fandom.com/'
}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Error fetching {url[:100]}...: {e}")
        return None

with open("scratch/fandom_candidate_titles.json", "r", encoding="utf-8") as f:
    titles = json.load(f)

print(f"Processing details for {len(titles)} titles...")

details_map = {}
batch_size = 40
for i in range(0, len(titles), batch_size):
    chunk = titles[i:i+batch_size]
    # format for titles parameter
    titles_str = "|".join([t for t in chunk])
    params = urllib.parse.urlencode({
        'action': 'query',
        'titles': titles_str,
        'prop': 'pageimages|categories|extracts',
        'pithumbsize': '600',
        'exintro': '1',
        'explaintext': '1',
        'cllimit': '50',
        'format': 'json'
    })
    url = f"https://monopoly.fandom.com/api.php?{params}"
    data = fetch_json(url)
    if data and 'query' in data and 'pages' in data['query']:
        for pid, p in data['query']['pages'].items():
            if int(pid) > 0:
                details_map[p.get('title')] = {
                    'pageid': p.get('pageid'),
                    'title': p.get('title'),
                    'thumbnail': p.get('thumbnail', {}).get('source', ''),
                    'extract': p.get('extract', ''),
                    'categories': [c.get('title', '').replace('Category:', '') for c in p.get('categories', [])]
                }
    print(f"Progress: {min(i+batch_size, len(titles))}/{len(titles)} (Collected {len(details_map)} entries)")
    time.sleep(0.15)

with open("scratch/fandom_details_raw.json", "w", encoding="utf-8") as f:
    json.dump(details_map, f, ensure_ascii=False, indent=2)

print(f"Saved {len(details_map)} page details to scratch/fandom_details_raw.json")
