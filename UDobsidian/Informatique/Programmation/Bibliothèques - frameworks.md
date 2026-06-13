---
tags:
  - bibliothèque/python
---
# Bibliothèques - frameworks


Voici les meilleures options de **bibliothèques / frameworks graphiques (GUI)** pour **Python 3** sous **Ubuntu** (y compris Ubuntu Pro) en 2026. Elles sont toutes très bien supportées sur Ubuntu, car c'est l'une des distributions les plus utilisées par les développeurs Python.

### Options les plus recommandées en 2026

|Rang|Bibliothèque|Installation sur Ubuntu|Look moderne ?|Niveau de difficulté|Points forts|Points faibles|Usage typique en 2026|
|---|---|---|---|---|---|---|---|
|1|**Tkinter** (+ CustomTkinter)|Déjà inclus avec Python 3 pip install customtkinter|Oui (avec CustomTkinter)|Très facile|Zéro installation complexe, très stable|Look basique sans CustomTkinter|Scripts rapides, outils internes, débutants|
|2|**PySide6** (Qt officiel gratuit)|sudo apt install python3-pyside6.qt* ou pip install PySide6|Excellent (natif)|Moyen|Très beau, très puissant, multi-plateforme, support commercial|Plus lourd que Tkinter|Applications professionnelles, outils complexes|
|3|**PyQt6**|pip install PyQt6|Excellent|Moyen|Presque identique à PySide6, très mature|Licence GPL ou commerciale (payante pour closed-source)|Même que PySide6, mais PySide6 préféré maintenant|
|4|**Dear PyGui**|pip install dearpygui|Très moderne (GPU)|Moyen-facile|Ultra rapide, look 2025+, immédiat rendering|Moins "natif" sur Linux|Dashboards, outils scientifiques, apps performantes|
|5|**Flet**|pip install flet|Très moderne (Flutter)|Très facile|Code Python → UI web ou desktop natif|Toujours un mini-serveur web en arrière-plan|Apps cross-platform (desktop + web + mobile)|
|6|**Kivy**|pip install kivy (ou via poetry/venv)|Moderne/tactile|Moyen|Très bon pour le multi-touch et mobile|Look pas natif sur desktop Linux|Applications mobiles, interfaces tactiles|

### Recommandations concrètes selon ton besoin

- **Tu débutes ou veux quelque chose de rapide et sans prise de tête** → **Tkinter + CustomTkinter** C’est la solution 80 % des cas en 2026 pour les outils perso / admin sys sous Ubuntu.
    
    Bash
    
    ```
    sudo apt update
    sudo apt install python3-tk python3-pip
    pip install customtkinter
    ``
    
- Exemple ultra-simple :
    
    Python
    
    ```
    import customtkinter as ctk
    
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app.title("Mon App Ubuntu")
    ctk.CTkLabel(app, text="Salut Mario !", font=("Arial", 24)).pack(pady=40)
    app.mainloop()
    ```
    
- **Tu veux une application qui a l'air pro et native** (comme un vrai logiciel Ubuntu) → **PySide6** (préféré à PyQt6 en 2026 car licence plus permissive)
    
    Bash
    
    ```
    sudo apt install python3-pyside6.qtcore python3-pyside6.qtwidgets python3-pyside6.qtgui
    # ou via pip : pip install PySide6
    ```
    
- **Tu veux le look le plus moderne possible avec le moins de code** → **Flet** (très populaire en 2025-2026)
    
    Bash
    
    ```
    pip install flet
    flet run ton_script.py   # → devient une app desktop ou web
    ```
    

### Verdict rapide pour la majorité des utilisateurs Ubuntu Pro en 2026

1. Commence par **CustomTkinter** → 10 minutes et tu as une belle fenêtre
2. Si tu as besoin de plus puissant / composants riches → passe à **PySide6**
3. Si tu veux coder comme du HTML/Flutter → essaie **Flet**

Tu peux me dire quel genre d’application tu veux faire (outil simple, dashboard, logiciel plus complexe, etc.) pour que je te donne un choix encore plus précis ? 😄


1. (Pillow est souvent utile pour les images dans CustomTkinter.)
    
2. **Pour des apps plus pros** (si CustomTkinter devient limité) :
    
    - Passe à **PySide6** (look natif Ubuntu, widgets riches) : pip install PySide6
    - Ou **Flet** (style Flutter, très rapide à prototyper) : pip install flet
    
    Mais CustomTkinter est parfait pour démarrer et faire de belles interfaces simples/modernes.
    

Si tu as une idée précise de ce que tu veux créer (outil admin, dashboard, convertisseur, jeu simple, etc.), dis-le-moi et je te donne un squelette de code adapté ! Ou si tu rencontres un nouveau petit bug, partage l'erreur ou le comportement.

Bravo encore, t'as persévéré et ça paye ! 🚀 Qu'est-ce que tu comptes faire en premier avec ton GUI qui marche ? 😊

