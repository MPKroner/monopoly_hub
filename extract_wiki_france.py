import urllib.request, json, re

url = "https://en.wikipedia.org/w/api.php?action=parse&page=List_of_licensed_and_localized_editions_of_Monopoly:_Europe&prop=wikitext&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'MonopolyTracker/2.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        text = data.get('parse', {}).get('wikitext', {}).get('*', '')
        print("Total wikitext length:", len(text))
        
        # Find France section
        france_idx = text.find("== France ==")
        if france_idx == -1:
            france_idx = text.find("==France==")
        if france_idx != -1:
            france_text = text[france_idx:france_idx+15000]
            print("Found France section!")
            print(france_text[:2000])
            with open("scratch/wiki_france_section.txt", "w", encoding="utf-8") as f:
                f.write(france_text)
        else:
            print("France section not found by exact header")
except Exception as e:
    print("Error:", e)
