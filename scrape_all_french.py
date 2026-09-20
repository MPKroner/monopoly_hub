# -*- coding: utf-8 -*-
import urllib.request
import re
import json

found_pages = {}

categories = [
    'villes-et-regions/monopoly-villes',
    'films-et-series/monopoly-films-series',
    'mangas-et-comics/monopoly-mangas',
    'jeux-video/monopoly-jeux-video',
    'sport/monopoly-sport',
    'musique/monopoly-musique'
]

for cat in categories:
    for page in range(1, 10):
        if page == 1:
            url = f'https://www.winningmoves.fr/categorie-produit/{cat}/'
        else:
            url = f'https://www.winningmoves.fr/categorie-produit/{cat}/page/{page}/'
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8')
                matches = list(set(re.findall(r'href="(https://www.winningmoves.fr/nos-jeux/monopoly-[^"]+)"', html)))
                for m in matches:
                    found_pages[m] = True
        except Exception as e:
            # End of pagination
            break

print(f"Total unique French Monopoly product pages on Winning Moves: {len(found_pages)}")

# Extract image from each product page
product_images = {}
for prod_url in found_pages.keys():
    req = urllib.request.Request(prod_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            # Extract og:image
            og_match = re.search(r'<meta property="og:image" content="(https://www.winningmoves.fr/wp-content/uploads/[^"]+)"', html)
            title_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
            if og_match:
                title = title_match.group(1).replace(' - Winning Moves', '').strip() if title_match else prod_url
                img_url = og_match.group(1)
                product_images[prod_url] = {"title": title, "image": img_url}
                print(f"French Box: {title} --> {img_url}")
    except Exception as e:
        print(f"Error fetching {prod_url}: {e}")

with open("winning_moves_images.json", "w", encoding="utf-8") as f:
    json.dump(product_images, f, ensure_ascii=False, indent=2)

print(f"Saved {len(product_images)} French Monopoly box images to winning_moves_images.json")
