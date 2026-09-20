# -*- coding: utf-8 -*-
import json

with open("editions_seed.json", "r", encoding="utf-8") as f:
    seed_data = json.load(f)

json_str = json.dumps(seed_data, ensure_ascii=False)

with open("build_real_covers_app.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace the onerror with simple handleImageError(this)
code = code.replace(
    r"""onerror="handleImageError(this, \'' + item.id + '\')\"""",
    r"""onerror="handleImageError(this)""""
)
code = code.replace(
    r"""onerror="handleImageError(this, \'""" + r"""' + item.id + \'""" + r"""')\"""",
    r"""onerror="handleImageError(this)""""
)
code = code.replace(
    """onerror="this.src=\\'data:image/svg+xml;utf8,<svg xmlns=\\\\'http://www.w3.org/2000/svg\\\\' width=\\\\'50\\\\' height=\\\\'35\\\\'><rect width=\\\\'50\\\\' height=\\\\'35\\\\' fill=\\\\'%23334155\\\\'/><text x=\\\\'25\\\\' y=\\\\'22\\\\' fill=\\\\'white\\\\' font-size=\\\\'10\\\\' text-anchor=\\\\'middle\\\\'>📦</text></svg>\\';\"""",
    """onerror="handleThumbError(this)\""""
)

with open("build_real_covers_app.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_real_covers_app.py")
