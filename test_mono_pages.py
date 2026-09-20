import urllib.request, re

for page in [1, 5, 10, 15, 20, 25, 30, 40]:
    url = f"https://monopolymania.com/?page={page}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'<a href="https://monopolymania\.com/([^"]+)"><img src="(/public/[^"]+)" alt="" />([^<]+)</a>', html)
            print(f"Page {page}: {len(matches)} items")
            if matches:
                print("   Sample:", matches[0][2])
    except Exception as e:
        print(f"Page {page}: {e}")
