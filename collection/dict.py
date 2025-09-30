mon_dict = dict()

mon_dict: dict[str, str] = {
    "name": "Baptiste",
    "surname": "Gautier",
    "age": "25",
}

# ajout d'élément
mon_dict["linkedin"] = "<inserer_lien_linkedin>"

# recherche
print(mon_dict["name"])
# print(mon_dict[14])
# recherche "safe"
print(mon_dict.get(14, "Not in the dict"))

# comprehension
print({f"Nombre {i}": i for i in range(10)})




