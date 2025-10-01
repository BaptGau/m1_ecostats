l = list()
empty_list = []

# append
non_empty_list = [12, 2.0, True, "bonjour"]
non_empty_list.append("au revoir")
print(non_empty_list)

# extend
non_empty_list = [12, 2.0, True, "bonjour"]
non_empty_list.extend(["au revoir"])
print(non_empty_list)

# prefill
prefilled_list = [None] * 10
prefilled_list[0] = 1
prefilled_list[1] = 2
prefilled_list[2] = 3
prefilled_list[7] = 4
print(prefilled_list)
print(len(prefilled_list))


def map_grade_to_comment(grade: int) -> str:
    if grade < 5:
        return "Nul"
    elif grade < 7:
        return "Pas ouf"
    elif grade < 10:
        return "Pas loin"
    elif grade < 12:
        return "Ok"
    elif grade < 15:
        return "Pas mal"
    else:
        return "Niquel"


notes = [5, 10, 12, 15, 14, 13, 20, 2, 15]

# list comprehension
comments = [map_grade_to_comment(grade=list_grade) for list_grade in notes]
print(comments)

# égal
comments = list()
for grade in notes:
    comments.append(map_grade_to_comment(grade=grade))
print(comments)


# example de fonction prenant une liste en entrée
def square(integers: list[int]) -> list[int]:
    return [integer**2 for integer in integers]


print(square([2, 4, 6, 8, 10]))


# exercice recrutement
def append_list_element(sequence: list[str], element: str):
    sequence.append(element)


def append_string_element(sequence: str, element: str):
    sequence += element


test_list = ["foo", "bar"]
append_list_element(sequence=test_list, element="baz")
print(test_list)

test_str = "foo"
append_string_element(sequence=test_str, element="baz")
print(test_str)
