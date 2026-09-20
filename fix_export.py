# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Replace the entire exportToCsv function with a perfectly clean implementation
clean_export_func = """    function exportToCsv() {
      const headers = ["ID", "Statut", "Nom", "Categorie", "Annee", "Pays", "Editeur", "Image_URL", "Etat", "Prix_Achat_EUR", "Valeur_Estimee_EUR", "Emplacement", "Notes", "Description"];
      const rows = database.map(function(e) {
        return [
          '"' + (e.id || '').replace(/"/g, '""') + '"',
          '"' + (e.status === 'owned' ? 'Possédé' : e.status === 'wishlist' ? 'Recherché' : 'Non possédé').replace(/"/g, '""') + '"',
          '"' + (e.name || '').replace(/"/g, '""') + '"',
          '"' + (e.category || '').replace(/"/g, '""') + '"',
          '"' + (e.year || '') + '"',
          '"' + (e.country || '').replace(/"/g, '""') + '"',
          '"' + (e.publisher || '').replace(/"/g, '""') + '"',
          '"' + (e.image_url || '').replace(/"/g, '""') + '"',
          '"' + (e.condition || '').replace(/"/g, '""') + '"',
          '"' + (e.price || '') + '"',
          '"' + (e.value || '') + '"',
          '"' + (e.location || '').replace(/"/g, '""') + '"',
          '"' + (e.notes || '').replace(/"/g, '""') + '"',
          '"' + (e.description || '').replace(/"/g, '""') + '"'
        ];
      });

      const lineBreak = String.fromCharCode(10);
      const csvContent = "\\uFEFF" + headers.join(";") + lineBreak + rows.map(function(r) { return r.join(";"); }).join(lineBreak);
      const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "monopoly_collection_" + new Date().toISOString().slice(0,10) + ".csv";
      a.click();
      URL.revokeObjectURL(url);
      showToast("Fichier CSV exporté pour Excel !");
    }"""

# Use regex to replace from function exportToCsv() until showToast(...);\n    }
text = re.sub(r'function exportToCsv\(\)[\s\S]*?showToast\("Fichier CSV exporté pour Excel !"\);\s*\}', clean_export_func, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleanly replaced exportToCsv with String.fromCharCode(10) to avoid any newline escaping issue!")
