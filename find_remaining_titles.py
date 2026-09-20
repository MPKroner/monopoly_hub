# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import re

with open("editions_seed.json", "r", encoding="utf-8") as f:
    editions = json.load(f)

unmatched = [e for e in editions if not e.get("image_url")]
print(f"Total unmatched editions: {len(unmatched)}")

def search_fandom(q):
    params = urllib.parse.urlencode({'action': 'opensearch', 'search': q, 'limit': 6, 'format': 'json'})
    url = f"https://monopoly.fandom.com/api.php?{params}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [t for t in data[1] if not t.startswith('List of') and 'Tokens' not in t]
    except Exception as e:
        return []

for e in unmatched[:25]:
    # Extract keywords
    name = re.sub(r'Monopoly\s*(:|-)?\s*', '', e['name'])
    name_clean = re.sub(r'[\(\)]', '', name).strip()
    res = search_fandom(name_clean)
    if not res:
        # try English or first words
        words = name_clean.split()[:2]
        res = search_fandom(" ".join(words))
    print(f"{e['id']} | {e['name']}  ===>  {res}")
