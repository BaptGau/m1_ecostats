from dataclasses import dataclass


# Panier -> contient: une liste de produits
# peut faire la somme des prix de tous les produits qu'il contient


# Produit -> contient
# - un nom (chaine de caractère)
# - un prix (réel)


# exercice: Créer un panier de trois (ou plus) produits et faire la somme
@dataclass
class Produit:
    nom: str
    prix: float


@dataclass
class Panier:
    produits: list[Produit]

    def somme_des_produits(self) -> int:
        return sum(produit.prix for produit in self.produits)


# définition des produits
ordinateur = Produit(nom="ordinateur", prix=350.45)
farine = Produit(nom="farine", prix=1)
oeufs = Produit(nom="oeufs par 6 bio", prix=3)
sucre = Produit(nom="sucre de canne", prix=2)

# définition du panier
panier_vide = Panier(produits=[])
print(panier_vide.somme_des_produits())

panier = Panier(
    produits=[ordinateur, farine, oeufs, sucre],
)

# accès à la variable
produits_du_panier = panier.produits

# somme
somme_des_produits = panier.somme_des_produits()
print(somme_des_produits)
