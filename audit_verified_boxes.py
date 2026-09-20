# -*- coding: utf-8 -*-
import json
import os

# Clean verified matches table: eid -> verified filename
# We only keep files where we are 100% sure the cover is the EXACT edition!

VERIFIED_MATCHES = {
    # Anniversaries & Classics
    "mono-1935": "images/mono-1935.jpg",
    "mono-60th": "images/mono-60th.jpg",
    "mono-70th": "images/mono-70th.jpg",
    "mono-80th": "images/mono-80th.webp",
    "mono-85th": "images/mono-85th.webp",
    "mono-fr-standard": "images/mono-fr-standard.jpg",
    "mono-franklin-mint": "images/mono-franklin-mint.jpg",
    "mono-vintage-wood": "images/mono-vintage-wood.jpg",
    
    # Gameplay Variations
    "mono-cheaters": "images/mono-cheaters.webp",
    "mono-mega": "images/mono-mega.webp",
    "mono-crooked": "images/mono-crooked.webp",
    "mono-electronic-bank": "images/mono-electronic-bank.webp",
    "mono-ultimate-bank": "images/mono-ultimate-bank.jpg",
    "mono-voice-banking": "images/mono-voice-banking.webp",
    "mono-longest-game": "images/mono-longest-game.webp",
    "mono-speed": "images/mono-speed.webp",
    "mono-revolution": "images/mono-revolution.jpg",
    "mono-bad-losers": "images/mono-bad-losers.jpg",
    "mono-socialism": "images/mono-socialism.webp",
    "mono-millennials": "images/mono-millennials.webp",
    
    # Pop Culture - Cinema & TV
    "mono-pop-starwars-classic": "images/mono-pop-starwars-classic.webp",
    "mono-pop-starwars-mandalorian": "images/mono-pop-starwars-mandalorian.webp",
    "mono-pop-got": "images/mono-pop-got.webp",
    "mono-pop-stranger-things": "images/mono-pop-stranger-things.jpg",
    "mono-pop-breaking-bad": "images/mono-pop-breaking-bad.webp",
    "mono-pop-james-bond": "images/mono-pop-james-bond.jpg",
    "mono-pop-the-simpsons": "images/mono-pop-the-simpsons.jpg",
    "mono-pop-batman": "images/mono-pop-batman.jpg",
    "mono-pop-marvel-avengers": "images/mono-pop-marvel-avengers.jpg",
    "mono-pop-nightmare-christmas": "images/mono-pop-nightmare-christmas.webp",
    "mono-pop-the-walking-dead": "images/mono-pop-the-walking-dead.jpg",
    "mono-pop-the-office": "images/mono-pop-the-office.webp",
    "mono-pop-rick-and-morty": "images/mono-pop-rick-and-morty.webp",
    "mono-pop-tbbt": "images/mono-pop-tbbt.webp",
    "mono-pop-doctor-who": "images/mono-pop-doctor-who.jpg",
    "mono-pop-scoobydoo": "images/mono-pop-scoobydoo.jpg",
    "mono-pop-shrek": "images/mono-pop-shrek.jpg",
    "mono-pop-south-park": "images/mono-pop-south-park.jpg",
    "mono-pop-supernatural": "images/mono-pop-supernatural.jpg",
    "mono-pop-transformers": "images/mono-pop-transformers.jpg",
    "mono-pop-toy-story": "images/mono-pop-toy-story.webp",
    "mono-pop-disney-villains": "images/mono-pop-disney-villains.jpg",
    
    # Video Games
    "mono-vg-pokemon-kanto": "images/mono-vg-pokemon-kanto.webp",
    "mono-vg-zelda": "images/mono-vg-zelda.webp",
    "mono-vg-fallout": "images/mono-vg-fallout.webp",
    "mono-vg-assassins-creed": "images/mono-vg-assassins-creed.webp",
    "mono-vg-animal-crossing": "images/mono-vg-animal-crossing.webp",
    "mono-vg-nintendo-collector": "images/mono-vg-nintendo-collector.webp",
    "mono-vg-sonic": "images/mono-vg-sonic.webp",
    "mono-vg-roblox": "images/mono-vg-roblox.webp",
    "mono-vg-street-fighter": "images/mono-vg-street-fighter.jpg",
    "mono-vg-world-of-warcraft": "images/mono-vg-world-of-warcraft.jpg",
    
    # Manga & Anime
    "mono-manga-dbz": "images/mono-manga-dbz.jpg",
    "mono-manga-one-piece": "images/mono-manga-one-piece.webp",
    "mono-manga-yugioh": "images/mono-manga-yugioh.webp",
    
    # Music
    "mono-music-acdc": "images/mono-music-acdc.jpg",
    "mono-music-queen": "images/mono-music-queen.webp",
    "mono-music-beatles": "images/mono-music-beatles.webp",
    "mono-music-metallica": "images/mono-music-metallica.jpg",
    "mono-music-bowie": "images/mono-music-bowie.webp",
    "mono-music-iron-maiden": "images/mono-music-iron-maiden.webp",
    "mono-music-kiss": "images/mono-music-kiss.jpg",
    
    # Cities & World
    "mono-city-berlin": "images/mono-city-berlin.webp",
    "mono-city-amsterdam": "images/mono-city-amsterdam.jpg",
    "mono-city-chicago": "images/mono-city-chicago.jpg",
    "mono-city-lasvegas": "images/mono-city-lasvegas.jpg",
    "mono-region-alsace": "images/mono-region-alsace.jpg",
    "mono-world-edition": "images/mono-world-edition.jpg"
}

with open("editions_seed.json", "r", encoding="utf-8") as f:
    editions = json.load(f)

# Delete invalid images that were mismatched
all_files = [os.path.join("images", f) for f in os.listdir("images")]
for f in all_files:
    # normalize path with forward slash
    norm = f.replace("\\", "/")
    if norm not in VERIFIED_MATCHES.values() and not norm.endswith("test_cheaters.jpg"):
        try:
            os.remove(f)
            print(f"Removed mismatched file: {f}")
        except:
            pass

# Update editions_seed.json with only verified real box images
verified_count = 0
for ed in editions:
    eid = ed["id"]
    if eid in VERIFIED_MATCHES and os.path.exists(VERIFIED_MATCHES[eid]):
        ed["image_url"] = VERIFIED_MATCHES[eid]
        ed["is_verified_box"] = True
        verified_count += 1
    else:
        ed["image_url"] = ""
        ed["is_verified_box"] = False

with open("editions_seed.json", "w", encoding="utf-8") as f:
    json.dump(editions, f, ensure_ascii=False, indent=2)

print(f"Total verified 100% authentic physical box images: {verified_count}")
