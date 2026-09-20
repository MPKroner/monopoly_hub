# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the broken unescaped newline in exportToCsv
broken_snippet = 'headers.join(";") + "\n'
fixed_snippet = 'headers.join(";") + "\\n'
text = text.replace(broken_snippet, fixed_snippet)

broken_snippet2 = '.join(";")) + "\n'
fixed_snippet2 = '.join(";")) + "\\n'
text = text.replace(broken_snippet2, fixed_snippet2)

broken_snippet3 = '.join(";")).join("\n'
fixed_snippet3 = '.join(";")).join("\\n'
text = text.replace(broken_snippet3, fixed_snippet3)

# Also ensure all .join("\n") are .join("\\n")
text = text.replace('join(";\")).join("', 'join(";")).join("\\n"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed newline in index.html!")
