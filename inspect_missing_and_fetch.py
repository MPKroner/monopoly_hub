# -*- coding: utf-8 -*-
import json
import os
import urllib.request
import urllib.parse
import re

with open("editions_seed.json", "r", encoding="utf-8") as f:
    editions = json.load(f)

missing = []
for ed in editions:
    img = ed.get("image_url", "")
    if not img or not os.path.exists(img):
        missing.append(ed)

print(f"Editions with real box cover already: {len(editions) - len(missing)} / {len(editions)}")
print(f"Still missing: {len(missing)}")

# Search targeted on Fandom by testing combinations
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://monopoly.fandom.com/"
}

def query_fandom_image(title):
    url = f"https://monopoly.fandom.com/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&pithumbsize=600&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for pid, p in pages.items():
                thumb = p.get("thumbnail", {}).get("source")
                if thumb:
                    return thumb
    except:
        pass
    return None

def search_fandom_smart(q):
    url = f"https://monopoly.fandom.com/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srlimit=6&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            items = data.get("query", {}).get("search", [])
            for it in items:
                t = it["title"]
                if not t.startswith("Category:") and "List of" not in t and "Tokens" not in t and "Rules" not in t:
                    thumb = query_fandom_image(t)
                    if thumb:
                        return t, thumb
    except:
        pass
    return None, None

# Try smart searches
found_more = 0
for ed in missing:
    eid = ed["id"]
    name = ed["name"]

    # Candidate query terms
    candidates = []
    # Clean french/english terms
    c1 = re.sub(r'Monopoly\s*(:|-)?\s*', '', name)
    c1 = re.sub(r'[\(\)]', ' ', c1).strip()
    candidates.append(f"Monopoly {c1}")
    candidates.append(c1)
    
    # Specific keywords
    words = c1.split()
    if len(words) > 1:
        candidates.append(f"{words[0]} {words[1]}")
    candidates.append(words[0])

    thumb_url = None
    matched_title = None
    for cand in candidates:
        matched_title, thumb_url = search_fandom_smart(cand)
        if thumb_url:
            break

    if thumb_url:
        ext = "webp" if ".webp" in thumb_url or "scale-to" in thumb_url else "jpg"
        filepath = os.path.join("images", f"{eid}.{ext}")
        try:
            req = urllib.request.Request(thumb_url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                content = resp.read()
                if len(content) > 1500:
                    with open(filepath, "wb") as f:
                        f.write(content)
                    ed["image_url"] = f"images/{eid}.{ext}"
                    found_more += 1
                    print(f"[{found_more}] SUCCESS: {name} (matched '{matched_title}') -> {filepath}")
        except Exception as e:
            print(f"Failed download {name}: {e}")

print(f"\nFound {found_more} additional box covers!")
with open("editions_seed.json", "w", encoding="utf-8") as f:
    json.dump(editions, f, ensure_ascii=False, indent=2)
