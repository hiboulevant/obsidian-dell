# Commandes Linux
#linux #command #xkill #htop 

https://kinsta.com/fr/blog/commandes-linux/

Tuez une application:

Comment fermer une application qui est en boucle sur linux mint 22?

Pour fermer une application qui est en boucle ou qui ne répond plus sous **Linux Mint 22** (basé sur Ubuntu 24.04), voici plusieurs méthodes :

---

### **1. Utiliser `xkill` (méthode graphique simple)**
- Ouvrez un terminal (`Ctrl + Alt + T`) et tapez :
  ```bash
  xkill
  ```
- Le curseur se transformera en **`✖`** : cliquez sur la fenêtre de l’application qui bugge pour la tuer.

---

### **2. Via le gestionnaire de tâches système**
- Appuyez sur **`Ctrl + Alt + Suppr`** (ou **`Ctrl + Esc`** si ça ne fonctionne pas).
- Sélectionnez **"Ouvrir le gestionnaire de tâches"** (ou installez `gnome-system-monitor` si absent).

---

### **3. Tuer le processus via le terminal**
#### **Avec `ps` et `kill`**
- Trouvez le nom du processus :
  ```bash
  ps aux | grep "nom_de_l_application"
  ```
  (Exemple : `ps aux | grep firefox`)

- Identifiez le **PID** (numéro de processus) et tuez-le :
  ```bash
  kill -9 PID
  ```
  (Remplacez `PID` par le numéro affiché.)

#### **Avec `pkill` (plus rapide)**
  ```bash
  pkill -9 nom_du_processus
  ```
  (Exemple : `pkill -9 chrome`)

#### **Avec `htop` (interactif)**
- Installez `htop` si nécessaire :
  ```bash
  sudo apt install htop
  ```
- Lancez-le :
  ```bash
  htop
  ```
- Trouvez le processus et tuez-le avec **`F9`** → **`SIGKILL`**.

---

### **4. Redémarrer le gestionnaire de fenêtres (si tout est bloqué)**
- Si l’interface ne répond plus, redémarrez **Cinnamon** (ou votre gestionnaire de fenêtres) :
  ```bash
  cinnamon --replace &
  ```
  (Remplacez `cinnamon` par `xfwm4` pour XFCE ou `mate-session` pour MATE.)

---

### **5. En dernier recours : redémarrer**
- Si rien ne fonctionne, forcez un redémarrage propre :
  ```bash
  reboot
  ```
  Ou en cas de blocage total : **`Alt + Impr Écran + REISUB`** (magic SysRq).

---

### **Cas spécifique : application en boucle infinie**
Si l’application consomme 100% CPU et ne répond pas, utilisez :
```bash
Killall -9 nom_du_processus
```
(Exemple : `killall -9 gimp`)

---

**Rappel** : `kill -9` (`SIGKILL`) force la fermeture, mais peut causer une perte de données. Utilisez d’abord un simple `kill PID` (`SIGTERM`).

[[Fedora 43 (commande)]]