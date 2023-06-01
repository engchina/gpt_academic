> **Note**
>
> Ce fichier README est généré automatiquement par le plugin de traduction markdown de ce projet et n'est peut - être pas correct à 100%.
>
<<<<<<< HEAD

# <img src="logo.png" width="40" > ChatGPT Optimisation Académique

**Si vous aimez ce projet, donnez-lui une étoile; si vous avez inventé des raccourcis académiques plus utiles ou des plugins fonctionnels, n'hésitez pas à ouvrir une demande ou une demande de traction. Nous avons également un fichier README en [anglais|](docs/README_EN.md)[japonais|](docs/README_JP.md)[russe|](docs/README_RS.md)[français](docs/README_FR.md) traduit par ce projet lui-même.**

> **Note**
>
> 1. Veuillez noter que seuls les plugins de fonction signalés en **rouge** sont capables de lire les fichiers, certains plugins se trouvent dans le **menu déroulant** de la section plugin. Nous sommes également les bienvenus avec la plus haute priorité pour traiter et accepter tout nouveau PR de plugin!
>
> 2. Chaque fichier dans ce projet est expliqué en détail dans l'auto-analyse [self_analysis.md](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A). Avec l'itération des versions, vous pouvez également cliquer sur les plugins fonctionnels pertinents pour appeler GPT et générer un rapport d'auto-analyse projet mis à jour. Les questions fréquemment posées sont résumées dans le [wiki](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98).
> 

<div align="center">

Fonctionnalité | Description
--- | ---
Polissage en un clic | Prend en charge la correction en un clic et la recherche d'erreurs de syntaxe dans les documents de recherche.
Traduction Chinois-Anglais en un clic | Une touche pour traduire la partie chinoise en anglais ou celle anglaise en chinois.
Explication de code en un clic | Affiche et explique correctement le code.
[Raccourcis clavier personnalisables](https://www.bilibili.com/video/BV14s4y1E7jN) | Prend en charge les raccourcis clavier personnalisables.
[Configuration du serveur proxy](https://www.bilibili.com/video/BV1rc411W7Dr) | Prend en charge la configuration du serveur proxy.
Conception modulaire | Prend en charge la personnalisation des plugins de fonctions et des [plugins] de fonctions hiérarchiques personnalisés, et les plugins prennent en charge [la mise à jour à chaud](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97).
[Auto-analyse du programme](https://www.bilibili.com/video/BV1cj411A7VW) | [Plugins] [Lire en un clic](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A) le code source de ce projet.
[Analyse de programme](https://www.bilibili.com/video/BV1cj411A7VW) | [Plugins] En un clic, les projets Python/C/C++/Java/Lua/... peuvent être analysés.
Lire le document de recherche | [Plugins] Lisez le résumé de l'article en latex et générer un résumé.
Traduction et polissage de l'article complet en LaTeX | [Plugins] Une touche pour traduire ou corriger en LaTeX
Génération Commentaire de fonction en vrac | [Plugins] Lisez en un clic les fonctions et générez des commentaires de fonction.
Rapport d'analyse automatique des chats générés | [Plugins] Génère un rapport de synthèse après l'exécution.
[Assistant arxiv](https://www.bilibili.com/video/BV1LM4y1279X) | [Plugins] Entrez l'url de l'article arxiv pour traduire le résumé + télécharger le PDF en un clic
[Traduction complète des articles PDF](https://www.bilibili.com/video/BV1KT411x7Wn) | [Plugins] Extraire le titre et le résumé de l'article PDF + Traduire le texte entier (multithread)
[Aide à la recherche Google Academ](https://www.bilibili.com/video/BV19L411U7ia) | [Plugins] Donnez à GPT l'URL de n'importe quelle page de recherche Google Academ pour vous aider à sélectionner des articles intéressants
Affichage de formules/images/tableaux | Afficher la forme traduite et rendue d'une formule en même temps, plusieurs formules et surlignage du code prend en charge
Prise en charge des plugins multithread | Prise en charge de l'appel multithread de chatgpt, traitement en masse de texte ou de programmes en un clic
Activer le thème Gradio sombre [theme](https://github.com/binary-husky/chatgpt_academic/issues/173) au démarrage | Ajoutez ```/?__dark-theme=true``` à l'URL du navigateur pour basculer vers le thème sombre
[Prise en charge de plusieurs modèles LLM](https://www.bilibili.com/video/BV1wT411p7yf), [prise en charge de l'interface API2D](https://api2d.com/) | Comment cela serait-il de se faire servir par GPT3.5, GPT4 et la [ChatGLM de Tsinghua](https://github.com/THUDM/ChatGLM-6B) en même temps?
Expérience en ligne d'huggingface sans science | Après vous être connecté à huggingface, copiez [cet espace](https://huggingface.co/spaces/qingxu98/gpt-academic)
... | ...
=======
> During installation, please strictly select the versions **specified** in requirements.txt. 
>
> `pip install -r requirements.txt`
>

# <img src="logo.png" width="40" > Optimisation académique GPT (GPT Academic)

**Si vous aimez ce projet, veuillez lui donner une étoile. Si vous avez trouvé des raccourcis académiques ou des plugins fonctionnels plus utiles, n'hésitez pas à ouvrir une demande ou une pull request. 
Pour traduire ce projet dans une langue arbitraire avec GPT, lisez et exécutez [`multi_language.py`](multi_language.py) (expérimental).

> **Note**
>
> 1. Veuillez noter que seuls les plugins de fonctions (boutons) **en rouge** prennent en charge la lecture de fichiers. Certains plugins se trouvent dans le **menu déroulant** de la zone de plugins. De plus, nous accueillons et traitons les nouvelles pull requests pour les plugins avec **la plus haute priorité**!
>
> 2. Les fonctions de chaque fichier de ce projet sont expliquées en détail dans l'auto-analyse [`self_analysis.md`](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A). Avec l'itération des versions, vous pouvez également cliquer sur les plugins de fonctions pertinents et appeler GPT pour régénérer le rapport d'auto-analyse du projet à tout moment. Les FAQ sont résumées dans [le wiki](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98). [Méthode d'installation](#installation).
>
> 3. Ce projet est compatible avec et encourage l'utilisation de grands modèles de langage nationaux tels que chatglm, RWKV, Pangu, etc. La coexistence de plusieurs clés API est prise en charge et peut être remplie dans le fichier de configuration, tel que `API_KEY="openai-key1,openai-key2,api2d-key3"`. Lorsque vous souhaitez remplacer temporairement `API_KEY`, saisissez temporairement `API_KEY` dans la zone de saisie, puis appuyez sur Entrée pour soumettre et activer. 

<div align="center">

Functionnalité | Description
--- | ---
Révision en un clic | prend en charge la révision en un clic et la recherche d'erreurs de syntaxe dans les articles
Traduction chinois-anglais en un clic | Traduction chinois-anglais en un clic
Explication de code en un clic | Affichage, explication, génération et ajout de commentaires de code
[Raccourcis personnalisés](https://www.bilibili.com/video/BV14s4y1E7jN) | prend en charge les raccourcis personnalisés
Conception modulaire | prend en charge de puissants plugins de fonction personnalisée, les plugins prennent en charge la [mise à jour à chaud](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97)  
[Autoscanner](https://www.bilibili.com/video/BV1cj411A7VW) | [Plug-in de fonction] [Compréhension instantanée](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A) du code source de ce projet
[Analyse de programme](https://www.bilibili.com/video/BV1cj411A7VW) | [Plug-in de fonction] Analyse en un clic de la structure d'autres projets Python / C / C ++ / Java / Lua / ...
Lecture d'articles, [traduction](https://www.bilibili.com/video/BV1KT411x7Wn) d'articles | [Plug-in de fonction] Compréhension instantanée de l'article latex / pdf complet et génération de résumés
[Traduction](https://www.bilibili.com/video/BV1nk4y1Y7Js/) et [révision](https://www.bilibili.com/video/BV1FT411H7c5/) complets en latex | [Plug-in de fonction] traduction ou révision en un clic d'articles en latex
Génération de commentaires en masse | [Plug-in de fonction] Génération en un clic de commentaires de fonction en masse
Traduction [chinois-anglais](https://www.bilibili.com/video/BV1yo4y157jV/) en Markdown | [Plug-in de fonction] avez-vous vu la [README](https://github.com/binary-husky/chatgpt_academic/blob/master/docs/README_EN.md) pour les 5 langues ci-dessus?
Génération de rapports d'analyse de chat | [Plug-in de fonction] Génère automatiquement un rapport de résumé après l'exécution
[Traduction intégrale en pdf](https://www.bilibili.com/video/BV1KT411x7Wn) | [Plug-in de fonction] Extraction de titre et de résumé de l'article pdf + traduction intégrale (multi-thread)
[Aide à arxiv](https://www.bilibili.com/video/BV1LM4y1279X) | [Plug-in de fonction] Entrer l'url de l'article arxiv pour traduire et télécharger le résumé en un clic
[Aide à la recherche Google Scholar](https://www.bilibili.com/video/BV19L411U7ia) | [Plug-in de fonction] Donnez l'URL de la page de recherche Google Scholar, laissez GPT vous aider à [Ã©crire des ouvrages connexes](https://www.bilibili.com/video/BV1GP411U7Az/)
Aggrégation d'informations en ligne et GPT | [Plug-in de fonction] Permet à GPT de [récupérer des informations en ligne](https://www.bilibili.com/video/BV1om4y127ck), puis de répondre aux questions, afin que les informations ne soient jamais obsolètes
Affichage d'équations / images / tableaux | Fournit un affichage simultané de [la forme tex et de la forme rendue](https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png), prend en charge les formules mathématiques et la coloration syntaxique du code
Prise en charge des plugins à plusieurs threads | prend en charge l'appel multithread de chatgpt, un clic pour traiter [un grand nombre d'articles](https://www.bilibili.com/video/BV1FT411H7c5/) ou de programmes
Thème gradio sombre en option de démarrage | Ajoutez```/?__theme=dark``` à la fin de l'URL du navigateur pour basculer vers le thème sombre
[Prise en charge de plusieurs modèles LLM](https://www.bilibili.com/video/BV1wT411p7yf), [API2D](https://api2d.com/) | Sera probablement très agréable d'être servi simultanément par GPT3.5, GPT4, [ChatGLM de Tsinghua](https://github.com/THUDM/ChatGLM-6B), [MOSS de Fudan](https://github.com/OpenLMLab/MOSS)
Plus de modèles LLM, déploiement de [huggingface](https://huggingface.co/spaces/qingxu98/gpt-academic) | Ajout prise en charge de l'interface Newbing (nouvelle bing), introduction du support de [Jittorllms de Tsinghua](https://github.com/Jittor/JittorLLMs), [LLaMA](https://github.com/facebookresearch/llama), [RWKV](https://github.com/BlinkDL/ChatRWKV) et [Panguα](https://openi.org.cn/pangu/)
Plus de nouvelles fonctionnalités (génération d'images, etc.) ... | Voir la fin de ce document pour plus de détails ...
>>>>>>> upstream/master

</div>


<<<<<<< HEAD
Vous êtes un traducteur professionnel d'articles universitaires en français.

Ceci est un fichier Markdown, veuillez le traduire en français sans modifier les commandes Markdown existantes :

- Nouvelle interface (modifiable en modifiant l'option de mise en page dans config.py pour basculer entre les mises en page gauche-droite et haut-bas)
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230361456-61078362-a966-4eb5-b49e-3c62ef18b860.gif" width="700" >
</div>


- Tous les boutons sont générés dynamiquement en lisant functional.py, les utilisateurs peuvent ajouter librement des fonctions personnalisées pour libérer le presse-papiers.
=======
- Nouvelle interface (modifier l'option LAYOUT de `config.py` pour passer d'une disposition ``gauche-droite`` à une disposition ``haut-bas``)
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230361456-61078362-a966-4eb5-b49e-3c62ef18b860.gif" width="700" >
</div>- Tous les boutons sont générés dynamiquement en lisant functional.py et peuvent être facilement personnalisés pour ajouter des fonctionnalités personnalisées, ce qui facilite l'utilisation du presse-papiers.
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/231975334-b4788e91-4887-412f-8b43-2b9c5f41d248.gif" width="700" >
</div>

<<<<<<< HEAD
- Correction/amélioration
=======
- Correction d'erreurs/lissage du texte.
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/231980294-f374bdcb-3309-4560-b424-38ef39f04ebd.gif" width="700" >
</div>

<<<<<<< HEAD
- Si la sortie contient des formules, elles seront affichées simultanément sous forme de de texte brut et de forme rendue pour faciliter la copie et la lecture.
=======
- Si la sortie contient des équations, elles sont affichées à la fois sous forme de tex et sous forme rendue pour faciliter la lecture et la copie.
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png" width="700" >
</div>

<<<<<<< HEAD
- Pas envie de lire le code du projet ? Faites votre propre démo avec ChatGPT.
=======
- Pas envie de lire les codes de ce projet? Tout le projet est directement exposé par ChatGPT.
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="700" >
</div>

<<<<<<< HEAD
- Utilisation combinée de plusieurs modèles de langage sophistiqués (ChatGLM + OpenAI-GPT3.5 + [API2D](https://api2d.com/)-GPT4)
=======
- Appel à une variété de modèles de langage de grande envergure (ChatGLM + OpenAI-GPT3.5 + [API2D] (https://api2d.com/)-GPT4).
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/232537274-deca0563-7aa6-4b5d-94a2-b7c453c47794.png" width="700" >
</div>

<<<<<<< HEAD
Utilisation combinée de plusieurs modèles de langage sophistiqués en version de test [huggingface](https://huggingface.co/spaces/qingxu98/academic-chatgpt-beta) (la version huggingface ne prend pas en charge Chatglm).


---

## Installation - Méthode 1 : Exécution directe (Windows, Linux or MacOS)

1. Téléchargez le projet
=======
---
# Installation
## Installation-Method 1: running directly (Windows, Linux or MacOS)

1. Télécharger le projet
>>>>>>> upstream/master
```sh
git clone https://github.com/binary-husky/chatgpt_academic.git
cd chatgpt_academic
```

<<<<<<< HEAD
2. Configuration de l'API_KEY et des paramètres de proxy

Dans `config.py`, configurez les paramètres de proxy et de clé d'API OpenAI, comme indiqué ci-dessous
```
1. Si vous êtes en Chine, vous devez configurer un proxy étranger pour utiliser l'API OpenAI en toute transparence. Pour ce faire, veuillez lire attentivement le fichier config.py (1. Modifiez l'option USE_PROXY ; 2. Modifiez les paramètres de proxies comme indiqué dans les instructions).
2. Configurez votre clé API OpenAI. Vous devez vous inscrire sur le site web d'OpenAI pour obtenir une clé API. Une fois que vous avez votre clé API, vous pouvez la configurer dans le fichier config.py.
3. Tous les problèmes liés aux réseaux de proxy (temps d'attente, non-fonctionnement des proxies) sont résumés dans https://github.com/binary-husky/chatgpt_academic/issues/1.
```
(Remarque : le programme vérifie d'abord s'il existe un fichier de configuration privé nommé `config_private.py`, et utilise les configurations de celui-ci à la place de celles du fichier `config.py`. Par conséquent, si vous comprenez notre logique de lecture de configuration, nous vous recommandons fortement de créer un nouveau fichier de configuration nommé `config_private.py` à côté de `config.py` et de transférer (copier) les configurations de celui-ci dans `config_private.py`. `config_private.py` n'est pas contrôlé par git et rend vos informations personnelles plus sûres.)

3. Installation des dépendances
```sh
# (Option 1) Recommandé
python -m pip install -r requirements.txt   

# (Option 2) Si vous utilisez anaconda, les étapes sont similaires :
# (Option 2.1) conda create -n gptac_venv python=3.11
# (Option 2.2) conda activate gptac_venv
# (Option 2.3) python -m pip install -r requirements.txt

# note : Utilisez la source pip officielle ou la source pip Alibaba. D'autres sources (comme celles des universités) pourraient poser problème. Pour utiliser temporairement une autre source, utilisez :
# python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

Si vous avez besoin de soutenir ChatGLM de Tsinghua, vous devez installer plus de dépendances (si vous n'êtes pas familier avec Python ou que votre ordinateur n'est pas assez performant, nous vous recommandons de ne pas essayer) :
```sh
python -m pip install -r request_llm/requirements_chatglm.txt
```

4. Exécution
```sh
python main.py
```

5. Tester les plugins de fonctions
```
- Test Python Project Analysis
    Dans la zone de saisie, entrez `./crazy_functions/test_project/python/dqn`, puis cliquez sur "Parse Entire Python Project"
- Test d'auto-lecture du code
    Cliquez sur "[Démo multi-thread] Parser ce projet lui-même (auto-traduction de la source)"
- Test du modèle de fonctionnalité expérimentale (exige une réponse de l'IA à ce qui est arrivé aujourd'hui dans l'histoire). Vous pouvez utiliser cette fonctionnalité comme modèle pour des fonctions plus complexes.
    Cliquez sur "[Démo modèle de plugin de fonction] Histoire du Jour"
- Le menu déroulant de la zone de plugin de fonctionnalité contient plus de fonctionnalités à sélectionner.
```

## Installation - Méthode 2 : Utilisation de docker (Linux)


Vous êtes un traducteur professionnel d'articles académiques en français.

1. ChatGPT seul (recommandé pour la plupart des gens)
``` sh
# Télécharger le projet
git clone https://github.com/binary-husky/chatgpt_academic.git
cd chatgpt_academic
# Configurer le proxy outre-mer et la clé API OpenAI
Modifier le fichier config.py avec n'importe quel éditeur de texte
# Installer
docker build -t gpt-academic .
# Exécuter
docker run --rm -it --net=host gpt-academic

# Tester les modules de fonction
## Tester la fonction modèle des modules (requiert la réponse de GPT à "qu'est-ce qui s'est passé dans l'histoire aujourd'hui ?"), vous pouvez utiliser cette fonction en tant que modèle pour implémenter des fonctions plus complexes.
Cliquez sur "[Exemple de modèle de module] Histoire d'aujourd'hui"
## Tester le résumé écrit pour le projet LaTeX
Dans la zone de saisie, tapez ./crazy_functions/test_project/latex/attention, puis cliquez sur "Lire le résumé de l'article de recherche LaTeX"
## Tester l'analyse du projet Python
Dans la zone de saisie, tapez ./crazy_functions/test_project/python/dqn, puis cliquez sur "Analyser l'ensemble du projet Python"

D'autres fonctions sont disponibles dans la liste déroulante des modules de fonction.
```

2. ChatGPT+ChatGLM (nécessite une grande connaissance de docker et une configuration informatique suffisamment puissante)
``` sh
# Modifier le dockerfile
cd docs && nano Dockerfile+ChatGLM
# Comment construire | 如何构建 （Dockerfile+ChatGLM在docs路径下，请先cd docs）
docker build -t gpt-academic --network=host -f Dockerfile+ChatGLM .
# Comment exécuter | 如何运行 (1) Directement exécuter :
docker run --rm -it --net=host --gpus=all gpt-academic
# Comment exécuter | 如何运行 (2) Je veux effectuer quelques ajustements dans le conteneur avant de lancer :
docker run --rm -it --net=host --gpus=all gpt-academic bash
```

## Installation - Méthode 3 : Autres méthodes de déploiement

1. Déploiement sur un cloud serveur distant
Veuillez consulter le [wiki de déploiement-1](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%9C%E7%A8%8B%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)

2. Utilisation de WSL2 (Windows Subsystem for Linux)
Veuillez consulter le [wiki de déploiement-2](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BD%BF%E7%94%A8WSL2%EF%BC%88Windows-Subsystem-for-Linux-%E5%AD%90%E7%B3%BB%E7%BB%9F%EF%BC%89%E9%83%A8%E7%BD%B2)


## Configuration de la procuration de l'installation
### Méthode 1 : Méthode conventionnelle
[Configuration de la procuration](https://github.com/binary-husky/chatgpt_academic/issues/1)

### Méthode 2 : Tutoriel pour débutant pur
[Tutoriel pour débutant pur](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BB%A3%E7%90%86%E8%BD%AF%E4%BB%B6%E9%97%AE%E9%A2%98%E7%9A%84%E6%96%B0%E6%89%8B%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%EF%BC%88%E6%96%B9%E6%B3%95%E5%8F%AA%E9%80%82%E7%94%A8%E4%BA%8E%E6%96%B0%E6%89%8B%EF%BC%89)


---

## Personnalisation des nouveaux boutons pratiques (personnalisation des raccourcis académiques)
Ouvrez le fichier `core_functional.py` avec n'importe quel éditeur de texte, ajoutez les éléments suivants, puis redémarrez le programme. (Si le bouton a déjà été ajouté avec succès et est visible, le préfixe et le suffixe pris en charge peuvent être modifiés à chaud sans avoir besoin de redémarrer le programme.)
Par exemple:
```
"Traduction Français-Chinois": {
    # Préfixe, qui sera ajouté avant votre saisie. Par exemple, pour décrire votre demande, telle que la traduction, le débogage de code, l'amélioration, etc.
    "Prefix": "Veuillez traduire le contenu ci-dessous en chinois, puis expliquer chaque terme propre mentionné dans un tableau Markdown :\n\n", 
    
    # Suffixe, qui sera ajouté après votre saisie. Par exemple, en combinaison avec un préfixe, vous pouvez mettre le contenu de votre saisie entre guillemets.
    "Suffix": "",
},
```

=======
2. Configuration de la clé API

Dans `config.py`, configurez la clé API et d'autres paramètres. Consultez [Special network environment settings] (https://github.com/binary-husky/gpt_academic/issues/1).

(P.S. Lorsque le programme est exécuté, il vérifie en premier s'il existe un fichier de configuration privé nommé `config_private.py` et remplace les paramètres portant le même nom dans `config.py` par les paramètres correspondants dans `config_private.py`. Par conséquent, si vous comprenez la logique de lecture de nos configurations, nous vous recommandons vivement de créer un nouveau fichier de configuration nommé `config_private.py` à côté de `config.py` et de transférer (copier) les configurations de `config.py`. `config_private.py` n'est pas contrôlé par Git et peut garantir la sécurité de vos informations privées. P.S. Le projet prend également en charge la configuration de la plupart des options via "variables d'environnement", le format d'écriture des variables d'environnement est référencé dans le fichier `docker-compose`. Priorité de lecture: "variables d'environnement" > `config_private.py` > `config.py`)


3. Installer les dépendances
```sh
# (Option I: python users instalation) (Python version 3.9 or higher, the newer the better). Note: use official pip source or ali pip source. To temporarily change the source: python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python -m pip install -r requirements.txt

# (Option II: non-python users instalation) Use Anaconda, the steps are similar (https://www.bilibili.com/video/BV1rc411W7Dr):
conda create -n gptac_venv python=3.11    # Create anaconda env
conda activate gptac_venv                 # Activate anaconda env
python -m pip install -r requirements.txt # Same step as pip instalation
```

<details><summary>Cliquez ici pour afficher le texte si vous souhaitez prendre en charge THU ChatGLM/FDU MOSS en tant que backend.</summary>
<p>

【Optional】 Si vous souhaitez prendre en charge THU ChatGLM/FDU MOSS en tant que backend, des dépendances supplémentaires doivent être installées (prérequis: compétent en Python + utilisez Pytorch + configuration suffisante de l'ordinateur):
```sh
# 【Optional Step I】 Support THU ChatGLM. Remarque sur THU ChatGLM: Si vous rencontrez l'erreur "Appel à ChatGLM échoué, les paramètres ChatGLM ne peuvent pas être chargés normalement", reportez-vous à ce qui suit: 1: La version par défaut installée est torch+cpu, si vous souhaitez utiliser cuda, vous devez désinstaller torch et réinstaller torch+cuda; 2: Si le modèle ne peut pas être chargé en raison d'une configuration insuffisante de l'ordinateur local, vous pouvez modifier la précision du modèle dans request_llm/bridge_chatglm.py, modifier AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True) par AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
python -m pip install -r request_llm/requirements_chatglm.txt  

# 【Optional Step II】 Support FDU MOSS
python -m pip install -r request_llm/requirements_moss.txt
git clone https://github.com/OpenLMLab/MOSS.git request_llm/moss  # Note: When running this line of code, you must be in the project root path.

# 【Optional Step III】Make sure the AVAIL_LLM_MODELS in the config.py configuration file contains the desired model. Currently, all models supported are as follows (the jittorllms series currently only supports the docker scheme):
AVAIL_LLM_MODELS = ["gpt-3.5-turbo", "api2d-gpt-3.5-turbo", "gpt-4", "api2d-gpt-4", "chatglm", "newbing", "moss"] # + ["jittorllms_rwkv", "jittorllms_pangualpha", "jittorllms_llama"]
```

</p>
</details>



4. Exécution
```sh
python main.py
```5. Plugin de fonction de test
```
- Fonction de modèle de plugin de test (requiert que GPT réponde à ce qui s'est passé dans l'histoire aujourd'hui), vous pouvez utiliser cette fonction comme modèle pour mettre en œuvre des fonctionnalités plus complexes.
    Cliquez sur "[Démo de modèle de plugin de fonction] Aujourd'hui dans l'histoire"
```

## Installation - Méthode 2: Utilisation de Docker

1. ChatGPT uniquement (recommandé pour la plupart des gens)

``` sh
git clone https://github.com/binary-husky/chatgpt_academic.git  # Télécharger le projet
cd chatgpt_academic                                 # Accéder au chemin
nano config.py                                      # Editez config.py avec n'importe quel éditeur de texte en configurant "Proxy", "API_KEY" et "WEB_PORT" (p. ex. 50923)
docker build -t gpt-academic .                      # Installer

# (Dernière étape - choix1) Dans un environnement Linux, l'utilisation de `--net=host` est plus facile et rapide
docker run --rm -it --net=host gpt-academic
# (Dernière étape - choix 2) Dans un environnement macOS/Windows, seule l'option -p permet d'exposer le port du récipient (p.ex. 50923) au port de l'hôte.
docker run --rm -it -e WEB_PORT=50923 -p 50923:50923 gpt-academic
```

2. ChatGPT + ChatGLM + MOSS (il faut connaître Docker)

``` sh
# Modifiez docker-compose.yml, supprimez la solution 1 et la solution 3, conservez la solution 2. Modifiez la configuration de la solution 2 dans docker-compose.yml en suivant les commentaires.
docker-compose up
```

3. ChatGPT + LLAMA + PanGu + RWKV (il faut connaître Docker)
``` sh
# Modifiez docker-compose.yml, supprimez la solution 1 et la solution 2, conservez la solution 3. Modifiez la configuration de la solution 3 dans docker-compose.yml en suivant les commentaires.
docker-compose up
```


## Installation - Méthode 3: Autres méthodes de déploiement

1. Comment utiliser une URL de proxy inversé / Microsoft Azure Cloud API
Configurez simplement API_URL_REDIRECT selon les instructions de config.py.

2. Déploiement distant sur un serveur cloud (connaissance et expérience des serveurs cloud requises)
Veuillez consulter [Wiki de déploiement-1] (https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%9C%E7%A8%8B%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97).

3. Utilisation de WSL2 (sous-système Windows pour Linux)
Veuillez consulter [Wiki de déploiement-2] (https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BD%BF%E7%94%A8WSL2%EF%BC%88Windows-Subsystem-for-Linux-%E5%AD%90%E7%B3%BB%E7%BB%9F%EF%BC%89%E9%83%A8%E7%BD%B2).

4. Comment exécuter sous un sous-répertoire (tel que `http://localhost/subpath`)
Veuillez consulter les [instructions d'exécution de FastAPI] (docs/WithFastapi.md).

5. Utilisation de docker-compose
Veuillez lire docker-compose.yml, puis suivre les instructions fournies.

# Utilisation avancée
## Personnalisation de nouveaux boutons pratiques / Plugins de fonctions personnalisées

1. Personnalisation de nouveaux boutons pratiques (raccourcis académiques)
Ouvrez core_functional.py avec n'importe quel éditeur de texte, ajoutez une entrée comme suit, puis redémarrez le programme. (Si le bouton a été ajouté avec succès et est visible, le préfixe et le suffixe prennent en charge les modifications à chaud et ne nécessitent pas le redémarrage du programme pour prendre effet.)
Par exemple
```
"Super coller sens": {
    # Préfixe, sera ajouté avant votre entrée. Par exemple, pour décrire votre demande, telle que traduire, expliquer du code, faire la mise en forme, etc.
    "Prefix": "Veuillez traduire le contenu suivant en chinois, puis expliquer chaque terme proprement nommé qui y apparaît avec un tableau markdown:\n\n", 
    
    # Suffixe, sera ajouté après votre entrée. Par exemple, en utilisant le préfixe, vous pouvez entourer votre contenu d'entrée de guillemets.
    "Suffix": "",
},
```
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226899272-477c2134-ed71-4326-810c-29891fe4a508.png" width="500" >
</div>

<<<<<<< HEAD
---


## Présentation de certaines fonctionnalités

### Affichage des images:

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/228737599-bf0a9d9c-1808-4f43-ae15-dfcc7af0f295.png" width="800" >
</div>


### Si un programme peut comprendre et décomposer lui-même :

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226936850-c77d7183-0749-4c1c-9875-fd4891842d0c.png" width="800" >
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226936618-9b487e4b-ab5b-4b6e-84c6-16942102e917.png" width="800" >
</div>


### Analyse de tout projet Python/Cpp quelconque :
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="800" >
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226969067-968a27c1-1b9c-486b-8b81-ab2de8d3f88a.png" width="800" >
</div>

### Lecture et résumé générés automatiquement pour les articles en Latex
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/227504406-86ab97cd-f208-41c3-8e4a-7000e51cf980.png" width="800" >
</div>

### Génération de rapports automatique
=======
2. Plugins de fonctions personnalisées

Écrivez des plugins de fonctions puissants pour effectuer toutes les tâches que vous souhaitez ou que vous ne pouvez pas imaginer.
Les plugins de ce projet ont une difficulté de programmation et de débogage très faible. Si vous avez des connaissances de base en Python, vous pouvez simuler la fonctionnalité de votre propre plugin en suivant le modèle que nous avons fourni.
Veuillez consulter le [Guide du plugin de fonction] (https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97) pour plus de détails.

---
# Latest Update

## Nouvelles fonctionnalités en cours de déploiement.

1. Fonction de sauvegarde de la conversation.
Appelez simplement "Enregistrer la conversation actuelle" dans la zone de plugin de fonction pour enregistrer la conversation actuelle en tant que fichier html lisible et récupérable. De plus, dans la zone de plugin de fonction (menu déroulant), appelez "Charger une archive de l'historique de la conversation" pour restaurer la conversation précédente. Astuce : cliquer directement sur "Charger une archive de l'historique de la conversation" sans spécifier de fichier permet de consulter le cache d'archive html précédent. Cliquez sur "Supprimer tous les enregistrements locaux de l'historique de la conversation" pour supprimer le cache d'archive html.

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/235222390-24a9acc0-680f-49f5-bc81-2f3161f1e049.png" width="500" >
</div>



2. Générer un rapport. La plupart des plugins génèrent un rapport de travail après l'exécution.
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/227503770-fe29ce2c-53fd-47b0-b0ff-93805f0c2ff4.png" height="300" >
<img src="https://user-images.githubusercontent.com/96192199/227504617-7a497bb3-0a2a-4b50-9a8a-95ae60ea7afd.png" height="300" >
<img src="https://user-images.githubusercontent.com/96192199/227504005-efeaefe0-b687-49d0-bf95-2d7b7e66c348.png" height="300" >
</div>

<<<<<<< HEAD
### Conception de fonctionnalités modulaires
=======
3. Conception de fonctionnalités modulaires avec une interface simple mais capable d'une fonctionnalité puissante.
>>>>>>> upstream/master
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/229288270-093643c1-0018-487a-81e6-1d7809b6e90f.png" height="400" >
<img src="https://user-images.githubusercontent.com/96192199/227504931-19955f78-45cd-4d1c-adac-e71e50957915.png" height="400" >
</div>

<<<<<<< HEAD

### Traduction de code source en anglais

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/229720562-fe6c3508-6142-4635-a83d-21eb3669baee.png" height="400" >
</div>

## À faire et planification de version :
- version 3.2+ (à faire) : Prise en charge de plus de paramètres d'interface de plugin de fonction
- version 3.1 : Prise en charge de l'interrogation simultanée de plusieurs modèles GPT ! Prise en charge de l'API2d, prise en charge de la répartition de charge de plusieurs clés API
- version 3.0 : Prise en charge de chatglm et d'autres petits llm
- version 2.6 : Réorganisation de la structure du plugin, amélioration de l'interactivité, ajout de plus de plugins
- version 2.5 : Mise à jour automatique, résolution du problème de dépassement de jeton et de texte trop long lors de la compilation du code source complet
- version 2.4 : (1) Ajout de la fonctionnalité de traduction intégrale de PDF ; (2) Ajout d'une fonctionnalité de changement de position de zone de saisie ; (3) Ajout d'une option de disposition verticale ; (4) Optimisation du plugin de fonction multi-thread.
- version 2.3 : Amélioration de l'interactivité multi-thread
- version 2.2 : Prise en charge du rechargement à chaud du plugin de fonction
- version 2.1 : Mise en page pliable
- version 2.0 : Introduction du plugin de fonction modulaire
- version 1.0 : Fonctionnalité de base

## Références et apprentissage

```
De nombreux designs d'autres projets exceptionnels ont été utilisés pour référence dans le code, notamment :

# Projet 1 : De nombreuses astuces ont été empruntées à ChuanhuChatGPT
https://github.com/GaiZhenbiao/ChuanhuChatGPT

# Projet 2 : ChatGLM-6B de Tsinghua :
https://github.com/THUDM/ChatGLM-6B
```

=======
4. C'est un projet open source qui peut "se traduire de lui-même".
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226936850-c77d7183-0749-4c1c-9875-fd4891842d0c.png" width="500" >
</div>

5. Traduire d'autres projets open source n'est pas un problème.
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="500" >
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226969067-968a27c1-1b9c-486b-8b81-ab2de8d3f88a.png" width="500" >
</div>

6. Fonction de décoration de live2d (désactivée par défaut, nécessite une modification de config.py).
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/236432361-67739153-73e8-43fe-8111-b61296edabd9.png" width="500" >
</div>

7. Prise en charge du modèle de langue MOSS.
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/236639178-92836f37-13af-4fdd-984d-b4450fe30336.png" width="500" >
</div>

8. Génération d'images OpenAI.
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/bc7ab234-ad90-48a0-8d62-f703d9e74665" width="500" >
</div>

9. Analyse et synthèse vocales OpenAI.
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/709ccf95-3aee-498a-934a-e1c22d3d5d5b" width="500" >
</div>

10. Correction de la totalité des erreurs de Latex.
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/651ccd98-02c9-4464-91e1-77a6b7d1b033" width="500" >
</div>


## Versions :
- version 3.5 (À faire) : appel de toutes les fonctions de plugin de ce projet en langage naturel (priorité élevée)
- version 3.4 (À faire) : amélioration du support multi-thread de chatglm en local
- version 3.3 : Fonctionnalité intégrée d'informations d'internet 
- version 3.2 : La fonction du plugin de fonction prend désormais en charge des interfaces de paramètres plus nombreuses (fonction de sauvegarde, décodage de n'importe quel langage de code + interrogation simultanée de n'importe quelle combinaison de LLM)
- version 3.1 : Prise en charge de l'interrogation simultanée de plusieurs modèles GPT ! Support api2d, équilibrage de charge multi-clé api.
- version 3.0 : Prise en charge de chatglm et autres LLM de petite taille.
- version 2.6 : Refonte de la structure des plugins, amélioration de l'interactivité, ajout de plus de plugins.
- version 2.5 : Auto-mise à jour, résolution des problèmes de texte trop long et de dépassement de jetons lors de la compilation du projet global.
- version 2.4 : (1) Nouvelle fonction de traduction de texte intégral PDF ; (2) Nouvelle fonction de permutation de position de la zone d'entrée ; (3) Nouvelle option de mise en page verticale ; (4) Amélioration des fonctions multi-thread de plug-in.
- version 2.3 : Amélioration de l'interactivité multithread.
- version 2.2 : Les plugins de fonctions peuvent désormais être rechargés à chaud.
- version 2.1 : Disposition pliable
- version 2.0 : Introduction de plugins de fonctions modulaires
- version 1.0 : Fonctionnalités de base

gpt_academic développeur QQ groupe-2：610599535

- Problèmes connus
    - Certains plugins de traduction de navigateur perturbent le fonctionnement de l'interface frontend de ce logiciel
    - Des versions gradio trop hautes ou trop basses provoquent de nombreuses anomalies

## Référence et apprentissage

```
De nombreux autres excellents projets ont été référencés dans le code, notamment :

# Projet 1 : ChatGLM-6B de Tsinghua :
https://github.com/THUDM/ChatGLM-6B

# Projet 2 : JittorLLMs de Tsinghua :
https://github.com/Jittor/JittorLLMs

# Projet 3 : Edge-GPT :
https://github.com/acheong08/EdgeGPT

# Projet 4 : ChuanhuChatGPT :
https://github.com/GaiZhenbiao/ChuanhuChatGPT

# Projet 5 : ChatPaper :
https://github.com/kaixindelele/ChatPaper

# Plus :
https://github.com/gradio-app/gradio
https://github.com/fghrsh/live2d_demo
```
>>>>>>> upstream/master
