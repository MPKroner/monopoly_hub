import urllib.request, json

wiki_titles = [
    "List of licensed and localized editions of Monopoly: USA",
    "List of licensed and localized editions of Monopoly: UK",
    "List of licensed and localized editions of Monopoly: Europe",
    "List of licensed and localized editions of Monopoly: France",
    "List of licensed and localized editions of Monopoly: Canada",
    "List of licensed and localized editions of Monopoly: Asia"
]

for title in wiki_titles:
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'MonopolyCollector/1.0 (test@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, page in pages.items():
                if int(pid) > 0:
                    print(f"Found on Wikipedia: {page['title']}")
                else:
                    print(f"Not found: {title}")
    except Exception as e:
        print(f"Error {title}: {e}")
