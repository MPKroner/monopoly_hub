# -*- coding: utf-8 -*-
import json

editions = [
    # --- CLASSIQUES & HISTORIQUES & ANNIVERSAIRES ---
    {
        "id": "mono-1935",
        "name": "Monopoly Édition Originale 1935 (Reproduction)",
        "category": "Classique & Anniversaire",
        "year": 1935,
        "country": "USA / Monde",
        "publisher": "Parker Brothers / Hasbro",
        "description": "Reproduction de la boîte originale Parker Brothers de 1935 avec les pions en métal rétro et billets vintage."
    },
    {
        "id": "mono-fr-1937",
        "name": "Monopoly France Édition Originale 1937",
        "category": "Classique & Anniversaire",
        "year": 1937,
        "country": "France",
        "publisher": "Miro Company",
        "description": "Première édition française par Miro Company avec les rues parisiennes historiques (Rue de la Paix, Belleville)."
    },
    {
        "id": "mono-fr-standard",
        "name": "Monopoly Classique Standard (Rues de Paris)",
        "category": "Classique & Anniversaire",
        "year": 2008,
        "country": "France",
        "publisher": "Hasbro",
        "description": "L'édition de référence avec le plateau français moderne (Belleville à Rue de la Paix) et pions modernes."
    },
    {
        "id": "mono-deluxe-1995",
        "name": "Monopoly Deluxe Edition",
        "category": "Classique & Anniversaire",
        "year": 1995,
        "country": "Monde",
        "publisher": "Parker Brothers",
        "description": "Boîte dorée avec plateau feutrine, socles en bois pour maisons et hôtels, billets dorés et carrousel à billets."
    },
    {
        "id": "mono-50th",
        "name": "Monopoly 50ème Anniversaire (1935-1985)",
        "category": "Classique & Anniversaire",
        "year": 1985,
        "country": "Monde",
        "publisher": "Parker Brothers",
        "description": "Édition commémorative spéciale 50 ans avec boîte argentée ou dorée et pions en métal collector."
    },
    {
        "id": "mono-60th",
        "name": "Monopoly 60ème Anniversaire (1935-1995)",
        "category": "Classique & Anniversaire",
        "year": 1995,
        "country": "Monde",
        "publisher": "Parker Brothers",
        "description": "Boîte en métal embossé commémorative avec pions dorés spéciaux."
    },
    {
        "id": "mono-70th",
        "name": "Monopoly 70ème Anniversaire",
        "category": "Classique & Anniversaire",
        "year": 2005,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Boîte en fer blanc argenté avec cartes argentées et pions chromés."
    },
    {
        "id": "mono-80th",
        "name": "Monopoly 80ème Anniversaire (1935-2015)",
        "category": "Classique & Anniversaire",
        "year": 2015,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Comprend 8 pions vintage emblématiques représentant chacun une décennie (années 30 à 2000)."
    },
    {
        "id": "mono-85th",
        "name": "Monopoly 85ème Anniversaire",
        "category": "Classique & Anniversaire",
        "year": 2020,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Édition de luxe festive avec finitions brillantes et pions spéciaux célébrant 85 ans de Monopoly."
    },
    {
        "id": "mono-franklin-mint",
        "name": "Monopoly The Franklin Mint Collector's Edition",
        "category": "Classique & Anniversaire",
        "year": 1991,
        "country": "USA / Monde",
        "publisher": "Franklin Mint",
        "description": "Plateau en bois noble surélevé, tiroir feutre vert, hôtels plaqués or 24 carats, maisons en argent massif."
    },
    {
        "id": "mono-vintage-wood",
        "name": "Monopoly Vintage Book Collection (Boîte Livre Bois)",
        "category": "Classique & Anniversaire",
        "year": 2005,
        "country": "USA / International",
        "publisher": "Winning Solutions",
        "description": "Boîtier en bois simulant un livre ancien de collection, plateau pliable et composants rétro."
    },
    {
        "id": "mono-nostalgia-tin",
        "name": "Monopoly Nostalgia Tin Edition",
        "category": "Classique & Anniversaire",
        "year": 2001,
        "country": "Monde",
        "publisher": "Hasbro / Parker Brothers",
        "description": "Boîte métallique collector avec graphismes et illustrations rétro des années 1930/1950."
    },
    {
        "id": "mono-rustic",
        "name": "Monopoly Rustic Wood Series",
        "category": "Classique & Anniversaire",
        "year": 2018,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Plateau et boîte en bois rustique vieilli, idéal pour décoration et jeu chaleureux."
    },

    # --- VARIANTES & TWISTS DE GAMEPLAY ---
    {
        "id": "mono-mega",
        "name": "The Mega Edition Monopoly",
        "category": "Variantes & Règles Spéciales",
        "year": 2006,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "Plateau étendu avec 12 cases supplémentaires, gratte-ciels, dépôts de train et dé de rapidité (Speed Die)."
    },
    {
        "id": "mono-cheaters",
        "name": "Monopoly Édition Tricheurs (Cheaters Edition)",
        "category": "Variantes & Règles Spéciales",
        "year": 2018,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Trichez pour gagner sans vous faire attraper ! Menottes en plastique incluses pour les tricheurs découverts."
    },
    {
        "id": "mono-crooked",
        "name": "Monopoly Faux Billets (Crooked Cash)",
        "category": "Variantes & Règles Spéciales",
        "year": 2021,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Utilisez le décodeur de Mr. Monopoly pour démasquer les faux billets et les fausses cartes Chance."
    },
    {
        "id": "mono-electronic-bank",
        "name": "Monopoly Banque Électronique (Electronic Banking)",
        "category": "Variantes & Règles Spéciales",
        "year": 2006,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Remplacement des billets par une unité bancaire électronique et des cartes de crédit pour chaque joueur."
    },
    {
        "id": "mono-ultimate-bank",
        "name": "Monopoly Banque Électronique Ultime (Ultimate Banking)",
        "category": "Variantes & Règles Spéciales",
        "year": 2016,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Lecteur sans contact tap-to-pay instantané : scanne les cartes de propriété et cartes bancaires automatiquement."
    },
    {
        "id": "mono-voice-banking",
        "name": "Monopoly Voice Banking (Banque Vocale)",
        "category": "Variantes & Règles Spéciales",
        "year": 2019,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Le chapeau haut-de-forme électronique interactif gère toutes les transactions bancaires par commande vocale."
    },
    {
        "id": "mono-longest-game",
        "name": "Monopoly Longest Game Ever",
        "category": "Variantes & Règles Spéciales",
        "year": 2019,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Plateau géant de 66 propriétés, un seul dé, la partie ne s'arrête que quand quelqu'un possède TOUTES les propriétés."
    },
    {
        "id": "mono-speed",
        "name": "Monopoly Speed (En moins de 10 minutes)",
        "category": "Variantes & Règles Spéciales",
        "year": 2019,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Chaque joueur joue en même temps avec son propre dé et chronomètre, partie pliée en 10 minutes."
    },
    {
        "id": "mono-revolution",
        "name": "Monopoly Révolution (Plateau Rond)",
        "category": "Variantes & Règles Spéciales",
        "year": 2010,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Plateau de jeu circulaire unique avec unité sonore centrale diffusant musique et effets sonores."
    },
    {
        "id": "mono-empire",
        "name": "Monopoly Empire",
        "category": "Variantes & Règles Spéciales",
        "year": 2013,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Achetez de grandes marques mondiales (Coca-Cola, Xbox, McDonald's) et empilez leurs panneaux dans votre gratte-ciel."
    },
    {
        "id": "mono-millennials",
        "name": "Monopoly for Millennials",
        "category": "Variantes & Règles Spéciales",
        "year": 2018,
        "country": "USA / Monde",
        "publisher": "Hasbro",
        "description": "'Oubliez l'immobilier, vous n'avez pas les moyens de toute façon' : accumulez des points d'expérience (brunch, canapé...)."
    },
    {
        "id": "mono-socialism",
        "name": "Monopoly Socialism",
        "category": "Variantes & Règles Spéciales",
        "year": 2019,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Édition parodique où les joueurs collaborent pour un fonds commun, souvent avec des effets chaotiques."
    },
    {
        "id": "mono-pizza",
        "name": "Monopoly Pizza",
        "category": "Variantes & Règles Spéciales",
        "year": 2018,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Boîte en forme de boîte à pizza avec pions tranche de pizza, collectez les meilleures garnitures de pizza."
    },
    {
        "id": "mono-bad-losers",
        "name": "Monopoly Mauvais Perdants (Sore Losers)",
        "category": "Variantes & Règles Spéciales",
        "year": 2020,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Payer le loyer ou aller en prison vous donne des pièces Mauvais Perdant pour réclamer le pion géant Mr. Monopoly !"
    },
    {
        "id": "mono-super-mario-celebration",
        "name": "Monopoly Super Mario Celebration",
        "category": "Jeux Vidéo",
        "year": 2020,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Bloc « ? » sonore avec bruitages classiques de Nintendo qui change les règles du jeu."
    },
    {
        "id": "mono-deal-card",
        "name": "Monopoly Deal (Jeu de Cartes)",
        "category": "Variantes & Règles Spéciales",
        "year": 2008,
        "country": "France / Monde",
        "publisher": "Hasbro",
        "description": "Format jeu de cartes rapide (15 min) extrêmement populaire, volez des propriétés et complétez 3 groupes."
    },

    # --- VILLES & RÉGIONS (FRANCE & FRANCOPHONIE) ---
    {
        "id": "mono-ville-paris",
        "name": "Monopoly Paris (Monuments)",
        "category": "Villes & Régions (France)",
        "year": 2000,
        "country": "France",
        "publisher": "Winning Moves / Hasbro",
        "description": "Achetez la Tour Eiffel, le Musée du Louvre, Notre-Dame, Montmartre et les Champs-Élysées."
    },
    {
        "id": "mono-ville-lyon",
        "name": "Monopoly Lyon",
        "category": "Villes & Régions (France)",
        "year": 2002,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Les hauts lieux lyonnais : Place Bellecour, Basilique de Fourvière, Parc de la Tête d'Or, Vieux Lyon."
    },
    {
        "id": "mono-ville-marseille",
        "name": "Monopoly Marseille",
        "category": "Villes & Régions (France)",
        "year": 2001,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Vieux-Port, Basilique Notre-Dame de la Garde, Stade Vélodrome, les Calanques et la Canebière."
    },
    {
        "id": "mono-ville-bordeaux",
        "name": "Monopoly Bordeaux",
        "category": "Villes & Régions (France)",
        "year": 2004,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Place de la Bourse, Grand Théâtre, Rue Sainte-Catherine, Miroir d'eau et vignobles bordelais."
    },
    {
        "id": "mono-ville-lille",
        "name": "Monopoly Lille",
        "category": "Villes & Régions (France)",
        "year": 2003,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Grand'Place, Vieille Bourse, Citadelle Vauban, Palais des Beaux-Arts et Braderie de Lille."
    },
    {
        "id": "mono-ville-nantes",
        "name": "Monopoly Nantes",
        "category": "Villes & Régions (France)",
        "year": 2004,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Château des ducs de Bretagne, Machines de l'Île, Passage Pommeraye, Tour Bretagne."
    },
    {
        "id": "mono-ville-strasbourg",
        "name": "Monopoly Strasbourg",
        "category": "Villes & Régions (France)",
        "year": 2003,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Cathédrale Notre-Dame, Petite France, Parlement Européen et Marché de Noël."
    },
    {
        "id": "mono-ville-toulouse",
        "name": "Monopoly Toulouse",
        "category": "Villes & Régions (France)",
        "year": 2003,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Place du Capitole, Basilique Saint-Sernin, Cité de l'Espace, Pont-Neuf et berges de la Garonne."
    },
    {
        "id": "mono-ville-nice",
        "name": "Monopoly Nice",
        "category": "Villes & Régions (France)",
        "year": 2002,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Promenade des Anglais, Vieux-Nice, Colline du Château, Place Masséna et Baie des Anges."
    },
    {
        "id": "mono-ville-montpellier",
        "name": "Monopoly Montpellier",
        "category": "Villes & Régions (France)",
        "year": 2004,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Place de la Comédie, Promenade du Peyrou, Quartier Antigone et Faculté de Médecine."
    },
    {
        "id": "mono-ville-rennes",
        "name": "Monopoly Rennes",
        "category": "Villes & Régions (France)",
        "year": 2004,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Parlement de Bretagne, Place Sainte-Anne, Parc du Thabor et Portes Mordelaises."
    },
    {
        "id": "mono-region-bretagne",
        "name": "Monopoly Bretagne",
        "category": "Villes & Régions (France)",
        "year": 2002,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Saint-Malo, Brest, Golfe du Morbihan, Carnac, Forêt de Brocéliande et Côte de Granit Rose."
    },
    {
        "id": "mono-region-normandie",
        "name": "Monopoly Normandie",
        "category": "Villes & Régions (France)",
        "year": 2005,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Mont-Saint-Michel, Falaises d'Étretat, Plages du Débarquement, Honfleur, Rouen et Deauville."
    },
    {
        "id": "mono-region-alsace",
        "name": "Monopoly Alsace",
        "category": "Villes & Régions (France)",
        "year": 2003,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Château du Haut-Kœnigsbourg, Route des Vins, Colmar, Riquewihr et maisons à colombages."
    },
    {
        "id": "mono-region-corse",
        "name": "Monopoly Corse",
        "category": "Villes & Régions (France)",
        "year": 2004,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Falaises de Bonifacio, Calanques de Piana, Ajaccio, Bastia, Île Rousse et plages sauvages."
    },
    {
        "id": "mono-region-pays-basque",
        "name": "Monopoly Pays Basque",
        "category": "Villes & Régions (France)",
        "year": 2006,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Biarritz, Saint-Jean-de-Luz, Bayonne, Espelette, la Rhune et les traditions basques."
    },
    {
        "id": "mono-dom-reunion",
        "name": "Monopoly La Réunion",
        "category": "Villes & Régions (France)",
        "year": 2005,
        "country": "France (Outre-mer)",
        "publisher": "Winning Moves",
        "description": "Piton de la Fournaise, Cirque de Mafate, Cilaos, Saint-Denis et plages de Saint-Gilles."
    },
    {
        "id": "mono-dom-antilles",
        "name": "Monopoly Guadeloupe / Martinique (Antilles)",
        "category": "Villes & Régions (France)",
        "year": 2006,
        "country": "France (Outre-mer)",
        "publisher": "Winning Moves",
        "description": "La Soufrière, Montagne Pelée, Pointe-à-Pitre, Fort-de-France et les plages de cartes postales."
    },
    {
        "id": "mono-be-bruxelles",
        "name": "Monopoly Bruxelles",
        "category": "Villes & Régions (France)",
        "year": 2001,
        "country": "Belgique",
        "publisher": "Winning Moves",
        "description": "Grand-Place de Bruxelles, Atomium, Manneken-Pis, Sablon et Palais Royal."
    },
    {
        "id": "mono-be-national",
        "name": "Monopoly Belgique (Édition Nationale)",
        "category": "Villes & Régions (France)",
        "year": 2000,
        "country": "Belgique",
        "publisher": "Hasbro",
        "description": "Édition bilingue français / néerlandais avec les grandes villes belges (Bruges, Gand, Liège, Anvers)."
    },
    {
        "id": "mono-ch-national",
        "name": "Monopoly Suisse",
        "category": "Villes & Régions (France)",
        "year": 2001,
        "country": "Suisse",
        "publisher": "Hasbro",
        "description": "Édition quadrilingue avec Genève, Zurich, Bâle, Lausanne, Berne et le Cervin."
    },
    {
        "id": "mono-ch-geneve",
        "name": "Monopoly Genève",
        "category": "Villes & Régions (France)",
        "year": 2008,
        "country": "Suisse",
        "publisher": "Winning Moves",
        "description": "Jet d'eau de Genève, Horloge fleurie, Palais des Nations, Vieille-Ville et Lac Léman."
    },

    # --- VILLES & MONDE (INTERNATIONAL) ---
    {
        "id": "mono-world-edition",
        "name": "Monopoly Here & Now: World Edition",
        "category": "Villes & Pays (Monde)",
        "year": 2008,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Les plus grandes villes du monde élues par des millions d'internautes (Montréal, Paris, Londres, Tokyo)."
    },
    {
        "id": "mono-city-london",
        "name": "Monopoly London (Classic UK)",
        "category": "Villes & Pays (Monde)",
        "year": 1936,
        "country": "Royaume-Uni",
        "publisher": "Waddingtons / Hasbro",
        "description": "Le légendaire plateau britannique d'origine : Mayfair, Park Lane, Piccadilly, Trafalgar Square."
    },
    {
        "id": "mono-city-newyork",
        "name": "Monopoly New York City",
        "category": "Villes & Pays (Monde)",
        "year": 1995,
        "country": "USA",
        "publisher": "USAopoly",
        "description": "Times Square, Central Park, Empire State Building, Statue de la Liberté, Wall Street."
    },
    {
        "id": "mono-city-tokyo",
        "name": "Monopoly Tokyo",
        "category": "Villes & Pays (Monde)",
        "year": 2006,
        "country": "Japon",
        "publisher": "Hasbro / Takara Tomy",
        "description": "Shibuya, Shinjuku, Ginza, Tour de Tokyo, Akihabara et Roppongi."
    },
    {
        "id": "mono-city-lasvegas",
        "name": "Monopoly Las Vegas",
        "category": "Villes & Pays (Monde)",
        "year": 1997,
        "country": "USA",
        "publisher": "USAopoly",
        "description": "Le Strip de Las Vegas, Bellagio, Caesars Palace, Fremont Street et les plus célèbres casinos."
    },
    {
        "id": "mono-city-rome",
        "name": "Monopoly Roma",
        "category": "Villes & Pays (Monde)",
        "year": 2012,
        "country": "Italie",
        "publisher": "Winning Moves",
        "description": "Colisée, Fontaine de Trevi, Panthéon, Place Navone et Forum Romain."
    },
    {
        "id": "mono-city-berlin",
        "name": "Monopoly Berlin",
        "category": "Villes & Pays (Monde)",
        "year": 2005,
        "country": "Allemagne",
        "publisher": "Winning Moves",
        "description": "Porte de Brandebourg, Alexanderplatz, Mur de Berlin, Kurfürstendamm et Potsdamer Platz."
    },
    {
        "id": "mono-city-sydney",
        "name": "Monopoly Sydney",
        "category": "Villes & Pays (Monde)",
        "year": 2004,
        "country": "Australie",
        "publisher": "Winning Moves",
        "description": "Opéra de Sydney, Harbour Bridge, Bondi Beach, The Rocks et Darling Harbour."
    },

    # --- FILMS & SÉRIES TÉLÉVISÉES ---
    {
        "id": "mono-pop-starwars-classic",
        "name": "Monopoly Star Wars Édition Collector (1997)",
        "category": "Films & Séries",
        "year": 1997,
        "country": "Monde / France",
        "publisher": "Parker Brothers / Hasbro",
        "description": "Pions étain des héros originaux (Luke, Vador, Han, Leïa, Chewbacca, R2-D2), crédits impériaux et républicains."
    },
    {
        "id": "mono-pop-starwars-mandalorian",
        "name": "Monopoly Star Wars The Mandalorian",
        "category": "Films & Séries",
        "year": 2020,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Incarnez Din Djarin, Greef Karga, Cara Dune ou IG-11 et protégez l'Enfant (Grogu / Bébé Yoda)."
    },
    {
        "id": "mono-pop-harrypotter",
        "name": "Monopoly Harry Potter",
        "category": "Films & Séries",
        "year": 2024,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Rejoignez Poudlard, prenez le Poudlard Express, explorez Pré-au-Lard et gagnez des points de maison."
    },
    {
        "id": "mono-pop-lotr",
        "name": "Monopoly Le Seigneur des Anneaux (The Lord of the Rings)",
        "category": "Films & Séries",
        "year": 2003,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Inclut l'Anneau Unique avec pion doré spécial, la Terre du Milieu, Mordor, la Comté et Fondcombe."
    },
    {
        "id": "mono-pop-got",
        "name": "Monopoly Game of Thrones (Le Trône de Fer)",
        "category": "Films & Séries",
        "year": 2015,
        "country": "Monde / France",
        "publisher": "Hasbro / HBO",
        "description": "Musique du générique intégrée dans le Trône sonore, maisons de Westeros (Stark, Lannister, Targaryen)."
    },
    {
        "id": "mono-pop-marvel-avengers",
        "name": "Monopoly Marvel Avengers",
        "category": "Films & Séries",
        "year": 2019,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Recrutez des héros Marvel au lieu d'acheter des rues pour sauver l'univers de Thanos."
    },
    {
        "id": "mono-pop-stranger-things",
        "name": "Monopoly Stranger Things",
        "category": "Films & Séries",
        "year": 2017,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Hawkins dans les années 80 et l'Upside Down (Monde à l'envers) avec pions bicyclette, talkie-walkie, gaufre."
    },
    {
        "id": "mono-pop-friends",
        "name": "Monopoly Friends (Série TV)",
        "category": "Films & Séries",
        "year": 2018,
        "country": "Monde / France",
        "publisher": "Winning Moves",
        "description": "Pions emblématiques (la guitare de Phoebe, la pizza de Joey, la tasse de café, le dinosaure de Ross)."
    },
    {
        "id": "mono-pop-the-simpsons",
        "name": "Monopoly Les Simpson (The Simpsons)",
        "category": "Films & Séries",
        "year": 2001,
        "country": "Monde / France",
        "publisher": "USAopoly / Hasbro",
        "description": "Springfield, la centrale nucléaire de M. Burns, le bar de Moe, la maison des Simpson et pions spéciaux."
    },
    {
        "id": "mono-pop-disney-classics",
        "name": "Monopoly Disney Classics",
        "category": "Films & Séries",
        "year": 2002,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Tous les grands classiques Disney de Blanche-Neige au Roi Lion avec pions sculptés dorés des héros féeriques."
    },
    {
        "id": "mono-pop-disney-villains",
        "name": "Monopoly Disney Villains (Les Méchants)",
        "category": "Films & Séries",
        "year": 2020,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Incarnez Maléfique, Ursula, Scar, Jafar, Capitaine Crochet ou Cruella d'Enfer avec leurs cartes Pouvoir."
    },
    {
        "id": "mono-pop-jurassic-park",
        "name": "Monopoly Jurassic Park",
        "category": "Films & Séries",
        "year": 2021,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Comprend la porte du parc avec bruitage électronique culte du T-Rex et le thème musical officiel."
    },
    {
        "id": "mono-pop-back-to-the-future",
        "name": "Monopoly Retour vers le Futur (Back to the Future)",
        "category": "Films & Séries",
        "year": 2015,
        "country": "Monde / France",
        "publisher": "Winning Moves",
        "description": "Hill Valley à travers 1885, 1955, 1985 et 2015 avec pions DeLorean, Hoverboard, casquette de Marty."
    },
    {
        "id": "mono-pop-batman",
        "name": "Monopoly Batman Collector's Edition",
        "category": "Films & Séries",
        "year": 2005,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Gotham City, l'Asile d'Arkham, Wayne Enterprises et la Batcave avec pions Batmobile et Bat-Signal."
    },
    {
        "id": "mono-pop-spiderman",
        "name": "Monopoly Spider-Man",
        "category": "Films & Séries",
        "year": 2014,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Capturez les super-vilains de New York (Bouffon Vert, Venom, Docteur Octopus, Electro)."
    },
    {
        "id": "mono-pop-the-walking-dead",
        "name": "Monopoly The Walking Dead (Survival Edition)",
        "category": "Films & Séries",
        "year": 2013,
        "country": "Monde / USA",
        "publisher": "USAopoly",
        "description": "Achetez, vendez et fortifiez des lieux sécurisés contre les Rôdeurs (prison, Woodbury, Hershel's Farm)."
    },
    {
        "id": "mono-pop-ghostbusters",
        "name": "Monopoly SOS Fantômes (Ghostbusters)",
        "category": "Films & Séries",
        "year": 2016,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Pions Ecto-1, Piège à fantôme, Bibendum Chamallow, Pack de protons et caserne des pompiers."
    },
    {
        "id": "mono-pop-doctor-who",
        "name": "Monopoly Doctor Who (50th Anniversary)",
        "category": "Films & Séries",
        "year": 2013,
        "country": "Royaume-Uni / Monde",
        "publisher": "Winning Moves",
        "description": "Voyagez à travers l'espace et le temps avec le TARDIS, le Tournevis sonique, les Daleks et les Cybermen."
    },
    {
        "id": "mono-pop-rick-and-morty",
        "name": "Monopoly Rick and Morty",
        "category": "Films & Séries",
        "year": 2016,
        "country": "Monde / France",
        "publisher": "USAopoly / Winning Moves",
        "description": "Explorez le Multivers, la Dimension C-137, Gazorpazorp avec pions Portal Gun, Plumbus et boîte de Meeseeks."
    },
    {
        "id": "mono-pop-the-office",
        "name": "Monopoly The Office (Dunder Mifflin)",
        "category": "Films & Séries",
        "year": 2019,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Dunder Mifflin Scranton : agrafeuse dans la gelée, le trophée Dundie, tasse World's Best Boss."
    },

    # --- JEUX VIDÉO ---
    {
        "id": "mono-vg-pokemon-kanto",
        "name": "Monopoly Pokémon Kanto Edition",
        "category": "Jeux Vidéo",
        "year": 2014,
        "country": "Monde / France",
        "publisher": "USAopoly / Winning Moves",
        "description": "Capturez les arènes et les Pokémon des 8 badges de la région Kanto avec pions Pikachu, Évoli, Salamèche..."
    },
    {
        "id": "mono-vg-pokemon-johto",
        "name": "Monopoly Pokémon Johto Edition",
        "category": "Jeux Vidéo",
        "year": 2016,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Explorez Bourg Geon, Doublonville et capturez Germignon, Héricendre, Kaiminus, Togepi."
    },
    {
        "id": "mono-vg-zelda",
        "name": "Monopoly The Legend of Zelda",
        "category": "Jeux Vidéo",
        "year": 2014,
        "country": "Monde / France",
        "publisher": "USAopoly / Winning Moves",
        "description": "Hyrule, le Temple du Temps, Mont du Péril, château d'Hyrule avec pions Triforce, Bouclier Hylien, Arc."
    },
    {
        "id": "mono-vg-nintendo-collector",
        "name": "Monopoly Nintendo Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2006,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Réunit les grandes licences Nintendo : Mario, Donkey Kong, Link, Samus Aran, Fox McCloud, Kirby."
    },
    {
        "id": "mono-vg-fortnite",
        "name": "Monopoly Fortnite",
        "category": "Jeux Vidéo",
        "year": 2018,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Pas d'argent classique : chaque joueur a des points de vie (PV/HP). Évitez la tempête et soyez le dernier survivant."
    },
    {
        "id": "mono-vg-minecraft",
        "name": "Monopoly Minecraft",
        "category": "Jeux Vidéo",
        "year": 2021,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Monde cubique : minez des ressources (bois, pierre, fer, diamant) et construisez vos abris."
    },
    {
        "id": "mono-vg-fallout",
        "name": "Monopoly Fallout Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2015,
        "country": "Monde / France",
        "publisher": "USAopoly",
        "description": "Terres désolées du Wasteland : payez en capsules Nuka-Cola, pions Vault Boy, casque Power Armor, Mini Nuke."
    },
    {
        "id": "mono-vg-sonic",
        "name": "Monopoly Sonic the Hedgehog Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2013,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Green Hill Zone, Chemical Plant, collectez les anneaux d'or et les émeraudes du Chaos avec Sonic et Tails."
    },
    {
        "id": "mono-vg-assassins-creed",
        "name": "Monopoly Assassin's Creed",
        "category": "Jeux Vidéo",
        "year": 2014,
        "country": "Monde / France",
        "publisher": "Winning Moves",
        "description": "Incarnez Altaïr, Ezio, Connor, Edward Kenway, Arno Dorian dans les villes historiques de la confrérie."
    },
    {
        "id": "mono-vg-skyrim",
        "name": "Monopoly The Elder Scrolls V: Skyrim",
        "category": "Jeux Vidéo",
        "year": 2017,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "Bordeciel, Blancherive, Solitude, Vendeaume, pions Casque de fer de Dovahkiin, bouclier d'azur."
    },
    {
        "id": "mono-vg-world-of-warcraft",
        "name": "Monopoly World of Warcraft Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2012,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Azeroth, Hurlevent, Orgrimmar, Fossoyeuse, pions Heaume de domination, Botte de chenille, Épée de Varian."
    },
    {
        "id": "mono-vg-animal-crossing",
        "name": "Monopoly Animal Crossing New Horizons",
        "category": "Jeux Vidéo",
        "year": 2021,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Explorez des îles, attrapez des insectes et des poissons, vendez-les contre des Nook Miles pour gagner !"
    },
    {
        "id": "mono-vg-pacman",
        "name": "Monopoly Arcade Pac-Man",
        "category": "Jeux Vidéo",
        "year": 2020,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Mini borne d'arcade Pac-Man rétro interactive incluse pour jouer et enregistrer ses scores."
    },
    {
        "id": "mono-vg-overwatch",
        "name": "Monopoly Overwatch Collector's Edition",
        "category": "Jeux Vidéo",
        "year": 2019,
        "country": "Monde",
        "publisher": "Hasbro",
        "description": "Rassemblez une équipe de 6 héros parmi D.Va, Lúcio, Tracer, Faucheur, Winston et Hanzo."
    },

    # --- ANIME, MANGA & BD ---
    {
        "id": "mono-manga-dbz",
        "name": "Monopoly Dragon Ball Z",
        "category": "Anime & Manga",
        "year": 2018,
        "country": "Monde / France",
        "publisher": "USAopoly / Winning Moves",
        "description": "Recrutez des guerriers Z (Goku, Vegeta, Piccolo, Gohan) et affrontez Freezer, Cell et Buu avec 7 Dragon Balls."
    },
    {
        "id": "mono-manga-db-super",
        "name": "Monopoly Dragon Ball Super",
        "category": "Anime & Manga",
        "year": 2019,
        "country": "Monde / France",
        "publisher": "Winning Moves",
        "description": "Tournoi du Pouvoir, Dieux de la Destruction, Beerus, Whis, Goku Ultra Instinct et Jiren."
    },
    {
        "id": "mono-manga-one-piece",
        "name": "Monopoly One Piece",
        "category": "Anime & Manga",
        "year": 2018,
        "country": "Monde / France",
        "publisher": "Winning Moves",
        "description": "L'Équipage du Chapeau de Paille à Dressrosa, pions Chapeau de Luffy, sabre de Zoro, Thousand Sunny."
    },
    {
        "id": "mono-manga-naruto",
        "name": "Monopoly Naruto Shippuden",
        "category": "Anime & Manga",
        "year": 2020,
        "country": "Monde / France",
        "publisher": "USAopoly / Winning Moves",
        "description": "Village de Konoha, Akatsuki, pions Kunaï, bandeau frontal ninja, nuage de l'Akatsuki, bol de ramen d'Ichiraku."
    },
    {
        "id": "mono-manga-aot",
        "name": "Monopoly L'Attaque des Titans (Attack on Titan)",
        "category": "Anime & Manga",
        "year": 2016,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Murs Maria, Rose et Sina, bataillon d'exploration, pions équipement tridimensionnel, clé d'Eren, canon."
    },
    {
        "id": "mono-manga-mha",
        "name": "Monopoly My Hero Academia",
        "category": "Anime & Manga",
        "year": 2019,
        "country": "Monde / France",
        "publisher": "USAopoly / Winning Moves",
        "description": "Lycée Yuei (U.A. High), recrues de la classe 1-A (Deku, Bakugo, Todoroki) et pions Alter."
    },
    {
        "id": "mono-manga-asterix",
        "name": "Monopoly Astérix et Obélix",
        "category": "Anime & Manga",
        "year": 2019,
        "country": "France / Europe",
        "publisher": "Winning Moves",
        "description": "Le Village Gaulois qui résiste à l'envahisseur, menhirs, sangliers, camp de Babaorum et potion magique."
    },
    {
        "id": "mono-manga-tintin",
        "name": "Monopoly Les Aventures de Tintin",
        "category": "Anime & Manga",
        "year": 2007,
        "country": "Belgique / France",
        "publisher": "Winning Moves / Moulinsart",
        "description": "Château de Moulinsart, la fusée lunaire, le Crabe aux pinces d'or, pions Milou, Capitaine Haddock, Tintin."
    },

    # --- MUSIQUE & GROUPES DE LÉGENDE ---
    {
        "id": "mono-music-beatles",
        "name": "Monopoly The Beatles Collector's Edition",
        "category": "Musique & Groupes",
        "year": 2008,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Abbey Road, Sgt. Pepper's, Yellow Submarine, Strawberry Fields avec pions sous-marin jaune, morse, marteau."
    },
    {
        "id": "mono-music-queen",
        "name": "Monopoly Queen Edition",
        "category": "Musique & Groupes",
        "year": 2017,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "Conçu avec Brian May : revivez les tournées mythiques du groupe Queen (Wembley, Hyde Park, Rio)."
    },
    {
        "id": "mono-music-acdc",
        "name": "Monopoly AC/DC Collector's Edition",
        "category": "Musique & Groupes",
        "year": 2011,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Back in Black, Highway to Hell, For Those About to Rock, pions cloche d'enfer, casquette d'Angus, canon."
    },
    {
        "id": "mono-music-metallica",
        "name": "Monopoly Metallica Collector's Edition",
        "category": "Musique & Groupes",
        "year": 2011,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Master of Puppets, Ride the Lightning, Black Album avec pions serpent de Don't Tread on Me, marteau de Kill 'Em All."
    },
    {
        "id": "mono-music-rolling-stones",
        "name": "Monopoly The Rolling Stones Collector's Edition",
        "category": "Musique & Groupes",
        "year": 2010,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Sticky Fingers, Exile on Main St., célèbre logo à la langue rouge et lèvres de Mick Jagger."
    },
    {
        "id": "mono-music-kiss",
        "name": "Monopoly KISS Collector's Edition",
        "category": "Musique & Groupes",
        "year": 2006,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "The Demon, The Starchild, The Spaceman, The Catman avec leurs albums légendaires et concerts pyrotechniques."
    },
    {
        "id": "mono-music-bowie",
        "name": "Monopoly David Bowie",
        "category": "Musique & Groupes",
        "year": 2021,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "Ziggy Stardust, Aladdin Sane, Heroes, Blackstar, pions éclair emblématique, cravate, chapeau de feutre."
    },
    {
        "id": "mono-music-iron-maiden",
        "name": "Monopoly Iron Maiden: Somewhere on Tour",
        "category": "Musique & Groupes",
        "year": 2023,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Voyagez avec la mascotte Eddie à travers l'histoire d'Iron Maiden (The Number of the Beast, Powerslave)."
    },

    # --- MARQUES & SPORTS ---
    {
        "id": "mono-brand-ferrari",
        "name": "Monopoly Ferrari Collector's Edition",
        "category": "Marques & Sports",
        "year": 2006,
        "country": "Monde",
        "publisher": "Winning Moves",
        "description": "Achetez les modèles mythiques de Maranello (250 GTO, F40, Enzo, Formule 1 de Michael Schumacher)."
    },
    {
        "id": "mono-brand-harley",
        "name": "Monopoly Harley-Davidson Collector's Edition",
        "category": "Marques & Sports",
        "year": 1999,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Motos légendaires (Fat Boy, Electra Glide, Sportster) et pions casque de biker, moteur V-Twin, botte en cuir."
    },
    {
        "id": "mono-brand-cocacola",
        "name": "Monopoly Coca-Cola Collector's Edition",
        "category": "Marques & Sports",
        "year": 1999,
        "country": "Monde",
        "publisher": "USAopoly",
        "description": "Bouteille galbée contour historique, camion de Noël, ours polaire Coca-Cola et distributeur vintage."
    },
    {
        "id": "mono-brand-nasa",
        "name": "Monopoly NASA (Space Exploration)",
        "category": "Marques & Sports",
        "year": 2020,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Missions Apollo, navette spatiale, télescope Hubble, rover martien Curiosity et Station Spatiale Internationale."
    },
    {
        "id": "mono-sport-fifa-world-cup",
        "name": "Monopoly Coupe du Monde FIFA (World Cup)",
        "category": "Marques & Sports",
        "year": 2006,
        "country": "Monde / France",
        "publisher": "Hasbro",
        "description": "Les plus grandes nations du football mondial, stades légendaires et pion Trophée de la Coupe du Monde."
    },
    {
        "id": "mono-sport-tour-de-france",
        "name": "Monopoly Tour de France",
        "category": "Marques & Sports",
        "year": 2017,
        "country": "France / Europe",
        "publisher": "Winning Moves",
        "description": "Les cols mythiques (Alpe d'Huez, Tourmalet, Mont Ventoux) et l'arrivée mythique sur les Champs-Élysées."
    },
    {
        "id": "mono-sport-roland-garros",
        "name": "Monopoly Roland-Garros",
        "category": "Marques & Sports",
        "year": 2015,
        "country": "France",
        "publisher": "Winning Moves",
        "description": "Courts Philippe-Chatrier, Suzanne-Lenglen, terre battue parisienne, pions raquette, chaise d'arbitre, trophée."
    },
    {
        "id": "mono-sport-nba",
        "name": "Monopoly NBA",
        "category": "Marques & Sports",
        "year": 1999,
        "country": "USA / Monde",
        "publisher": "USAopoly",
        "description": "Franchises légendaires (Lakers, Celtics, Bulls, Warriors) avec pion panier de basket et ballon spalding."
    }
]

with open("C:/Users/Admin/.gemini/antigravity/scratch/monopoly-collection-tracker/editions_seed.json", "w", encoding="utf-8") as f:
    json.dump(editions, f, ensure_ascii=False, indent=2)

print(f"Seed dataset created with {len(editions)} editions.")
