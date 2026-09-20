import urllib.request, urllib.parse, json, time

url = "https://monopoly.fandom.com/api.php?action=query&generator=allpages&gaplimit=100&prop=pageimages|categories&pithumbsize=600&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    pages = data.get('query', {}).get('pages', {})
    print(f"Sample 100 pages retrieved: {len(pages)}")
    with_img = [p for p in pages.values() if 'thumbnail' in p]
    print(f"Pages with box image: {len(with_img)} ({len(with_img)*100//len(pages)}%)")
