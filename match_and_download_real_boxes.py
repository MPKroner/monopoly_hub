# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import os
import re
import time

os.makedirs("images", exist_ok=True)

# 1. Fetch the 1674 edition titles from Monopoly Fandom
print("Fetching master list of Monopoly edition titles from Fandom...")
url = "https://monopoly.fandom.com/api.php?action=parse&page=List_of_Monopoly_Games_(Board)&prop=links&format=json"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    fandom_titles = [l["*"] for l in data.get("parse", {}).get("links", []) if l.get("ns") == 0]

print(f"Loaded {len(fandom_titles)} article titles from Fandom!")

# 2. Load our seed database
with open("editions_seed.json", "r", encoding="utf-8") as f:
    editions = json.load(f)

# Helper function to normalize strings for comparison
def normalize(s):
    s = s.lower()
    s = re.sub(r'monopoly\s*(:|-)?\s*', '', s)
    s = re.sub(r'[\(\)\[\],\.\':!\?]', ' ', s)
    return set(s.split())

# Mapping dictionary: edition_id -> best matching Fandom article title
matches = {}

# Custom exact mappings for difficult / multilingual titles
EXACT_MAPPINGS = {
    "mono-cheaters": "Cheaters Edition",
    "mono-mega": "The Mega Edition Monopoly",
    "mono-vg-zelda": "Legend of Zelda Edition",
    "mono-pop-got": "Game of Thrones Collector's Edition",
    "mono-vg-pokemon-kanto": "Pokemon Collector's Edition",
    "mono-vg-pokemon-johto": "Pokemon: Johto Edition",
    "mono-vg-fallout": "Fallout Collector's Edition",
    "mono-pop-stranger-things": "Stranger Things Edition",
    "mono-music-acdc": "AC/DC Collector's Edition",
    "mono-music-queen": "Queen Edition",
    "mono-music-beatles": "The Beatles Collector's Edition",
    "mono-music-metallica": "Metallica Collector's Edition",
    "mono-music-bowie": "David Bowie Edition",
    "mono-music-kiss": "KISS Collector's Edition",
    "mono-pop-friends": "Friends Edition",
    "mono-pop-tbbt": "The Big Bang Theory",
    "mono-pop-south-park": "South Park Collector's Edition",
    "mono-pop-breaking-bad": "Breaking Bad Edition",
    "mono-pop-james-bond": "007 Collector's Edition",
    "mono-pop-the-simpsons": "The Simpsons Edition",
    "mono-pop-jurassic-park": "Jurassic Park Edition",
    "mono-pop-back-to-the-future": "Back to the Future Edition",
    "mono-pop-the-walking-dead": "The Walking Dead: Survival Edition",
    "mono-pop-batman": "Batman Collector's Edition",
    "mono-pop-spiderman": "Spider-Man Edition",
    "mono-pop-ghostbusters": "Ghostbusters Collector's Edition",
    "mono-pop-doctor-who": "Doctor Who 50th Anniversary Collector's Edition",
    "mono-pop-rick-and-morty": "Rick and Morty Edition",
    "mono-pop-the-office": "The Office Edition",
    "mono-pop-starwars-classic": "Star Wars: The Clone Wars Edition",
    "mono-pop-starwars-mandalorian": "Star Wars: The Mandalorian Edition",
    "mono-pop-lotr": "The Lord of the Rings: The Motion Picture Trilogy Edition",
    "mono-pop-marvel-avengers": "Marvel Avengers Edition",
    "mono-vg-assassins-creed": "Assassin's Creed Edition",
    "mono-vg-skyrim": "The Elder Scrolls V: Skyrim Edition",
    "mono-vg-world-of-warcraft": "World of Warcraft Collector's Edition",
    "mono-vg-animal-crossing": "Animal Crossing: New Horizons Edition",
    "mono-vg-pacman": "Pac-Man Arcade Edition",
    "mono-vg-overwatch": "Overwatch Collector's Edition",
    "mono-vg-sonic": "Sonic the Hedgehog Collector's Edition",
    "mono-vg-halo": "Halo Collector's Edition",
    "mono-vg-resident-evil": "Resident Evil Collector's Edition",
    "mono-vg-cyberpunk": "Cyberpunk 2077 Edition",
    "mono-vg-street-fighter": "Street Fighter Collector's Edition",
    "mono-vg-crash-bandicoot": "Crash Bandicoot Edition",
    "mono-vg-roblox": "Roblox Edition",
    "mono-vg-gamer-mariokart": "Monopoly Gamer: Mario Kart Edition",
    "mono-vg-gamer-original": "Monopoly Gamer",
    "mono-vg-minecraft": "Minecraft",
    "mono-manga-aot": "Attack on Titan Edition",
    "mono-manga-mha": "My Hero Academia Edition",
    "mono-manga-sailor-moon": "Sailor Moon Edition",
    "mono-manga-yugioh": "Yu-Gi-Oh! Edition",
    "mono-manga-death-note": "Death Note Edition",
    "mono-city-london": "London Edition",
    "mono-city-newyork": "New York City Edition",
    "mono-city-tokyo": "Tokyo Edition",
    "mono-city-lasvegas": "Las Vegas Edition",
    "mono-city-rome": "Rome Edition",
    "mono-city-berlin": "Berlin Edition",
    "mono-city-sydney": "Sydney Edition",
    "mono-city-montreal": "Montreal Edition",
    "mono-city-hongkong": "Hong Kong Edition",
    "mono-city-dubai": "Dubai Edition",
    "mono-city-madrid": "Madrid Edition",
    "mono-city-amsterdam": "Amsterdam Edition",
    "mono-city-sanfrancisco": "San Francisco Edition",
    "mono-city-chicago": "Chicago Edition",
    "mono-brand-ferrari": "Formula One 2009 Edition",
    "mono-brand-harley": "Harley-Davidson 2nd Edition",
    "mono-brand-cocacola": "Coca-Cola 125th Anniversary Edition",
    "mono-brand-nasa": "NASA Edition",
    "mono-sport-nba": "NBA Edition",
    "mono-50th": "50th Anniversary Deluxe Edition",
    "mono-60th": "60th Anniversary Edition",
    "mono-70th": "70th Anniversary Edition",
    "mono-80th": "80th Anniversary Edition",
    "mono-85th": "85th Anniversary Edition",
    "mono-1935": "1935 Commemorative Edition",
    "mono-deluxe-1995": "1995 Deluxe Edition",
    "mono-vintage-wood": "1936 Deluxe Wood Edition",
    "mono-electronic-bank": "Electronic Banking Edition",
    "mono-ultimate-bank": "Ultimate Banking Edition",
    "mono-voice-banking": "Voice Banking Edition",
    "mono-speed": "Speed Edition",
    "mono-revolution": "Revolution Edition",
    "mono-empire": "Empire Edition",
    "mono-millennials": "Monopoly for Millennials",
    "mono-socialism": "Monopoly: Socialism",
    "mono-pizza": "Pizza Edition",
    "mono-bad-losers": "Monopoly: Sore Losers Edition",
    "mono-world-edition": "Here and Now: World Edition",
    "mono-be-bruxelles": "Brussels Edition",
    "mono-be-national": "Belgium Edition",
    "mono-ch-national": "Switzerland Edition",
    "mono-ch-geneve": "Geneva Edition",
    "mono-fr-standard": "French Edition",
    "mono-fr-1937": "Miro Company Edition",
    "mono-ville-paris": "Paris Edition",
    "mono-ville-lyon": "Lyon Edition",
    "mono-ville-marseille": "Marseille Edition",
    "mono-ville-bordeaux": "Bordeaux Edition",
    "mono-ville-lille": "Lille Edition",
    "mono-ville-strasbourg": "Strasbourg Edition",
    "mono-ville-nice": "Nice Edition",
    "mono-region-bretagne": "Brittany Edition",
    "mono-region-normandie": "Normandy Edition",
    "mono-region-corse": "Corsica Edition",
    "mono-region-alsace": "Alsace Edition",
    "mono-club-realmadrid": "Real Madrid C.F. Edition",
    "mono-club-barca": "FC Barcelona Edition",
    "mono-club-manutd": "Manchester United Edition",
    "mono-club-juventus": "Juventus F.C. Edition",
    "mono-sport-fifa-world-cup": "2006 FIFA World Cup Germany Edition"
}

for ed in editions:
    eid = ed["id"]
    if eid in EXACT_MAPPINGS:
        matches[eid] = EXACT_MAPPINGS[eid]
    else:
        # Fuzzy match with Fandom list
        ed_words = normalize(ed["name"])
        best_title = None
        best_score = 0
        for ft in fandom_titles:
            ft_words = normalize(ft)
            common = ed_words.intersection(ft_words)
            score = len(common)
            if score > best_score and score >= 2:
                best_score = score
                best_title = ft
        if best_title:
            matches[eid] = best_title

print(f"Matched {len(matches)} editions to official Fandom articles!")

# 3. Query Fandom API for image URLs in batches of 40
matched_titles = list(set(matches.values()))
title_to_image = {}

batch_size = 40
for i in range(0, len(matched_titles), batch_size):
    batch = matched_titles[i:i + batch_size]
    encoded = "|".join([urllib.parse.quote(t) for t in batch])
    url = f"https://monopoly.fandom.com/api.php?action=query&titles={encoded}&prop=pageimages&pithumbsize=600&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for pid, p in pages.items():
                title = p.get("title")
                thumb = p.get("thumbnail", {}).get("source")
                if thumb and title:
                    title_to_image[title] = thumb
    except Exception as e:
        print(f"Batch {i} error: {e}")
    time.sleep(0.3)

print(f"Retrieved {len(title_to_image)} real box cover image URLs from Fandom!")

# 4. Download images locally to /images/<id>.<ext>
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://monopoly.fandom.com/"
}

downloaded_count = 0
for ed in editions:
    eid = ed["id"]
    target_title = matches.get(eid)
    if not target_title:
        continue
    img_url = title_to_image.get(target_title)
    if not img_url:
        continue

    # Determine extension
    ext = "webp" if ".webp" in img_url or "scale-to" in img_url else "jpg"
    filename = f"{eid}.{ext}"
    filepath = os.path.join("images", filename)

    try:
        req = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            if len(content) > 1000:
                with open(filepath, "wb") as f:
                    f.write(content)
                ed["image_url"] = f"images/{filename}"
                downloaded_count += 1
                print(f"[{downloaded_count}] Saved box for: {ed['name']} -> {filepath}")
    except Exception as e:
        print(f"Failed download for {ed['name']}: {e}")

print(f"Successfully downloaded {downloaded_count} physical box covers locally!")

# 5. Save updated editions_seed.json
with open("editions_seed.json", "w", encoding="utf-8") as f:
    json.dump(editions, f, ensure_ascii=False, indent=2)

print("Updated editions_seed.json with local image paths.")
