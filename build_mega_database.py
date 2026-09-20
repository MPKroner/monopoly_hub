# -*- coding: utf-8 -*-
"""
Mega Database Builder & Downloader for Monopoly Tracker.
Processes 1000+ real editions and downloads authentic box covers.
"""
import urllib.request
import urllib.parse
import json
import re
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = r"C:\Users\Admin\.gemini\antigravity\scratch\monopoly-collection-tracker"
IMAGES_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://monopoly.fandom.com/'
}

def sanitize_filename(name):
    # Keep alphanumeric, hyphen, underscore
    clean = re.sub(r'[^\w\-_\.]', '_', name)
    return clean[:80]

def detect_category(title, cats, extract):
    title_l = title.lower()
    cats_str = " ".join(cats).lower()
    ext_l = (extract or "").lower()
    combined = f"{title_l} {cats_str} {ext_l}"
    
    # 1. Junior & Enfants
    if "junior" in combined or "my first" in combined or "kids" in title_l:
        return "Junior & Enfants"
        
    # 2. Variantes & Règles Spéciales
    variants = [
        "builder", "knockout", "glisse", "cheaters", "sore losers", "mauvais perdants",
        "crooked cash", "faux billets", "deal", "speed", "bid", "chance", "longest game",
        "empire", "millionaire", "electronic banking", "ultimate banking", "voice banking",
        "revolution", "live", "city", "grab & go", "travel", "flip", "scrabble",
        "super electronic", "social distancing", "for millennials", "pizza", "target",
        "arcade pac-man", "express", "party", "town square", "free parking", "mega edition"
    ]
    if any(v in title_l for v in variants) or "board game variants" in cats_str or "derivative games" in cats_str:
        return "Variantes & Règles Spéciales"
        
    # 3. Jeux Vidéo
    vg = [
        "nintendo", "pokemon", "pokémon", "zelda", "mario", "gamer", "sonic", "fallout", "skyrim",
        "halo", "assassin", "cyberpunk", "overwatch", "minecraft", "fortnite", "world of warcraft",
        "warcraft", "animal crossing", "street fighter", "pac-man", "mega man", "uncharted",
        "playstation", "xbox", "sega", "resident evil", "apex legends", "league of legends",
        "roblox", "witcher", "crash bandicoot", "dungeons & dragons", "d&d", "magic the gathering",
        "pacman", "goldeneye", "donkey kong", "portal", "half-life", "elder scrolls", "skyward"
    ]
    if any(k in combined for k in vg) or "video game" in cats_str:
        return "Jeux Vidéo"
        
    # 4. Anime & Manga
    anime = [
        "dragon ball", "dbz", "naruto", "one piece", "my hero academia", "attack on titan",
        "death note", "sailor moon", "astérix", "asterix", "tintin", "lucky luke", "demon slayer",
        "jujutsu kaisen", "tokyo ghoul", "bleach", "hunter x hunter", "cowboy bebop", "yu-gi-oh",
        "avatar the last airbender", "studio ghibli", "pokémon"
    ]
    if any(k in combined for k in anime) or "anime" in cats_str or "manga" in cats_str:
        return "Anime & Manga"
        
    # 5. Musique & Groupes
    music = [
        "beatles", "queen", "ac/dc", "acdc", "metallica", "iron maiden", "kiss", "rolling stones",
        "elvis", "david bowie", "grateful dead", "pink floyd", "bob marley", "led zeppelin",
        "eminem", "bon jovi", "rush", "def leppard", "fleetwood mac", "woodstock", "music", "band"
    ]
    if any(k in combined for k in music) or "music" in cats_str:
        return "Musique & Groupes"
        
    # 6. Marques & Sports
    sports = [
        "fifa", "world cup", "nba", "nfl", "nhl", "mlb", "football", "soccer", "baseball", "rugby",
        "chelsea", "arsenal", "liverpool", "manchester", "barcelona", "real madrid", "juventus",
        "ferrari", "porsche", "ford", "harley", "corvette", "coca-cola", "pepsi", "mcdonald",
        "nasa", "olympics", "tour de france", "nascar", "wwe", "bayern", "dortmund", "celtics",
        "lakers", "red sox", "yankees", "corvette", "mustang", "jeep", "caterpillar", "john deere",
        "heineken", "guinness", "starbucks", "sports editions", "motorsports"
    ]
    if any(k in combined for k in sports) or "sports" in cats_str:
        return "Marques & Sports"
        
    # 7. Films & Séries
    films = [
        "star wars", "lord of the rings", "harry potter", "game of thrones", "stranger things",
        "friends", "marvel", "avengers", "batman", "superman", "dc comics", "spider-man",
        "disney", "pixar", "jurassic", "back to the future", "james bond", "007", "doctor who",
        "star trek", "the office", "walking dead", "breaking bad", "peaky blinders", "godfather",
        "ghostbusters", "simpsons", "rick & morty", "rick and morty", "transformers", "godzilla",
        "nightmare before christmas", "shrek", "fast & furious", "twilight", "seinfeld", "south park",
        "family guy", "futurama", "golden girls", "big bang theory", "gremlins", "et the extra",
        "indiana jones", "wizard of oz", "willy wonka", "looney tunes", "flintstones", "scooby-doo",
        "muppets", "sesame street", "sponge bob", "spongebob", "disney", "marvel", "pixar"
    ]
    if any(k in combined for k in films) or "movie" in cats_str or "television" in cats_str or "film" in cats_str:
        return "Films & Séries"
        
    # 8. Villes & Régions (France)
    fr_locs = [
        "france", "paris", "marseille", "lyon", "toulouse", "bordeaux", "nantes", "lille", "nice",
        "strasbourg", "rennes", "montpellier", "grenoble", "dijon", "bretagne", "alsace", "corse",
        "normandie", "provence", "pays basque", "auvergne", "bourgogne", "lorraine", "reunion",
        "antilles", "martinique", "guadeloupe", "polynesie", "chamonix", "saint-tropez", "avignon",
        "toulon", "angers", "nîmes", "le havre", "clermont"
    ]
    if any(c in title_l for c in fr_locs) or "french editions" in cats_str:
        return "Villes & Régions (France)"
        
    # 9. Villes & Pays (Monde)
    world = [
        "london", "new york", "chicago", "las vegas", "los angeles", "boston", "san francisco",
        "dubai", "tokyo", "hong kong", "sydney", "berlin", "madrid", "barcelona", "amsterdam",
        "rome", "dublin", "canada", "australia", "germany", "italy", "spain", "mexico", "brazil",
        "world edition", "here & now", "city editions", "national editions", "ireland", "scotland",
        "wales", "switzerland", "austria", "belgium", "netherlands", "portugal", "greece", "russia",
        "china", "japan", "singapore", "new zealand", "south africa", "egypt", "israel", "argentina"
    ]
    if any(w in title_l for w in world) or "city editions" in cats_str or "uk editions" in cats_str or "us related editions" in cats_str:
        return "Villes & Pays (Monde)"
        
    # 10. Classique & Anniversaire
    classic = [
        "1935", "1936", "1937", "194", "195", "196", "197", "198", "199", "anniversary", "deluxe",
        "commemorative", "nostalgia", "vintage", "original", "standard edition", "first edition",
        "classic", "wood edition", "tin edition", "signature", "heritage", "legacy"
    ]
    if any(c in title_l for c in classic) or "anniversary editions" in cats_str or "us standard editions" in cats_str:
        return "Classique & Anniversaire"
        
    return "Éditions Spéciales & Thématiques"

def detect_year(title, cats):
    for c in cats:
        m = re.search(r"\b(19\d\d|20[0-2]\d)\b", c)
        if m:
            return int(m.group(1))
    m = re.search(r"\b(19\d\d|20[0-2]\d)\b", title)
    if m:
        return int(m.group(1))
    return 2010

def detect_publisher(title, cats):
    combined = (title + " " + " ".join(cats)).lower()
    if "winning moves" in combined:
        return "Winning Moves"
    if "usaopoly" in combined or "the op" in combined:
        return "USAopoly / The Op"
    if "parker brothers" in combined or "parker" in combined:
        return "Parker Brothers"
    if "waddington" in combined:
        return "Waddingtons"
    if "miro company" in combined or "miro" in combined:
        return "Miro Company"
    if "eleven force" in combined:
        return "Eleven Force"
    if "franklin mint" in combined:
        return "Franklin Mint"
    return "Hasbro"

def detect_country(title, cats):
    combined = (title + " " + " ".join(cats)).lower()
    if "france" in combined or "french" in combined or "paris" in combined:
        return "France"
    if "uk" in combined or "british" in combined or "london" in combined or "england" in combined:
        return "Royaume-Uni"
    if "germany" in combined or "german" in combined:
        return "Allemagne"
    if "italy" in combined or "italian" in combined:
        return "Italie"
    if "spain" in combined or "spanish" in combined:
        return "Espagne"
    if "canada" in combined or "canadian" in combined:
        return "Canada"
    if "australia" in combined or "australian" in combined:
        return "Australie"
    if "usa" in combined or "american" in combined or "us " in combined:
        return "USA"
    return "Monde"

def download_single_image(args):
    img_id, url, dest_path = args
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        return img_id, True, dest_path
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            if len(data) > 1000:
                with open(dest_path, "wb") as f:
                    f.write(data)
                return img_id, True, dest_path
    except Exception as e:
        pass
    return img_id, False, None

def run_build():
    print("Loading raw Fandom data...")
    with open("scratch/fandom_details_raw.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Filter out non-games
    non_game_cats = {'Properties', 'Spaces', 'Streets', 'Railroads', 'Game Elements', 'Rules', 'Utilities', 'Tokens'}
    game_entries = {}
    for title, item in raw_data.items():
        cats = set(item.get('categories', []))
        if not cats.intersection(non_game_cats):
            game_entries[title] = item

    print(f"Total valid game entries from Fandom: {len(game_entries)}")

    # Load existing seed to preserve manual descriptions and IDs
    with open("editions_seed.json", "r", encoding="utf-8") as f:
        existing_seed = json.load(f)

    existing_map = {}
    for e in existing_seed:
        existing_map[e["id"]] = e
        # Also map clean lowercase names
        existing_map[e["name"].lower().strip()] = e

    print(f"Loaded {len(existing_seed)} existing seed items.")

    # Image download queue
    download_queue = []
    
    # Process each Fandom entry
    all_editions = []
    seen_ids = set()

    # First add all existing curated seed entries
    for e in existing_seed:
        all_editions.append(e)
        seen_ids.add(e["id"])

    # Specific mapping for user requested items
    special_names = {
        "Builder Edition": {
            "name": "Monopoly Builder",
            "desc": "Monopoly avec jeu de construction 3D : empilez des blocs de construction sur l'île centrale au fil de la partie.",
            "category": "Variantes & Règles Spéciales"
        },
        "Monopoly Knockout": {
            "name": "Monopoly Glisse (Monopoly Knockout)",
            "desc": "Jeu d'adresse rapide et convivial : glissez vos palets sur un plateau de jeu allongé pour occuper des propriétés ou éjecter vos adversaires !",
            "category": "Variantes & Règles Spéciales"
        }
    }

    for title, item in game_entries.items():
        clean_title = title.strip()
        # Ensure Monopoly is in the name
        if not clean_title.lower().startswith("monopoly"):
            display_name = f"Monopoly {clean_title}"
        else:
            display_name = clean_title

        # Check special overrides
        desc = item.get("extract", "").strip()
        cat = detect_category(title, item["categories"], desc)
        if title in special_names:
            display_name = special_names[title]["name"]
            desc = special_names[title]["desc"]
            cat = special_names[title]["category"]

        # Check if already in existing seed
        if display_name.lower().strip() in existing_map:
            # Update existing with image if missing
            existing_item = existing_map[display_name.lower().strip()]
            if not existing_item.get("image_url") and item.get("thumbnail"):
                thumb_url = item["thumbnail"]
                ext = ".png" if ".png" in thumb_url.lower() else ".jpg"
                filename = f"box_{existing_item['id']}{ext}"
                dest = os.path.join(IMAGES_DIR, filename)
                download_queue.append((existing_item["id"], thumb_url, dest))
                existing_item["image_url"] = f"images/{filename}"
                existing_item["is_verified_box"] = True
            continue

        # Generate unique ID
        slug = re.sub(r'[^a-z0-9]+', '-', display_name.lower()).strip('-')[:50]
        if not slug:
            slug = f"edition-{len(all_editions)+1}"
        item_id = f"mono-{slug}"
        counter = 1
        orig_id = item_id
        while item_id in seen_ids:
            item_id = f"{orig_id}-{counter}"
            counter += 1
        seen_ids.add(item_id)

        year = detect_year(title, item["categories"])
        publisher = detect_publisher(title, item["categories"])
        country = detect_country(title, item["categories"])
        
        if not desc:
            desc = f"Édition {display_name} éditée par {publisher}."

        local_img = ""
        is_verified = False
        if item.get("thumbnail"):
            thumb_url = item["thumbnail"]
            ext = ".png" if ".png" in thumb_url.lower() else ".jpg"
            filename = f"box_{item_id}{ext}"
            dest = os.path.join(IMAGES_DIR, filename)
            download_queue.append((item_id, thumb_url, dest))
            local_img = f"images/{filename}"
            is_verified = True

        new_edition = {
            "id": item_id,
            "name": display_name,
            "category": cat,
            "year": year,
            "country": country,
            "publisher": publisher,
            "description": desc[:300],
            "image_url": local_img,
            "is_verified_box": is_verified
        }
        all_editions.append(new_edition)

    print(f"Total compiled editions: {len(all_editions)}")
    print(f"Total box covers to download/verify: {len(download_queue)}")

    # Download images using ThreadPoolExecutor
    print("Downloading authentic box covers in parallel (10 threads)...")
    success_count = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(download_single_image, q): q for q in download_queue}
        done = 0
        for future in as_completed(futures):
            done += 1
            img_id, ok, path = future.result()
            if ok:
                success_count += 1
            if done % 50 == 0 or done == len(download_queue):
                print(f"  Downloaded {done}/{len(download_queue)} images (Success: {success_count})")

    # If any download failed, reset image_url for that entry to avoid broken images
    for ed in all_editions:
        if ed.get("image_url") and ed["image_url"].startswith("images/"):
            local_path = os.path.join(BASE_DIR, ed["image_url"])
            if not os.path.exists(local_path) or os.path.getsize(local_path) < 1000:
                ed["image_url"] = ""
                ed["is_verified_box"] = False

    with_imgs = [e for e in all_editions if e.get("image_url")]
    print(f"\nFinal tally:")
    print(f"Total editions in master database: {len(all_editions)}")
    print(f"Total verified local box images: {len(with_imgs)} ({len(with_imgs)*100//len(all_editions)}%)")

    # Save to editions_seed.json
    all_editions.sort(key=lambda x: x["name"])
    with open("editions_seed.json", "w", encoding="utf-8") as f:
        json.dump(all_editions, f, ensure_ascii=False, indent=2)

    print("Saved master database to editions_seed.json")

if __name__ == "__main__":
    run_build()
