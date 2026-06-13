# Link Alias
&alias #link/alias #obsidian

Voici un exemple concret d'utilisation de **Link Alias** dans Obsidian pour gérer un PDF externe sans alourdir votre coffre :

### Fichier : `Rapport Financier Q3.md`
```markdown
---
alias: Rapport Financier Q3
---

# Rapport Trimestriel

Ceci est une note référençant un PDF externe stocké sur Google Drive.

## 📁 Document complet
Lien vers le PDF : [Version complète]({{gdrive:rapport-financier-q3-2023.pdf}})

## 🔑 Points clés
- Revenus : +15% vs Q2
- Dépenses R&D : 1.2M€
- Projections :  [[Prévisions 2024]]
```

---

### Configuration requise :
1. **Plugin "Link Alias"** installé (via `Paramètres > Plugins communautaires`)
2. **Fichier de configuration** `.obsidian/link-alias.json` :
```json
{
  "aliases": {
    "gdrive": "https://drive.google.com/file/d/VOTRE_ID_GOOGLE_DRIVE/view?usp=sharing/"
  }
}
```

---

### Fonctionnement :
1. **Dans la note** :  
   `[Version complète]({{gdrive:rapport-financier-q3-2023.pdf}})`  
   → Devient un clic vers :  
   `https://drive.google.com/.../view?usp=sharing&resourcekey=...`

2. **Avantages** :
   - Le PDF **reste externe** (pas de synchro via Obsidian Sync)
   - Mise à jour centralisée : Modifiez l'URL dans `link-alias.json` pour mettre à jour tous les liens
   - Syntaxe propre : `{{gdrive:nom-fichier.pdf}}` au lieu d'URLs longues

---

### Alternative avec lien direct (sans alias) :
```markdown
[📥 Télécharger](https://drive.google.com/file/d/ABC123xyz/view)
```
→ Mais moins lisible et difficile à maintenir si l'URL change.

---

### Cas d'usage avancé :
Pour plusieurs clouds, ajoutez des alias multiples dans `link-alias.json` :
```json
{
  "aliases": {
    "gdrive": "https://drive.google.com/.../",
    "dropbox": "https://www.dropbox.com/s/.../",
    "notion": "https://notion.so/..."
  }
}
```
Puis utilisez dans vos notes :  
`{{dropbox:contrat-client.pdf}}` ou `{{notion:roadmap-projet}}`
---
alias: Rapport Financier Q3
---

# Rapport Trimestriel

Ceci est une note référençant un PDF externe stocké sur Google Drive.

## 📁 Document complet
Lien vers le PDF : [Version complète]({{gdrive:rapport-financier-q3-2023.pdf}})

## 🔑 Points clés
- Revenus : +15% vs Q2
- Dépenses R&D : 1.2M€
- Projections : [[Prévisions 2024]]