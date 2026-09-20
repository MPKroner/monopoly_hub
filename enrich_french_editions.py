# -*- coding: utf-8 -*-
"""
Enrich Monopoly Tracker with missing French editions from Le Bon Coin, Vinted, eBay, and Parker/Hasbro archives.
"""
import json
import os

with open("editions_seed.json", "r", encoding="utf-8") as f:
    seed = json.load(f)

print(f"Current seed count: {len(seed)}")

seed_map = {e["id"]: e for e in seed}
# Also map by name lowercase
name_map = {e["name"].lower().strip(): e for e in seed}

# 1. THE USER'S EXACT EDITION:
exact_user_edition = {
    "id": "mono-et-si-invente-aujourdhui",
    "name": "Monopoly : Et si Monopoly était inventé aujourd'hui ?",
    "category": "Classique & Anniversaire",
    "year": 2006,
    "country": "France",
    "publisher": "Parker / Hasbro",
    "description": "Édition spéciale 70ème anniversaire célébrant la modernité avec les lieux emblématiques de Paris (Stade de France, Musée d'Orsay, Notre-Dame, Tour Eiffel, Bourse), décapotable rouge 'MR M70', loyers en millions d'euros (Départ 2M€) et 6 pions spéciaux : téléphone portable clapet, paire de rollers, skateboard, cheeseburger, avion, Formule 1. Réf. 100601595101.",
    "image_url": "images/box_mono-et-si-invente-aujourdhui.jpg",
    "is_verified_box": True
}

# New French editions to add or update
french_editions_to_add = [
    exact_user_edition,
    {
        "id": "mono-et-si-invente-electronique",
        "name": "Monopoly : Et si Monopoly était inventé aujourd'hui ? (Édition Électronique)",
        "category": "Variantes & Règles Spéciales",
        "year": 2006,
        "country": "France",
        "publisher": "Parker / Hasbro",
        "description": "Version électronique avec terminal bancaire et cartes de crédit Visa Monopoly pour des transactions rapides en millions d'euros.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-france-villes-2008",
        "name": "Monopoly : Les Villes de France (Et si le Monopoly était inventé aujourd'hui ?)",
        "category": "Villes & Régions (France)",
        "year": 2008,
        "country": "France",
        "publisher": "Hasbro / Parker",
        "description": "Édition historique issue du grand vote national des Français en 2008 : Dunkerque est élue sur la case Rue de la Paix, Montauban sur les Champs-Élysées, et 20 autres villes françaises représentées.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-live-2011",
        "name": "Monopoly Live",
        "category": "Variantes & Règles Spéciales",
        "year": 2011,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Tour de contrôle centrale infrarouge qui observe les mouvements de dés, parle aux joueurs, gère les enchères et les événements météo en direct.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-revolution-75th",
        "name": "Monopoly Révolution (75ème Anniversaire)",
        "category": "Classique & Anniversaire",
        "year": 2010,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Plateau circulaire / rond spectaculaire créé pour les 75 ans du Monopoly, avec unité sonore centrale diffusant de vrais morceaux de musique et effets sonores.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-city-3d",
        "name": "Monopoly City",
        "category": "Variantes & Règles Spéciales",
        "year": 2009,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Jeu de construction urbaine en 3D : bâtissez des gratte-ciels, maisons, stades et zones industrielles au centre du plateau grâce à l'unité de construction électronique.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-millionnaire",
        "name": "Monopoly Millionnaire",
        "category": "Variantes & Règles Spéciales",
        "year": 2012,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Course au premier million : le premier joueur qui réussit à amasser 1 000 000 € gagne immédiatement ! Pions évolutifs (bateau, limousine, jet privé).",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-u-build",
        "name": "Monopoly U-Build",
        "category": "Variantes & Règles Spéciales",
        "year": 2010,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Plateau modulable composé de tuiles de piste emboîtables en plastique permettant de créer différentes longueurs de plateau et formes de circuits.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-speed-2020",
        "name": "Monopoly Speed",
        "category": "Variantes & Règles Spéciales",
        "year": 2020,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Partie garantie en moins de 10 minutes ! Tout le monde lance les dés et achète en même temps pendant des manches chronométrées.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-bid-2020",
        "name": "Monopoly Bid",
        "category": "Variantes & Règles Spéciales",
        "year": 2020,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Jeu de cartes rapide et tactique basé sur des enchères à l'aveugle pour rafler des groupes de propriétés.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-chance-2023",
        "name": "Monopoly Chance",
        "category": "Variantes & Règles Spéciales",
        "year": 2023,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Jeu de cartes et de dés rapides : tentez votre chance pour acheter des propriétés sans faire faillite !",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-voice-banking",
        "name": "Monopoly Voix (Voice Banking)",
        "category": "Variantes & Règles Spéciales",
        "year": 2019,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Le chapeau haut-de-forme électronique de Mr. Monopoly écoute votre voix et gère les transactions financières sans aucun billet ni carte.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-super-electronic-banking",
        "name": "Monopoly Super Electronic Banking (Banque Électronique Récompenses)",
        "category": "Variantes & Règles Spéciales",
        "year": 2020,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Terminal bancaire tout-en-un avec cartes de récompenses uniques accordant des bonus spécifiques à chaque joueur.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-nostalgie-bois",
        "name": "Monopoly Édition Nostalgie (Boîte Coffret Bois)",
        "category": "Classique & Anniversaire",
        "year": 2001,
        "country": "France / Monde",
        "publisher": "Parker Brothers / Hasbro",
        "description": "Magnifique coffret en bois massif teinté avec plateau vintage d'époque, casier de rangement en bois et pions moulés sous pression.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-fr-1961-blanche",
        "name": "Monopoly France 1961 (Boîte Blanche Historique)",
        "category": "Classique & Anniversaire",
        "year": 1961,
        "country": "France",
        "publisher": "Miro Company",
        "description": "La célèbre boîte blanche Miro Company des années 60 avec plateau plié en deux, billets de 100 à 100 000 Francs et maisons en bois.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-fr-1973-rouge",
        "name": "Monopoly France 1973 (Boîte Rouge Vintage)",
        "category": "Classique & Anniversaire",
        "year": 1973,
        "country": "France",
        "publisher": "Parker Brothers",
        "description": "L'édition culte des années 70 avec la grande boîte rouge, les illustrations pop et les célèbres pions métal (chapeau, dé à coudre, fer à repasser, chaussure, canon, chien terrier).",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-fr-1993-standard",
        "name": "Monopoly France 1993 (Boîte Rouge Rues de Paris)",
        "category": "Classique & Anniversaire",
        "year": 1993,
        "country": "France",
        "publisher": "Parker Brothers / Hasbro",
        "description": "L'édition référence des années 90 en Francs français avec thermoformage plastique noir et graphisme modernisé.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-fr-2001-euro",
        "name": "Monopoly France 2001 (Passage à l'Euro)",
        "category": "Classique & Anniversaire",
        "year": 2001,
        "country": "France",
        "publisher": "Parker / Hasbro",
        "description": "Édition spéciale éditée lors du passage historique du franc français à la monnaie unique européenne (€).",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-fr-2013-chat",
        "name": "Monopoly France 2013 (Nouveau Pion Chat)",
        "category": "Classique & Anniversaire",
        "year": 2013,
        "country": "France",
        "publisher": "Hasbro",
        "description": "Édition accueillant le nouveau pion Chat pour remplacer le fer à repasser suite à la première grande campagne de vote mondial.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-fr-2017-trex",
        "name": "Monopoly France 2017 (Nouveaux Pions T-Rex & Canard)",
        "category": "Classique & Anniversaire",
        "year": 2017,
        "country": "France",
        "publisher": "Hasbro",
        "description": "Édition intégrant le T-Rex, le Canard en plastique et le Pingouin après le vote planétaire de 2017.",
        "image_url": "",
        "is_verified_box": False
    },
    # Junior French editions
    {
        "id": "mono-junior-1990",
        "name": "Monopoly Junior Fête Foraine (Original 1990)",
        "category": "Junior & Enfants",
        "year": 1990,
        "country": "France / Monde",
        "publisher": "Parker Brothers",
        "description": "La version originale pour enfants avec les stands de fête foraine (Stand de frites, Barbe à papa, Grande roue, Montagnes russes) et billets simplifiés de 1 à 5.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-junior-pat-patrouille",
        "name": "Monopoly Junior Pat' Patrouille (Paw Patrol)",
        "category": "Junior & Enfants",
        "year": 2021,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Aventure avec Chase, Marcus, Ruben et Stella dans la Grande Vallée.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-junior-reine-des-neiges",
        "name": "Monopoly Junior La Reine des Neiges (Frozen)",
        "category": "Junior & Enfants",
        "year": 2015,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Arendelle avec Elsa, Anna et Olaf : achetez des lieux magiques du royaume glacé.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-junior-peppa-pig",
        "name": "Monopoly Junior Peppa Pig",
        "category": "Junior & Enfants",
        "year": 2021,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Explorez l'univers de Peppa Pig, George, Maman Pig et Papa Pig avec les bottes de pluie !",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-junior-miraculous",
        "name": "Monopoly Junior Miraculous : Les Aventures de Ladybug et Chat Noir",
        "category": "Junior & Enfants",
        "year": 2022,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Protégez Paris des akumatisés avec Ladybug, Chat Noir, Tikki et Plagg.",
        "image_url": "",
        "is_verified_box": False
    },
    # Missing French regional bestsellers from Le Bon Coin / Vinted
    {
        "id": "mono-region-arcachon",
        "name": "Monopoly Bassin d'Arcachon",
        "category": "Villes & Régions (France)",
        "year": 2007,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Dune du Pilat, Banc d'Arguin, cabanes tchanquées de l'Île aux Oiseaux, Cap Ferret et dégustation d'huîtres.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-baie-de-somme",
        "name": "Monopoly Baie de Somme",
        "category": "Villes & Régions (France)",
        "year": 2014,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Saint-Valery-sur-Somme, Le Crotoy, Parc du Marquenterre, les phoques de la baie et le petit train à vapeur.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-ville-biarritz",
        "name": "Monopoly Biarritz & Côte Basque",
        "category": "Villes & Régions (France)",
        "year": 2005,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Rocher de la Vierge, Hôtel du Palais, Grande Plage, spots de surf légendaires et casino.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-calvados",
        "name": "Monopoly Calvados",
        "category": "Villes & Régions (France)",
        "year": 2011,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Pays d'Auge, Deauville, Trouville, Honfleur, Bayeux et plages du Débarquement.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-cevennes",
        "name": "Monopoly Cévennes",
        "category": "Villes & Régions (France)",
        "year": 2015,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Parc national des Cévennes, Gorges du Tarn, Mont Aigoual, Bambouseraie d'Anduze et châtaigniers.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-champagne",
        "name": "Monopoly Champagne",
        "category": "Villes & Régions (France)",
        "year": 2008,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Grandes maisons de champagne d'Épernay et Reims, côte des Blancs, Montagne de Reims et caves historiques.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-dordogne",
        "name": "Monopoly Dordogne - Périgord",
        "category": "Villes & Régions (France)",
        "year": 2010,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Grotte de Lascaux, Sarlat-la-Canéda, châteaux de Castelnaud et Beynac, truffes et foie gras du Périgord.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-ile-de-re",
        "name": "Monopoly Île de Ré",
        "category": "Villes & Régions (France)",
        "year": 2008,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Saint-Martin-de-Ré, Phare des Baleines, marais salants, roses trémières et pistes cyclables.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-jura",
        "name": "Monopoly Jura",
        "category": "Villes & Régions (France)",
        "year": 2012,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Cascades du Hérisson, Lac de Vouglans, vignoble d'Arbois (Vin Jaune), Comté et massif jurassien.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-landes",
        "name": "Monopoly Landes",
        "category": "Villes & Régions (France)",
        "year": 2013,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Hossegor, Biscarrosse, Capbreton, forêt des Landes de Gascogne, ferias de Dax et Mont-de-Marsan.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-morbihan",
        "name": "Monopoly Morbihan",
        "category": "Villes & Régions (France)",
        "year": 2011,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Golfe du Morbihan, mégalithes de Carnac, presqu'île de Quiberon, Vannes, Belle-Île-en-Mer.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-savoie",
        "name": "Monopoly Savoie & Haute-Savoie (Mont-Blanc)",
        "category": "Villes & Régions (France)",
        "year": 2006,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Chamonix, Mont-Blanc, Annecy et son lac, Chambéry, stations de ski et gastronomie savoyarde.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-touraine",
        "name": "Monopoly Touraine & Châteaux de la Loire",
        "category": "Villes & Régions (France)",
        "year": 2009,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Châteaux de Chenonceau, Chambord, Amboise, Azay-le-Rideau, Tours et vignobles de Vouvray.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-vendee",
        "name": "Monopoly Vendée",
        "category": "Villes & Régions (France)",
        "year": 2008,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Les Sables-d'Olonne (Vendée Globe), Puy du Fou, Île d'Yeu, Île de Noirmoutier et Marais Poitevin.",
        "image_url": "",
        "is_verified_box": False
    },
    {
        "id": "mono-region-vosges",
        "name": "Monopoly Vosges",
        "category": "Villes & Régions (France)",
        "year": 2014,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Gérardmer, La Bresse, Massif des Vosges, Crêtes, thermalisme de Vittel et Épinal.",
        "image_url": "",
        "is_verified_box": False
    }
]

added_count = 0
updated_count = 0

for item in french_editions_to_add:
    clean_name = item["name"].lower().strip()
    if item["id"] in seed_map:
        seed_map[item["id"]].update(item)
        updated_count += 1
    elif clean_name in name_map:
        name_map[clean_name].update(item)
        updated_count += 1
    else:
        seed.append(item)
        seed_map[item["id"]] = item
        name_map[clean_name] = item
        added_count += 1

print(f"Added {added_count} new French editions, updated {updated_count} existing editions.")
print(f"New total editions: {len(seed)}")

seed.sort(key=lambda x: x["name"])
with open("editions_seed.json", "w", encoding="utf-8") as f:
    json.dump(seed, f, ensure_ascii=False, indent=2)

print("Saved updated editions_seed.json")
