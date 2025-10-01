import numpy as np

# somme
tableau = [1, 2, 3, 4, 5]
somme = np.sum(tableau)
print(somme)

# tableau
tableau = np.arange(15)
print(tableau)
print(tableau.shape)

tableau = tableau.reshape(
    3, 5
)  # il faut que le nombre de ligne x le nombre de colonnes = la taille du vecteur
print(tableau)
print(tableau.shape)
print("# Somme")
print(tableau.sum(axis=0))
print(tableau.sum(axis=1))
print(tableau.sum())

# filtrage
tableau = np.arange(5)
mask = np.array([True, False, True, True, False])
filtered_tab = tableau[mask]


# Indexing
tableau = np.arange(15)
tableau = tableau.reshape(3, 5)
print(tableau[0, :])  # accéder à la première ligne
print(tableau[:, 0])  # accéder à la première colonne
print(tableau[0, 0])  # accéder au premier élément [0, 0]
# print(tableau[i, j]) # accéder à l'élément i, j

# Random
laplace_vector = np.random.laplace(loc=0, scale=1, size=500)
gaussian_vector = np.random.normal(loc=0, scale=1, size=500)
uniform_vector = np.random.uniform(low=-5, high=5, size=500)

# plot
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.set_style("darkgrid")
# plt.figure(figsize=(12, 8))
# plt.title("Echantillons aléatoires générés avec numpy")
# sns.kdeplot(gaussian_vector, fill=True, alpha=0.5, color="dodgerblue", label="Gaussian distribution")
# sns.kdeplot(laplace_vector, fill=True, alpha=0.5, color="orangered", label="Laplace distribution")
# sns.kdeplot(uniform_vector, fill=True, alpha=0.5, color="chartreuse", label="Gaussian distribution")
# plt.legend()
# plt.show()

# broadcasting
tableau = np.arange(15)
tableau = tableau.reshape(3, 5)
tableau = tableau * 10  # -> broadcasting
print(tableau)

# slicing
tableau = np.arange(15)
print("Slicing")
print(f"Avant slicing: {tableau}")
print(f"Sliced: {tableau[5:11]}")  # on récupère les éléments aux indices 5 à 10
# tableau[i, j] -> créer un sous tableau des éléments compris entre i et j-1


# modification
tableau[1] = 1000
print(tableau)
tableau[1:9] = np.arange(8) * 1000
print(tableau)
