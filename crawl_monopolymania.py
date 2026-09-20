# -*- coding: utf-8 -*-
import urllib.request
import re
import json

boxes = {}

for page in range(1, 15):
    url = f"https://monopolymania.com/?page={page}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            # Extract links and images
            matches = re.findall(r'<a href="https://monopolymania\.com/([^"]+)"><img src="(/public/[^"]+)" alt="" />([^<]+)</a>', html)
            if not matches:
                break
            print(f"Page {page}: found {len(matches)} boxes")
            for slug, img, title in matches:
                clean_title = title.replace("&amp;", "&").strip()
                full_img = f"https://monopolymania.com{img}"
                boxes[slug] = {"title": clean_title, "image": full_img}
                print(f"  {clean_title} --> {full_img}")
    except Exception as e:
        print(f"Page {page} error: {e}")
        break

with open("monopolymania_boxes.json", "w", encoding="utf-8") as f:
    json.dump(boxes, f, ensure_ascii=False, indent=2)

print(f"Total box covers found on monopolymania: {len(boxes)}")
