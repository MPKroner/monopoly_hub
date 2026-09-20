# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(r'onerror="handleImageError\(this[^"]*\)"', 'onerror="handleImageError(this)"', text)
text = re.sub(r'onerror="this\.src=[^"]*"', 'onerror="handleImageError(this)"', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed index.html!')
