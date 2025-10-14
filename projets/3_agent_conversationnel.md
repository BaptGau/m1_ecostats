# 🤖 Projet Python – Agent Conversationnel

## 🎯 Objectif

L’objectif est de **concevoir un programme Python** permettant d’**évaluer la verbosité** de différents **modèles de langage (LLM)** lors d’une conversation structurée.  
L’analyse se base sur les échanges entre l’utilisateur et l’agent conversationnel.

---

## 🧩 Description Générale

Le projet s’articule autour de **trois grands volets** :

1. 📄 **Gestion des prises de parole (ChatTurn & Conversation)**  
2. 💬 **Exécution d’un script de discussion**  
3. 📊 **Benchmark de plusieurs modèles de langage**

---

## 1. 📄 ChatTurn & Conversation

### Définition
- Un `ChatTurn` est un objet représentant une **prise de parole unique**.  
- Une **Conversation** est une **collection ordonnée** de `ChatTurn`.

### Contenu d’un `ChatTurn`
- `speaker` : le locuteur (`User` ou `AI`)  
- `message` : la chaîne de caractères prononcée par le locuteur

### Fonctionnalités
- ➕ Ajouter une prise de parole à une conversation  
- 🧮 Calculer des **statistiques de verbosité** :
  - longueur moyenne des messages par speaker
  - longueur maximale et minimale
  - nombre total de tokens ou de mots par speaker
- 📊 Extraire ces statistiques sous une forme exploitable (ex. dictionnaire ou DataFrame)

---

## 2. 💬 Script de Discussion

### Objectif
- Mettre en place un **script automatisé** posant `n` questions successives à un modèle conversationnel.  
- Enregistrer chaque réponse dans la conversation sous forme de `ChatTurn`.

### Fonctionnalités
- Définir une **liste de questions standardisées** pour assurer des comparaisons équitables.  
- Exécuter le script sur un ou plusieurs modèles.  
- Stocker toutes les prises de parole pour analyse.

---

## 3. 🌐 Gestion du chat

Gérer comment interagir avec l'API Open AI de Nebius pour différents modèles.
- Faire une fonction "wrappant" l'usage de Nebius ou de n'importe lequel de vos providers.

## 4. 📊 Benchmark des Modèles

### Objectif
Comparer différents LLM sur la base de leur **verbosité**.

### Fonctionnalités
- 🧠 Exécuter le **même script** sur plusieurs modèles  
- 📈 Calculer les statistiques de verbosité pour chaque modèle :
  - longueur moyenne de réponse
  - écart-type / distribution des longueurs
  - nombre de tokens produits
- ⚖️ Identifier :
  - les modèles les plus verbeux
  - les modèles les plus concis

### Bonus
- 🌀 **Répéter l’expérience plusieurs fois** pour obtenir une **distribution** plus robuste des mesures de verbosité.  
- Générer des visualisations (ex. boxplots, histogrammes) pour comparer les modèles.

---

## 🧪 Remarques Générales

- Pour tester différents modèles, vous pouvez utiliser 

- 👉 [Nebius AI Studio](http://studio.nebius.com/) *(pensez à créer une clé API)*.

### Critères d’évaluation
- ✅ **Maintenabilité** : code propre, lisible et testé  
- ✅ **Principe de moindre surprise** : comportement prévisible et cohérent  
- ⚡ **Efficacité** : algorithmes performants et peu coûteux