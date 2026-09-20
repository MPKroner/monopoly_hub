# -*- coding: utf-8 -*-
import urllib.request
import re

url = 'https://www.winningmoves.fr/categorie-produit/villes-et-regions/monopoly-villes/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
        matches = re.findall(r'href="(https://www.winningmoves.fr/nos-jeux/monopoly-[^"]+)"', html)
        unique_urls = list(set(matches))
        print(f"Found {len(unique_urls)} French city Monopoly pages:")
        for u in sorted(unique_urls):
            print(u)
except Exception as e:
    print(e)
