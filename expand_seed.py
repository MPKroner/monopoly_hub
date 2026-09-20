# -*- coding: utf-8 -*-
import json

extra_editions = [
    # --- FOOTBALL & CLUBS ---
    {
        "id": "mono-club-psg",
        "name": "Monopoly Paris Saint-Germain (PSG)",
        "category": "Marques & Sports",
        "year": 2014,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Le Parc des Princes, les tribunes Auteuil et Boulogne, les joueurs et les trophées légendaires du PSG."
    },
    {
        "id": "mono-club-om",
        "name": "Monopoly Olympique de Marseille (OM)",
        "category": "Marques & Sports",
        "year": 2011,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Stade Vélodrome, Centre Robert Louis-Dreyfus, virages Nord et Sud, vainqueurs de la Ligue des Champions 1993."
    },
    {
        "id": "mono-club-realmadrid",
        "name": "Monopoly Real Madrid C.F.",
        "category": "Marques & Sports",
        "year": 2017,
        "country": "Espagne / International",
        "publisher": "Winning Moves",
        "description": "Stade Santiago Bernabéu, vestiaires, coupes d'Europe de la Maison Blanche et joueurs galactiques."
    },
    {
        "id": "mono-club-barca",
        "name": "Monopoly FC Barcelona",
        "category": "Marques & Sports",
        "year": 2016,
        "country": "Espagne / International",
        "publisher": "Eleven Force",
        "description": "Camp Nou, La Masia, musée du club « Més que un club », maillots blaugrana et trophées historiques."
    },
    {
        "id": "mono-club-manutd",
        "name": "Monopoly Manchester United",
        "category": "Marques & Sports",
        "year": 2015,
        "country": "Royaume-Uni / International",
        "publisher": "Winning Moves",
        "description": "Old Trafford (The Theatre of Dreams), Sir Alex Ferguson Stand et légendes des Red Devils."
    },
    {
        "id": "mono-club-juventus",
        "name": "Monopoly Juventus Football Club",
        "category": "Marques & Sports",
        "year": 2018,
        "country": "Italie / International",
        "publisher": "Winning Moves",
        "description": "Allianz Stadium de Turin, musée de la Juve, scudetti et légendes bianconeri."
    },

    # --- CINÉMA & SÉRIES ADDITIONNELLES ---
    {
        "id": "mono-pop-james-bond",
        "name": "Monopoly James Bond 007 Collector's Edition",
        "category": "Films & Séries",
        "year": 2008,
        "country": "Monde / France",
        "publisher": "Winning Moves",
        "description": "Tous les films de James Bond depuis Dr. No jusqu'à Spectre/No Time to Die. Pions Aston Martin DB5, pistolet Walther PPK."
    },
    {
        "id": "mono-pop-breaking-bad",
        "name": "Monopoly Breaking Bad",
        "category": "Films & Séries",
        "year": 2020,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Albuquerque : Los Pollos Hermanos, le labo clandestin, le camping-car Fleetwood Bounder, le chapeau Heisenberg."
    },
    {
        "id": "mono-pop-peaky-blinders",
        "name": "Monopoly Peaky Blinders",
        "category": "Films & Séries",
        "year": 2020,
        "country": "Royaume-Uni / France",
        "publisher": "Winning Moves",
        "description": "Birmingham dans les années 1920 : Garrison Tavern, Shelby Company Limited, pions casquette gavroche, fer à cheval."
    },
    {
        "id": "mono-pop-tbbt",
        "name": "Monopoly The Big Bang Theory",
        "category": "Films & Séries",
        "year": 2014,
        "country": "Monde / France",
        "publisher": "USAopoly / Winning Moves",
        "description": "L'appartement 4A de Sheldon et Leonard, la cafétéria de Caltech, pions canapé de Sheldon, lunettes de Leonard, Bazinga."
    },
    {
        "id": "mono-pop-south-park",
        "name": "Monopoly South Park Collector's Edition",
        "category": "Films & Séries",
        "year": 2013,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "L'école primaire de South Park, City Wok, Casa Bonita, pions Cartman, Stan, Kyle, Kenny, Servietsky."
    },
    {
        "id": "mono-pop-shrek",
        "name": "Monopoly Shrek 2 Collector's Edition",
        "category": "Films & Séries",
        "year": 2004,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Le Marais de Shrek, le Royaume de Fort Fort Lointain, la chaumière de la Fée Marraine, pions Âne, Shrek, Chat Potté."
    },
    {
        "id": "mono-pop-transformers",
        "name": "Monopoly Transformers Collector's Edition",
        "category": "Films & Séries",
        "year": 2007,
        "country": "Monde",
        "publisher": "USAopoly / Hasbro",
        "description": "Autobots vs Decepticons sur Cybertron et la Terre, pions Optimus Prime, Megatron, Bumblebee, Matrice de commandement."
    },
    {
        "id": "mono-pop-nightmare-christmas",
        "name": "Monopoly L'Étrange Noël de Monsieur Jack (Nightmare Before Christmas)",
        "category": "Films & Séries",
        "year": 2014,
        "country": "Monde / France",
        "publisher": "USAopoly",
        "description": "Ville d'Halloween et Ville de Noël avec Jack Skellington, Sally, Oogie Boogie, Zéro et la colline spiralée."
    },
    {
        "id": "mono-pop-toy-story",
        "name": "Monopoly Toy Story (Disney Pixar)",
        "category": "Films & Séries",
        "year": 2019,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "La chambre d'Andy, Pizza Planet, le magasin de jouets d'Al avec pions Woody, Buzz l'Éclair, Rex, Jessie, Kart."
    },
    {
        "id": "mono-pop-fast-and-furious",
        "name": "Monopoly Fast & Furious",
        "category": "Films & Séries",
        "year": 2023,
        "country": "Monde / France",
        "publisher": "Winning Moves",
        "description": "Les courses de rue et les braquages de la famille de Dom Toretto avec la mythique Dodge Charger R/T 1970."
    },
    {
        "id": "mono-pop-scoobydoo",
        "name": "Monopoly Scooby-Doo Collector's Edition",
        "category": "Films & Séries",
        "year": 2019,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Mystère et Compagnie : explorez les manoirs hantés à bord de la Mystery Machine avec des Scooby Snacks."
    },
    {
        "id": "mono-pop-supernatural",
        "name": "Monopoly Supernatural Collector's Edition",
        "category": "Films & Séries",
        "year": 2018,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Chassez démons et monstres avec Sam et Dean Winchester au volant de l'Impala 1967 (Baby)."
    },

    # --- JEUX VIDÉO ADDITIONNELS ---
    {
        "id": "mono-vg-gamer-mariokart",
        "name": "Monopoly Gamer Mario Kart",
        "category": "Jeux Vidéo",
        "year": 2018,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Chaque personnage a des capacités uniques ! Lancez des peaux de banane et carapaces bleues sur le plateau."
    },
    {
        "id": "mono-vg-gamer-original",
        "name": "Monopoly Gamer (Nintendo)",
        "category": "Jeux Vidéo",
        "year": 2017,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Le premier Monopoly Gamer fusionnant règles de jeu de plateau et mécaniques de combat de boss Nintendo."
    },
    {
        "id": "mono-vg-roblox",
        "name": "Monopoly Roblox",
        "category": "Jeux Vidéo",
        "year": 2021,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Achetez et collectionnez les meilleures expériences Roblox (Adopt Me, Brookhaven, MeepCity, Tower of Hell)."
    },
    {
        "id": "mono-vg-halo",
        "name": "Monopoly Halo Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2014,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Installation 04, Blood Gulch, Reach avec Master Chief, le Warthog, l'Épée à énergie et le Banshee."
    },
    {
        "id": "mono-vg-resident-evil",
        "name": "Monopoly Resident Evil Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2019,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Manoir Spencer, Commissariat de Raccoon City (R.P.D.), Umbrella Corporation avec Jill Valentine et Leon Kennedy."
    },
    {
        "id": "mono-vg-cyberpunk",
        "name": "Monopoly Cyberpunk 2077",
        "category": "Jeux Vidéo",
        "year": 2021,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "Explorez Night City, les corporations Arasaka et Militech, Watson et Westbrook avec Johnny Silverhand."
    },
    {
        "id": "mono-vg-street-fighter",
        "name": "Monopoly Street Fighter Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2012,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Dojos et arènes mythiques (Chine, Japon, Brésil, USA) avec Ryu, Ken, Chun-Li, Guile et M. Bison."
    },
    {
        "id": "mono-vg-crash-bandicoot",
        "name": "Monopoly Crash Bandicoot",
        "category": "Jeux Vidéo",
        "year": 2020,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "Les Îles Wumpa, la forteresse du Dr. Neo Cortex, pions masque Aku Aku, caisse TNT et fruit Wumpa."
    },

    # --- ANIME & BD ADDITIONNELS ---
    {
        "id": "mono-manga-sailor-moon",
        "name": "Monopoly Sailor Moon Collector's Edition",
        "category": "Anime & Manga",
        "year": 2018,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Le Royaume de la Lune, Tokyo Crystal, pions Sceptre lunaire, Broche de transformation, Masque Tuxedo."
    },
    {
        "id": "mono-manga-yugioh",
        "name": "Monopoly Yu-Gi-Oh!",
        "category": "Anime & Manga",
        "year": 2016,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Le Domaine des Duellistes, Bataille Ville, pions Puzzle du Millénium, Yeux du Millénium, Disque de duel."
    },
    {
        "id": "mono-manga-death-note",
        "name": "Monopoly Death Note",
        "category": "Anime & Manga",
        "year": 2019,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "La confrontation psychologique culte entre Light Yagami (Kira) et L, pions cahier Death Note, pomme de Ryuk."
    },
    {
        "id": "mono-manga-luckyluke",
        "name": "Monopoly Lucky Luke",
        "category": "Anime & Manga",
        "year": 2016,
        "country": "France / Belgique",
        "publisher": "Winning Moves",
        "description": "Le Far West de Lucky Luke, Jolly Jumper, Rantanplan et les quatre frères Dalton (Joe, William, Jack, Averell)."
    },

    # --- VILLES ET RÉGIONS DE FRANCE COMPLÉMENTAIRES ---
    {
        "id": "mono-ville-grenoble",
        "name": "Monopoly Grenoble",
        "category": "Villes & Régions (France)",
        "year": 2005,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "La Bastille et ses célèbres bulles téléphériques, Place Grenette, massif de Belledonne et Presqu'île."
    },
    {
        "id": "mono-ville-clermont",
        "name": "Monopoly Clermont-Ferrand",
        "category": "Villes & Régions (France)",
        "year": 2007,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Place de Jaude, Cathédrale Notre-Dame-de-l'Assomption en pierre de lave, Puy de Dôme et Michelin."
    },
    {
        "id": "mono-ville-reims",
        "name": "Monopoly Reims",
        "category": "Villes & Régions (France)",
        "year": 2008,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Cité des Sacres, Cathédrale Notre-Dame de Reims, prestigieuses maisons et caves de Champagne."
    },
    {
        "id": "mono-ville-dijon",
        "name": "Monopoly Dijon",
        "category": "Villes & Régions (France)",
        "year": 2006,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Palais des Ducs de Bourgogne, Tour Philippe le Bon, Rue des Forges, chouette de Notre-Dame et moutarde."
    },
    {
        "id": "mono-ville-toulon",
        "name": "Monopoly Toulon",
        "category": "Villes & Régions (France)",
        "year": 2007,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Rade de Toulon, Mont Faron, Stade Mayol (RCT), port militaire et plages du Mourillon."
    },
    {
        "id": "mono-ville-saint-etienne",
        "name": "Monopoly Saint-Étienne",
        "category": "Villes & Régions (France)",
        "year": 2006,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Stade Geoffroy-Guichard (Le Chaudron Vert), Musée d'Art et d'Industrie, Cité du Design et Puits Couriot."
    },
    {
        "id": "mono-region-savoie",
        "name": "Monopoly Savoie & Mont-Blanc",
        "category": "Villes & Régions (France)",
        "year": 2008,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Mont-Blanc, Lac d'Annecy, Chamonix, Val d'Isère, Courchevel, Chambéry et spécialités savoyardes."
    },
    {
        "id": "mono-region-vendee",
        "name": "Monopoly Vendée",
        "category": "Villes & Régions (France)",
        "year": 2005,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Puy du Fou, Les Sables-d'Olonne (Vendée Globe), Île d'Yeu, Noirmoutier et Marais Poitevin."
    },
    {
        "id": "mono-region-auvergne",
        "name": "Monopoly Auvergne",
        "category": "Villes & Régions (France)",
        "year": 2006,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Parc naturel des Volcans d'Auvergne, Vulcania, Lac Pavin, Mont-Dore, Saint-Nectaire et Cantal."
    },
    {
        "id": "mono-region-nord-pas-de-calais",
        "name": "Monopoly Nord-Pas-de-Calais",
        "category": "Villes & Régions (France)",
        "year": 2004,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Côte d'Opale, Cap Blanc-Nez, Beffrois, bassins miniers, Arras, Dunkerque et traditions ch'tis."
    },

    # --- VILLES ET PAYS DU MONDE COMPLÉMENTAIRES ---
    {
        "id": "mono-city-montreal",
        "name": "Monopoly Montréal",
        "category": "Villes & Pays (Monde)",
        "year": 2003,
        "country": "Canada",
        "publisher": "Hasbro",
        "description": "Vieux-Port, Mont-Royal, Basilique Notre-Dame, Sainte-Catherine, Place des Arts et poutine."
    },
    {
        "id": "mono-city-hongkong",
        "name": "Monopoly Hong Kong",
        "category": "Villes & Pays (Monde)",
        "year": 2007,
        "country": "Hong Kong / Asie",
        "publisher": "Hasbro",
        "description": "Victoria Peak, Star Ferry, Nathan Road, Temple Street, gratte-ciels spectaculaires et baie illuminée."
    },
    {
        "id": "mono-city-dubai",
        "name": "Monopoly Dubai",
        "category": "Villes & Pays (Monde)",
        "year": 2019,
        "country": "Émirats Arabes Unis",
        "publisher": "Winning Moves",
        "description": "Burj Khalifa, Burj Al Arab, Palm Jumeirah, Dubai Mall, Dubai Frame et souks de l'or."
    },
    {
        "id": "mono-city-madrid",
        "name": "Monopoly Madrid",
        "category": "Villes & Pays (Monde)",
        "year": 2004,
        "country": "Espagne",
        "publisher": "Hasbro",
        "description": "Puerta del Sol, Gran Vía, Plaza Mayor, Parc du Retiro, Musée du Prado et Palais Royal."
    },
    {
        "id": "mono-city-amsterdam",
        "name": "Monopoly Amsterdam",
        "category": "Villes & Pays (Monde)",
        "year": 2005,
        "country": "Pays-Bas",
        "publisher": "Hasbro",
        "description": "Canaux d'Amsterdam, Place du Dam, Rijksmuseum, Maison d'Anne Frank, Quartier des musées."
    },
    {
        "id": "mono-city-venise",
        "name": "Monopoly Venezia (Venise)",
        "category": "Villes & Pays (Monde)",
        "year": 2009,
        "country": "Italie",
        "publisher": "Winning Moves",
        "description": "Place Saint-Marc, Pont des Soupirs, Grand Canal, Pont du Rialto, Île de Murano et gondoles."
    },
    {
        "id": "mono-city-riodejaneiro",
        "name": "Monopoly Rio de Janeiro",
        "category": "Villes & Pays (Monde)",
        "year": 2007,
        "country": "Brésil",
        "publisher": "Estrela / Hasbro",
        "description": "Copacabana, Ipanema, Christ Rédempteur du Corcovado, Pain de Sucre et Sambodrome du Carnaval."
    },
    {
        "id": "mono-city-sanfrancisco",
        "name": "Monopoly San Francisco",
        "category": "Villes & Pays (Monde)",
        "year": 2002,
        "country": "USA",
        "publisher": "USAopoly",
        "description": "Golden Gate Bridge, Île d'Alcatraz, Fisherman's Wharf, Cable Cars, Lombard Street, Silicon Valley."
    },
    {
        "id": "mono-city-chicago",
        "name": "Monopoly Chicago",
        "category": "Villes & Pays (Monde)",
        "year": 2001,
        "country": "USA",
        "publisher": "USAopoly",
        "description": "Willis Tower (Sears Tower), Millennium Park (The Bean), Navy Pier, Magnificent Mile, Wrigley Field."
    }
]

# Load existing
with open("C:/Users/Admin/.gemini/antigravity/scratch/monopoly-collection-tracker/editions_seed.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

existing_ids = {e["id"] for e in existing}
for extra in extra_editions:
    if extra["id"] not in existing_ids:
        existing.append(extra)

# Sort alphabetically by name
existing.sort(key=lambda x: x["name"])

with open("C:/Users/Admin/.gemini/antigravity/scratch/monopoly-collection-tracker/editions_seed.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

print(f"Total editions now: {len(existing)}")
