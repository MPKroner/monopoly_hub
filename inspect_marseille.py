import urllib.request
import re

url = 'https://www.winningmoves.fr/nos-jeux/monopoly-marseille/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')
    imgs = re.findall(r'https://www\.winningmoves\.fr/wp-content/uploads/[^"\'\s>]+\.(?:png|jpg|jpeg)', html)
    print(f'Found {len(imgs)} images on Marseille page:')
    for img in sorted(set(imgs)):
        if 'Logo' not in img:
            print('-->', img)
