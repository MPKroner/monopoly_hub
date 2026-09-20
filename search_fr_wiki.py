import urllib.request, json

titles = [
    "Monopoly",
    "Liste des éditions du Monopoly",
    "Liste des éditions de Monopoly en France",
    "Liste des éditions régionales du Monopoly en France"
]

for t in titles:
    url = f"https://fr.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(t)}&limit=5&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'MonopolyTracker/2.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"FR Wiki search '{t}':", data[1])
    except Exception as e:
        print("Error:", e)
