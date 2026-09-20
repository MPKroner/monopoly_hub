import urllib.request, xml.etree.ElementTree as ET

url = "https://boardgamegeek.com/xmlapi2/thing?id=1406&versions=1"
req = urllib.request.Request(url, headers={'User-Agent': 'MonopolyCollector/1.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read()
        root = ET.fromstring(content)
        versions = root.findall(".//item[@type='boardgameversion']")
        print(f"BGG returned {len(versions)} versions for Monopoly!")
        for v in versions[:10]:
            name = v.find(".//name[@type='primary']")
            year = v.find(".//yearpublished")
            thumb = v.find(".//thumbnail")
            print(" -", name.get('value') if name is not None else 'Unknown', 
                  f"({year.get('value') if year is not None else '?'})",
                  "Thumb:", thumb.text if thumb is not None else 'No')
except Exception as e:
    print("BGG error:", e)
