# 📊 Projet Python – Régression Linéaire

## 🎯 Objectif

L’objectif est de **créer un programme Python** qui génère une **régression linéaire**, ses **données d’entrée** ainsi que son **résultat final**.

---

## 🧩 Description Générale

Votre code sera structuré autour de **trois objets principaux** + une **fonction principale** :

---

## 1. 📁 Dataset

### Contenu
- `X` : matrice des features — dimension *(n × p)*  
- `y` : vecteur des résultats — dimension *(n × 1)*  
- `features_name` : liste contenant les noms des colonnes *(longueur p)*

### Fonctionnalités
- Ajouter un **intercept** à la matrice `X` *(si non présent)*.  
- Convertir le dataset en **DataFrame Pandas**, en utilisant `features_name` pour nommer les colonnes.

---

## 2. 📈 Régression Linéaire

### Contenu
- `coefficients` : vecteur des coefficients du modèle *(longueur p)*  
- `features_names` : noms des features associés aux coefficients.

### Fonctionnalités
- Faire de **l’inférence** sur un nouvel échantillon *(vecteur ou matrice)*.  
- Convertir les coefficients en **dictionnaire** sous la forme :  
  ```python
  { feature_name: coefficient }
  
---

## 3. 📊 Résultats
### Contenu
- model : instance de la régression linéaire (voir point 2)
- R2 : coefficient de détermination
- y_true : valeurs réelles
- y_pred : valeurs prédites

### Fonctionnalités
#### Calculer les erreurs :
- MSE : Mean Squared Error
- RMSE : Root Mean Squared Error

#### Fournir un résumé du résultat de la prévision :
- performance du modèle
- écart entre valeurs réelles et prédites

---

## 4. 🧠 Fonction Principale
La fonction principale devra :
- Prendre un dataset en entrée
- Créer et entraîner un modèle de régression linéaire
- Retourner l’objet de résultat.

--- 

## 🧪 Remarques Générales
Pour tester le code, vous pouvez générer des données avec :
👉 [sklearn.datasets.make_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html)

### Critères d’évaluation
✅ Maintenabilité : code testé, formaté et lisible.

✅ Principe de moindre surprise : comportement prévisible et cohérent.

⚡ Efficacité : algorithmes performants.
