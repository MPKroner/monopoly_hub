# -*- coding: utf-8 -*-
"""
Process Fandom raw details into clean edition entries.
"""
import json
import re

with open("scratch/fandom_details_raw.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

print(f"Total raw items: {len(raw_data)}")

# Load existing seed to preserve existing IDs and rich data
with open("editions_seed.json", "r", encoding="utf-8") as f:
    existing_seed = json.load(f)

existing_by_name = {e["name"].lower().strip(): e for e in existing_seed}
print(f"Existing seed entries: {len(existing_seed)}")

processed = []
seen_slugs = set()

# Helper to determine category from title & categories
def detect_category(title, cats):
    title_lower = title.lower()
    cats_str = " ".join(cats).lower()
    
    # 1. Junior / Kids
    if "junior" in title_lower or "junior" in cats_str or "kids" in title_lower or "my first" in title_lower:
        return "Junior & Enfants"
        
    # 2. Variants & Special Rules
    variants_keywords = [
        "builder", "knockout", "cheaters", "sore losers", "mauvais perdants", "crooked cash",
        "faux billets", "deal", "speed", "bid", "chance", "longest game", "empire", "millionaire",
        "electronic banking", "ultimate banking", "voice banking", "revolution", "live", "city",
        "crazy cash", "grab & go", "travel", "express", "flip", "scrabble", "mega edition",
        "super electronic", "social distancing", "for millennials", "pizza", "target", "surprise",
        "arcade pac-man"
    ]
    if any(k in title_lower for k in variants_keywords) or "board game variants" in cats_str:
        return "Variantes & Règles Spéciales"
        
    # 3. Video Games
    vg_keywords = [
        "nintendo", "pokemon", "pokémon", "zelda", "mario", "gamer", "sonic", "fallout", "skyrim",
        "halo", "assassin", "cyberpunk", "overwatch", "minecraft", "fortnite", "world of warcraft",
        "warcraft", "animal crossing", "street fighter", "pac-man", "mega man", "uncharted",
        "playstation", "xbox", "sega", "resident evil", "apex legends", "league of legends",
        "roblox", "witcher", "crash bandicoot", "dungeons & dragons", "d&d", "magic the gathering"
    ]
    if any(k in title_lower for k in vg_keywords) or "video game" in cats_str:
        return "Jeux Vidéo"
        
    # 4. Anime & Manga
    anime_keywords = [
        "dragon ball", "dbz", "naruto", "one piece", "my hero academia", "attack on titan",
        "death note", "sailor moon", "astérix", "asterix", "tintin", "lucky luke", "demon slayer",
        "jujutsu kaisen", "tokyo ghoul", "bleach", "hunter x hunter", "cowboy bebop", "yu-gi-oh"
    ]
    if any(k in title_lower for k in anime_keywords) or "anime" in cats_str or "manga" in cats_str:
        return "Anime & Manga"
        
    # 5. Music & Bands
    music_keywords = [
        "beatles", "queen", "ac/dc", "acdc", "metallica", "iron maiden", "kiss", "rolling stones",
        "elvis", "david bowie", "grateful dead", "pink floyd", "bob marley", "led zeppelin",
        "eminem", "music"
    ]
    if any(k in title_lower for k in music_keywords) or "music" in cats_str or "band" in cats_str:
        return "Musique & Groupes"
        
    # 6. Brands & Sports
    sports_keywords = [
        "fifa", "world cup", "nba", "nfl", "nhl", "mlb", "football", "soccer", "baseball", "rugby",
        "chelsea", "arsenal", "liverpool", "manchester", "barcelona", "real madrid", "juventus",
        "ferrari", "porsche", "ford", "harley", "corvette", "coca-cola", "pepsi", "mcdonald",
        "nasa", "olympics", "tour de france", "nascar", "wwe"
    ]
    if any(k in title_lower for k in sports_keywords) or "sports" in cats_str or "brand" in cats_str:
        return "Marques & Sports"
        
    # 7. Movies & TV Series
    film_keywords = [
        "star wars", "lord of the rings", "harry potter", "game of thrones", "stranger things",
        "friends", "marvel", "avengers", "batman", "superman", "dc comics", "spider-man",
        "disney", "pixar", "jurassic", "back to the future", "james bond", "007", "doctor who",
        "star trek", "the office", "walking dead", "breaking bad", "peaky blinders", "godfather",
        "ghostbusters", "simpsons", "rick & morty", "rick and morty", "sponge", "transformers",
        "godzilla", "nightmare before christmas", "shrek", "fast & furious", "twilight", "seinfeld"
    ]
    if any(k in title_lower for k in film_keywords) or "movie" in cats_str or "film" in cats_str or "television" in cats_str or "series" in cats_str:
        return "Films & Séries"
        
    # 8. French Cities & Regions
    fr_cities = [
        "france", "paris", "marseille", "lyon", "toulouse", "bordeaux", "nantes", "lille", "nice",
        "strasbourg", "rennes", "montpellier", "grenoble", "dijon", "bretagne", "alsace", "corse",
        "normandie", "provence", "pays basque", "auvergne", "bourgogne", "lorraine", "reunion",
        "antilles", "martinique", "guadeloupe", "polynesie", "chamonix", "saint-tropez", "avignon"
    ]
    if any(c in title_lower for c in fr_cities) or "french" in cats_str:
        return "Villes & Régions (France)"
        
    # 9. Cities & Countries (World)
    world_keywords = [
        "london", "new york", "chicago", "las vegas", "los angeles", "boston", "san francisco",
        "dubai", "tokyo", "hong kong", "sydney", "berlin", "madrid", "barcelona", "amsterdam",
        "rome", "dublin", "canada", "australia", "germany", "italy", "spain", "mexico", "brazil",
        "world edition", "here & now"
    ]
    if any(w in title_lower for w in world_keywords) or "city" in cats_str or "countries" in cats_str:
        return "Villes & Pays (Monde)"
        
    # 10. Classic & Historic Packaging
    if "anniversary" in title_lower or "anniversary" in cats_str or "commemorative" in title_lower or "deluxe" in title_lower or "nostalgia" in title_lower or "vintage" in title_lower or "edition originale" in title_lower or "classic" in title_lower or "standard" in title_lower:
        return "Classique & Anniversaire"
        
    return "Édition Spéciale & Thématique"

# Detect year
def detect_year(title, cats):
    for c in cats:
        m = re.search(r"\b(19\d\d|20[0-2]\d)\b", c)
        if m:
            return int(m.group(1))
    m = re.search(r"\b(19\d\d|20[0-2]\d)\b", title)
    if m:
        return int(m.group(1))
    return None

# Detect publisher
def detect_publisher(title, cats):
    cats_str = " ".join(cats).lower()
    title_lower = title.lower()
    if "winning moves" in cats_str or "winning moves" in title_lower:
        return "Winning Moves"
    if "usaopoly" in cats_str or "usaopoly" in title_lower or "the op" in title_lower:
        return "USAopoly / The Op"
    if "parker" in cats_str or "parker" in title_lower:
        return "Parker Brothers"
    if "waddington" in cats_str or "waddington" in title_lower:
        return "Waddingtons"
    if "miro" in cats_str or "miro" in title_lower:
        return "Miro Company"
    if "eleven force" in cats_str:
        return "Eleven Force"
    return "Hasbro"

# Detect country
def detect_country(title, cats):
    cats_str = " ".join(cats).lower()
    title_lower = title.lower()
    if "french" in cats_str or "france" in title_lower:
        return "France"
    if "uk" in cats_str or "british" in cats_str or "london" in title_lower:
        return "Royaume-Uni"
    if "german" in cats_str or "germany" in title_lower:
        return "Allemagne"
    if "italian" in cats_str or "italy" in title_lower:
        return "Italie"
    if "spanish" in cats_str or "spain" in title_lower:
        return "Espagne"
    if "canadian" in cats_str or "canada" in title_lower:
        return "Canada"
    if "australian" in cats_str or "australia" in title_lower:
        return "Australie"
    if "american" in cats_str or "usa" in cats_str or "us" in cats_str:
        return "USA"
    return "Monde"

# Test classification
counts = {}
with_covers = 0
for title, item in raw_data.items():
    cat = detect_category(title, item["categories"])
    counts[cat] = counts.get(cat, 0) + 1
    if item.get("thumbnail"):
        with_covers += 1

print("\nCategory Distribution:")
for cat, count in sorted(counts.items(), key=lambda x: -x[1]):
    print(f" - {cat}: {count}")

print(f"\nTotal covers available: {with_covers}/{len(raw_data)}")
