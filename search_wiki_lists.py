import urllib.request, json

url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=List+of+licensed+and+localized+editions+of+Monopoly&limit=10&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'MonopolyCollector/1.0'})
with urllib.request.urlopen(req, timeout=5) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("Wikipedia related lists:", data[1])
