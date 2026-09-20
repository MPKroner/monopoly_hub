# -*- coding: utf-8 -*-
"""
Helper to enrich editions with theme colors, icons, and curated image support.
"""
import json

with open("C:/Users/Admin/.gemini/antigravity/scratch/monopoly-collection-tracker/editions_seed.json", "r", encoding="utf-8") as f:
    editions = json.load(f)

# Define thematic styles for editions
def get_theme(ed):
    name = ed.get("name", "").lower()
    cat = ed.get("category", "").lower()

    if "pokémon" in name or "pokemon" in name:
        return {"bg1": "#dc2626", "bg2": "#1e293b", "icon": "pokeball", "accent": "#facc15"}
    elif "zelda" in name:
        return {"bg1": "#064e3b", "bg2": "#022c22", "icon": "triforce", "accent": "#fbbf24"}
    elif "mario" in name:
        return {"bg1": "#b91c1c", "bg2": "#1d4ed8", "icon": "star", "accent": "#fde047"}
    elif "star wars" in name or "mandalorian" in name:
        return {"bg1": "#090d16", "bg2": "#1e1b4b", "icon": "space", "accent": "#38bdf8"}
    elif "harry potter" in name:
        return {"bg1": "#450a0a", "bg2": "#1c1917", "icon": "magic", "accent": "#f59e0b"}
    elif "seigneur des anneaux" in name or "lord of the rings" in name:
        return {"bg1": "#292524", "bg2": "#1c1917", "icon": "ring", "accent": "#eab308"}
    elif "game of thrones" in name:
        return {"bg1": "#18181b", "bg2": "#09090b", "icon": "crown", "accent": "#94a3b8"}
    elif "marvel" in name or "avengers" in name or "spiderman" in name:
        return {"bg1": "#991b1b", "bg2": "#1e1b4b", "icon": "shield", "accent": "#f87171"}
    elif "batman" in name:
        return {"bg1": "#18181b", "bg2": "#09090b", "icon": "bat", "accent": "#eab308"}
    elif "disney" in name:
        return {"bg1": "#1e1b4b", "bg2": "#312e81", "icon": "castle", "accent": "#67e8f9"}
    elif "fortnite" in name:
        return {"bg1": "#4338ca", "bg2": "#065f46", "icon": "fortnite", "accent": "#a855f7"}
    elif "minecraft" in name:
        return {"bg1": "#166534", "bg2": "#3f2d19", "icon": "cube", "accent": "#4ade80"}
    elif "dragon ball" in name:
        return {"bg1": "#ea580c", "bg2": "#1e3a8a", "icon": "dragonball", "accent": "#fbbf24"}
    elif "one piece" in name:
        return {"bg1": "#0369a1", "bg2": "#991b1b", "icon": "pirate", "accent": "#fde047"}
    elif "naruto" in name:
        return {"bg1": "#c2410c", "bg2": "#1e293b", "icon": "ninja", "accent": "#fdba74"}
    elif "paris" in name or "france" in name:
        return {"bg1": "#1e3a8a", "bg2": "#1e293b", "icon": "monument", "accent": "#ef4444"}
    elif "lyon" in name or "marseille" in name or "bordeaux" in name or "lille" in name or "nantes" in name:
        return {"bg1": "#1e40af", "bg2": "#0f172a", "icon": "city", "accent": "#60a5fa"}
    elif "bretagne" in name or "normandie" in name or "corse" in name or "alsace" in name:
        return {"bg1": "#047857", "bg2": "#0f172a", "icon": "region", "accent": "#34d399"}
    elif "beatles" in name or "queen" in name or "ac/dc" in name or "metallica" in name or "rolling stones" in name or "kiss" in name or "bowie" in name:
        return {"bg1": "#18181b", "bg2": "#27272a", "icon": "music", "accent": "#f43f5e"}
    elif "psg" in name or "paris saint-germain" in name:
        return {"bg1": "#1e3a8a", "bg2": "#991b1b", "icon": "football", "accent": "#f87171"}
    elif "om" in name or "marseille" in name and "club" in name:
        return {"bg1": "#0284c7", "bg2": "#0c4a6e", "icon": "football", "accent": "#38bdf8"}
    elif "real madrid" in name or "barca" in name or "juventus" in name or "manchester" in name or "fifa" in name:
        return {"bg1": "#15803d", "bg2": "#1e293b", "icon": "trophy", "accent": "#fde047"}
    elif "ferrari" in name:
        return {"bg1": "#b91c1c", "bg2": "#18181b", "icon": "car", "accent": "#facc15"}
    elif "harley" in name:
        return {"bg1": "#ea580c", "bg2": "#18181b", "icon": "motorcycle", "accent": "#fb923c"}
    elif "1935" in name or "deluxe" in name or "franklin" in name or "50ème" in name or "60ème" in name or "70ème" in name or "80ème" in name or "85ème" in name or "vintage" in name:
        return {"bg1": "#14532d", "bg2": "#3f2d19", "icon": "vintage", "accent": "#fbbf24"}
    elif "cheaters" in name or "tricheurs" in name or "faux billets" in name:
        return {"bg1": "#7f1d1d", "bg2": "#0f172a", "icon": "handcuffs", "accent": "#f87171"}
    elif "electronic" in name or "banque" in name or "voice" in name or "speed" in name:
        return {"bg1": "#0369a1", "bg2": "#0f172a", "icon": "electronic", "accent": "#38bdf8"}
    elif "jeux vidéo" in cat:
        return {"bg1": "#312e81", "bg2": "#0f172a", "icon": "gamepad", "accent": "#a855f7"}
    elif "films & séries" in cat:
        return {"bg1": "#4c0519", "bg2": "#18181b", "icon": "cinema", "accent": "#f43f5e"}
    elif "anime & manga" in cat:
        return {"bg1": "#7c2d12", "bg2": "#1e293b", "icon": "manga", "accent": "#fb923c"}
    elif "villes & pays" in cat:
        return {"bg1": "#0c4a6e", "bg2": "#0f172a", "icon": "globe", "accent": "#38bdf8"}
    elif "marques & sports" in cat:
        return {"bg1": "#065f46", "bg2": "#111827", "icon": "trophy", "accent": "#facc15"}
    else:
        return {"bg1": "#1e293b", "bg2": "#0f172a", "icon": "monopoly", "accent": "#e11d48"}

for ed in editions:
    t = get_theme(ed)
    ed["theme"] = t
    if "image_url" not in ed:
        ed["image_url"] = ""

with open("C:/Users/Admin/.gemini/antigravity/scratch/monopoly-collection-tracker/editions_seed.json", "w", encoding="utf-8") as f:
    json.dump(editions, f, ensure_ascii=False, indent=2)

print(f"Themes generated for {len(editions)} editions.")
