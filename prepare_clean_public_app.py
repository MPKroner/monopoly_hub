import json
import re
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(base_dir, "index.html")

print("Reading index.html...")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Extract SEED_DATA
match = re.search(r'const SEED_DATA = (\[[\s\S]*?\]);\s*const STORAGE_KEY', html)
if not match:
    print("Error: Could not find SEED_DATA in index.html")
    exit(1)

seed_json_str = match.group(1)
seed_data = json.loads(seed_json_str)
print(f"Total items in SEED_DATA: {len(seed_data)}")

# 1. Create personal user backup
# All 1225 items with user's 11 owned items preserved
user_backup_path = os.path.join(base_dir, "monopoly_sauvegarde_perso.json")
with open(user_backup_path, "w", encoding="utf-8") as f:
    json.dump(seed_data, f, ensure_ascii=False, indent=2)
print(f"Saved personal user backup to: {user_backup_path}")

# Check owned items in backup
owned_items = [item for item in seed_data if item.get("status") == "owned"]
print(f"Owned items in personal backup: {len(owned_items)}")
for it in owned_items:
    print(f" - {it.get('name')} ({it.get('year')}) : {it.get('value')} €")

# 2. Create clean virgin SEED_DATA for public GitHub
clean_seed = []
for item in seed_data:
    clean_item = dict(item)
    clean_item["status"] = "none"
    clean_item["condition"] = ""
    clean_item["price"] = ""
    clean_item["value"] = ""
    clean_item["location"] = ""
    if "user_image" in clean_item:
        del clean_item["user_image"]
    if "user_photos" in clean_item:
        del clean_item["user_photos"]
    # If notes were personal, clean them
    if clean_item.get("notes") and ("Réf" in clean_item["notes"] or "Ajouté" in clean_item["notes"]):
        clean_item["notes"] = ""
    clean_seed.append(clean_item)

clean_seed_json_str = json.dumps(clean_seed, ensure_ascii=False)

# Replace in index.html:
# Bump STORAGE_KEY to v10 so any new visitor starts completely fresh
new_html = html[:match.start(1)] + clean_seed_json_str + html[match.end(1):]
new_html = re.sub(r'const STORAGE_KEY = "[^"]+";', 'const STORAGE_KEY = "monopoly_collection_db_v10";', new_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("index.html updated successfully with clean virgin database (0 owned) and STORAGE_KEY v10!")
