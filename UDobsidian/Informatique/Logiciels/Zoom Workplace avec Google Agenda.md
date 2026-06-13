# Zoom Workplace avec Google Agenda

Voici comment procéder pour synchroniser le **Calendrier Zoom Workplace** avec **Google Agenda**.

---
#zoom/Workplace #zoom/agenda #visioconférence


### La Méthode Principale : L'Intégration Native via l'Admin Console

La bonne nouvelle est que Zoom Workplace propose une intégration native avec Google Workspace. Cette configuration se fait principalement par un administrateur Zoom ou Google Workspace.

#### Étape 1 : L'Administrateur doit configurer l'intégration

Un administrateur de votre domaine Zoom Workplace doit lier le compte à Google Workspace. Voici les grandes lignes de ce qu'il doit faire :

1.  **Se connecter au portail d'administration Zoom** (`admin.zoom.us`).
2.  Aller dans **Gestion des espaces de travail (Workspace Management)** > **Calendrier et contacts**.
3.  Cliquer sur **Ajouter un service de calendrier** et choisir **Google Workspace**.
4.  Suivre le processus d'authentification et d'autorisation qui permettra à Zoom d'accéder aux services calendrier de Google pour votre organisation.
5.  **Configurer les autorisations et la portée** : L'admin peut choisir quels utilisateurs ou groupes auront leur calendrier synchronisé.

#### Étape 2 : Configuration de Votre Compte Utilisateur

Une fois l'intégration activée au niveau administratif, vous, en tant qu'utilisateur, pouvez configurer votre client Zoom pour votre usage.

1.  **Ouvrez l'application de bureau Zoom** sur votre Windows 11.
2.  Allez dans **Paramètres** (icône d'engrenage) > **Calendrier et Contacts**.
3.  Vous devriez voir **Google Workspace** listé comme un service connecté.
4.  **Cochez les calendriers Google** que vous souhaitez synchroniser avec votre client Zoom (par exemple, "Mon Agenda" ou d'autres agendas partagés).
5.  Assurez-vous que l'option **Synchroniser mes réunions Zoom avec le service de calendrier** est activée.

---

### Ce que cette intégration permet de faire :

*   **Visualisation Bidirectionnelle** : Vous verrez vos événements Google Agenda dans l'onglet "Calendrier" de l'app Zoom et vos réunions Zoom planifiées dans Google Agenda.
*   **Création de réunions Zoom depuis Google Agenda** : Pour cela, vous devez installer l'**extension de navigateur "Zoom for Google Calendar"**. Cela ajoute un bouton "Make it a Zoom Meeting" directement dans l'interface de création d'événement de Google Agenda.
*   **Éviter les doublons** : La synchronisation des disponibilités permet de voir quand vous êtes occupé dans les deux systèmes, évitant ainsi les conflits de rendez-vous.

---

### Solution de Secours : L'Abonnement iCal (Si l'intégration native n'est pas activée)

Si votre administrateur n'a pas activé l'intégration Google Workspace, vous pouvez utiliser une méthode de visualisation simple pour voir votre Google Agenda dans Zoom.

1.  **Récupérez l'URL iCal de Google Agenda** :
    *   Ouvrez **Google Agenda** sur le web.
    *   Allez dans les paramètres de l'agenda que vous voulez voir (cliquez sur le nom de l'agenda dans la liste à gauche).
    *   Cherchez la section **URL secret de l'agenda** (ou "Adresse de l'agenda en iCal").
    *   **Copiez l'URL** fournie.

2.  **Ajoutez-la dans Zoom** :
    *   Dans l'app Zoom, allez dans **Paramètres** > **Calendrier et Contacts**.
    *   Cliquez sur **Ajouter un calendrier** > **URL iCal (abonnement)**.
    *   Collez l'URL que vous avez copiée et donnez-lui un nom.

**Limite de cette méthode** : Elle est en **lecture seule**. Vous verrez vos événements Google dans Zoom, mais vous ne pourrez pas les modifier ou créer de réunions Zoom depuis ces événements.

---

### Résumé et Actions à Entreprendre

| Action | Responsable | Résultat |
| :--- | :--- | :--- |
| **1. Activer l'intégration Google Workspace** | **Administrateur Zoom/Google** | Permet une synchronisation profonde et bidirectionnelle pour tous les utilisateurs. |
| **2. Configurer son client Zoom** | **Vous (Utilisateur)** | Choisir quels agendas synchroniser et activer les options. |
| **3. Installer l'extension de navigateur** | **Vous (Utilisateur)** | Pouvoir créer des réunions Zoom directement depuis Google Agenda. |

**Votre prochaine étape :**
**Contactez votre administrateur IT ou Zoom Workplace** et demandez-lui si l'intégration avec Google Workspace (Google Calendar) est activée et configurée pour votre organisation. C'est la condition sine qua non pour une synchronisation fluide et complète.

S'ils ne peuvent pas l'activer, utilisez la méthode de l'abonnement iCal comme solution de visualisation simple.