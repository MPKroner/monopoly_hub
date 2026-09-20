import urllib.request, re

url = "https://monopolymania.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=5) as resp:
    html = resp.read().decode('utf-8', errors='ignore')
    # find all links
    links = re.findall(r'href="([^"]+)"', html)
    ed_links = [l for l in links if 'monopolymania.com/' in l or l.startswith('/') or 'page' in l or 'categorie' in l]
    print("Links found:", len(set(ed_links)))
    for l in sorted(list(set(ed_links)))[:40]:
        print(" -", l)
