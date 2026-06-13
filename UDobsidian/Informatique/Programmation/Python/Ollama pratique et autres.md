---
tags:
  - ollama
  - python
---
# Ollama pratique et autres

Ollama run phi 3
>>> Qui est le président de la chine?
Le président actuel de la République populaire de Chine est Xi Jinping, qui a pris ses fonctions en mars 2013 et y est resté avec des rénitifications successives depuis lors. En tant 
Que chef suprême du Parti communiste chinois (PCC) et d'État, le président joue un rôle important dans la politique nationale de l'autorité majeure au sein du système 
Multi-partislementaire en Chine.

>>> Quel modèle me sera le plus utile pour apprendre le language python?
Pour apprendre efficacement le langage Python, je vous recommande d'utiliser la série de livres "Python for Everybody: Exploring Data This book by Jean Siffoff et Andrew Peppler est 
Particulièrement adaptée aux débutants. Elle couvre les fondamentaux tout en fournissant des exemples pratiques pertinents au domaine spécifique que vous pourriez travailler, comme le 
Développement web avec Django ou l'analyse de données avec Pandas. En outre, la plateforme Codecademy offre également une expérience interactive qui peut être particulièrement utile si 
Votre style d'apprentissage est visuel et pratique. Pour enrichir davantage vos compétences, vous pourriez suivre des cours sur Coursera ou edX liés à Python et assister aux séquences 
Accompagnées de tutoriels vidéo qui expliquent les concepts avec précision tout en offrant du contenu pratique. Enfin, participer à des projets GitHub fournit une bonne application 
Concrète où vous pouvez appliquer vos compétences et relever des défis réels pour améliorer votre maîtrise de Python au fil du temps.

### Les différents modèles
Voici un tableau qui résume les deux principales façons d'obtenir du contenu graphique avec Ollama :

|Approche|Ce que ça fait|Comment ça marche|Exemples concrets|
|---|---|---|---|
|**👀 Lire des images**|Le modèle **analyse et décrit** des images que tu fournis.|Il faut utiliser un **modèle "multimodal"** (vision-langage) qui comprend à la fois le texte et les images.|Décrire une photo, extraire du texte d'un document scanné, répondre à des questions sur un schéma.|
|**🎨 Générer des images**|Le modèle **crée** une nouvelle image à partir d'une description textuelle.|Ollama ne le fait pas nativement, mais on peut le combiner avec d'autres outils comme **OllamaDiffuser** ou des projets qui utilisent Ollama comme "cerveau" pour améliorer les invites.|Créer une image de "chat astronaut" à partir de cette phrase.|

### 👀 Faire "Lire" des Images à Ollama (Multimodal)

C'est la fonctionnalité la plus intégrée à Ollama aujourd'hui. Depuis la version 0.7.0, Ollama supporte nativement les modèles multimodaux, aussi appelés modèles de vision [](https://github.com/ollama/ollama/releases/tag/v0.7.0)[](https://packagehub.suse.com/update-infos/openSUSE-2025-181/)[](https://registry.ollama.ai/blog/multimodal-models). Cela signifie que tu peux montrer une image à un modèle et lui poser des questions dessus.

**Comment faire ?**

1. **Choisir un modèle multimodal.** Les plus connus et récents sont :
    
    - **Llama 4 Scout** : `llama4:scout` (très performant) [](https://registry.ollama.ai/blog/multimodal-models)
        
    - **Gemma 3** : `gemma3` (excellent pour comparer des images) [](https://registry.ollama.ai/blog/multimodal-models)
        
    - **Qwen 2.5 VL** : `qwen2.5vl` (idéal pour lire du texte dans des images, comme des documents) [](https://packagehub.suse.com/update-infos/openSUSE-2025-181/)[](https://registry.ollama.ai/blog/multimodal-models)
        
2. **Télécharger le modèle** (si ce n'est pas déjà fait) :
    
    bash
    
    ollama pull gemma3
    
3. **Lancer le modèle en lui fournissant une image**. Il suffit de donner le chemin d'accès à ton image dans l'invite de commande.
    
    bash
    
    ollama run gemma3
    >>> Chemin/vers/ton/image.jpg Décris-moi cette image ?
    
    Le modèle va alors "regarder" l'image et te répondre [](https://registry.ollama.ai/blog/multimodal-models).
    
    _Exemple tiré de la documentation officielle :_
    
    bash
    
    ollama@ordinateur ~ % ollama run gemma3
    >>> /Users/ollama/Images/chat.jpg /Users/ollama/Images/chien.jpg Quelle est la différence entre ces deux animaux ?
    
    Le modèle analysera les deux photos et pourra te répondre en comparant le chat et le chien [](https://registry.ollama.ai/blog/multimodal-models).
    

### 🎨 Générer des Images "Via" Ollama

Ollama, en tant que tel, ne crée pas d'images. Pour cela, il faut utiliser des outils spécialisés dans la génération d'images (comme **Stable Diffusion** ou **FLUX.1**). Cependant, Ollama peut jouer un rôle clé dans le processus créatif.

Voici comment ces deux approches se complètent :

- **Option 1 : Utiliser un outil comme OllamaDiffuser**  
    Ce projet est **exactement ce que tu cherches** : il propose une interface en ligne de commande (CLI) similaire à celle d'Ollama, mais dédiée à la génération d'images. Tu peux "pull" et "run" des modèles comme `flux.1-schnell` ou `stable-diffusion-1.5` [](https://pypi.org/project/ollamadiffuser/1.1.5/).
    
    bash
    
    # Installation
    pip install ollamadiffuser
    # Télécharger un modèle de génération d'images
    ollamadiffuser pull flux.1-schnell
    # Démarrer le serveur de génération
    ollamadiffuser run flux.1-schnell
    # (Dans un autre terminal) Générer une image via l'API
    curl -X POST http://localhost:8000/api/generate \
      -H "Content-Type: application/json" \
      -d '{"prompt": "un magnifique coucher de soleil sur la mer"}' \
      --output coucher-de-soleil.png
    
    OllamaDiffuser propose même une interface web et gère des contrôles avancés [](https://pypi.org/project/ollamadiffuser/1.1.5/).
    
- **Option 2 : Utiliser Ollama comme "Prompt Engineer" expert**  
    Cette approche est très élégante. Au lieu de chercher toi-même la description parfaite pour générer une image, tu donnes une idée simple à un modèle Ollama (comme `llama3.2`), et il va générer une description extrêmement détaillée et professionnelle. Cette description est ensuite envoyée à un générateur d'images comme Stable Diffusion [](https://github.com/ImdataScientistSachin/Local-Multimodal-Image-Generation-with-Ollama-Stable-Diffusion).
    
    - **Exemple** : Tu dis "un chat", Ollama génère la phrase : *"Chat majestueux aux yeux dorés, éclairage cinématographique, rayons de soleil traversant un rideau, style photographie professionnelle 8k, bokeh en arrière-plan..."*.
        
    - Cela permet d'obtenir des résultats de bien meilleure qualité sans être un expert des "prompts" [](https://github.com/ImdataScientistSachin/Local-Multimodal-Image-Generation-with-Ollama-Stable-Diffusion).
        

### 🤔 Par où commencer ?

Puisque tu es déjà familier avec la commande `ollama run`, je te conseille de commencer par explorer les **modèles multimodaux** (vision). C'est le plus simple :

1. Installe un modèle comme `gemma3` ou `qwen2.5vl`.
    
2. Prépare une image sur ton disque dur.
    
3. Lance la commande `ollama run gemma3` et fais glisser ton image dans le terminal (ou tape son chemin) suivi de ta question.
    

Tu verras, c'est très impressionnant de voir le modèle "comprendre" le contenu d'une photo ! Une fois que tu auras maîtrisé cela, tu pourras t'attaquer à la génération d'images avec OllamaDiffuser.

N'hésite pas si tu as des questions sur l'une de ces méthodes !