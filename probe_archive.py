import urllib.request, re

url = 'https://monopolymania.com/archive'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        links = re.findall(r'href="https://monopolymania\.com/([^"]+)"', html)
        print('Links on /archive:', len(links))
        print('Sample 20:', sorted(list(set(links)))[:20])
except Exception as e:
    print('Error:', e)
