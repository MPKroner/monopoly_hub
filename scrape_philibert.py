# -*- coding: utf-8 -*-
import urllib.request
import re

url = 'https://www.philibertnet.com/fr/1313-monopoly'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        imgs = re.findall(r'https://cdn[0-9]*\.philibertnet\.com/[^"\'\s>]+\.(?:jpg|jpeg|png|webp)', html)
        print(f"Found {len(imgs)} image links:")
        for img in sorted(set(imgs)):
            if 'large_default' in img or 'home_default' in img:
                print("-->", img)
except Exception as e:
    print(e)
