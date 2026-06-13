# Pandoc
Pour configurer le plugin Pandoc dans Obsidian, suivez ces étapes détaillées :
#Pandoc #obsidian #plugin 
---

### **1. Installer Pandoc sur votre système**
- **Windows/macOS/Linux** : Téléchargez depuis [pandoc.org](https://pandoc.org/installing.html).
  - *Vérification* : Ouvrez un terminal et tapez `pandoc --version`. Si une erreur s'affiche, vérifiez le chemin d'installation.

---

### **2. Activer le plugin Pandoc dans Obsidian**
1. Ouvrez Obsidian.
2. Allez dans **Paramètres** > **Plugins communautaires** (désactivez "Mode sans échec" si nécessaire).
3. Cherchez "Pandoc", installez-le et activez-le.

---

### **3. Configurer le plugin Pandoc**
1. Dans les paramètres d'Obsidian, allez à la section **Pandoc**.
2. **Chemin de Pandoc** :
   - *Windows* : `C:\Program Files\Pandoc\pandoc.exe` (par défaut).
   - *macOS/Linux* : `/usr/local/bin/pandoc` (vérifiez avec `which pandoc` en terminal).
3. **Arguments personnalisés** (optionnel) : Ajoutez des flags comme `--pdf-engine=xelatex` pour les PDF.

---

### **4. Exporter un fichier avec Pandoc**
1. Ouvrez une note dans Obsidian.
2. Utilisez `Ctrl+P` (ou `Cmd+P` sur macOS) pour ouvrir la palette de commandes.
3. Tapez **"Export with Pandoc"** et sélectionnez le format (PDF, DOCX, HTML, etc.).

---

### **Problèmes courants & solutions**
- **Erreur "Pandoc not found"** :
  - Vérifiez le chemin dans les paramètres du plugin.
  - Ajoutez Pandoc au **PATH** de votre système ([guide pour Windows](https://www.computerhope.com/issues/ch000549.htm), [macOS/Linux](https://opensource.com/article/17/6/set-path-linux)).

- **Échec de conversion PDF** :
  - Installez LaTeX (ex. [MiKTeX](https://miktex.org/) pour Windows, [MacTeX](https://www.tug.org/mactex/) pour macOS).

- **Logs de débogage** :
  - Activez les logs dans les paramètres du plugin Pandoc et vérifiez les erreurs.

---

### **Exemple de configuration avancée**
Pour générer un PDF avec une police spécifique :
```yaml
Arguments Pandoc :
--pdf-engine=xelatex
-V mainfont="Arial"
```

---

Si le problème persiste, décrivez précisément l'erreur et votre OS, je peux vous aider davantage ! 🛠️
