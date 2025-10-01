s = set()
s = {
    "foo",
    "bar",
    "baz",
    13,
    15,
}

# recherche
print("foo" in s)
print("chaudron" in s)

# Exercice
# prendre la liste ['foo', 'foo', 'foo', 'bar'] et enlever les doublons (1 ligne de code)
l = {"foo", "foo", "foo", "bar"}
print(l)
# ou:
l = ["foo", "foo", "foo", "bar"]
print(set(l))
# ou:
l = {element for element in l}
print(l)
