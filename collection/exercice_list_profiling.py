# exercice
# mesurer le temps d'allocation/de modification d'une liste pour un nombre d'éléments variant entre
# 1 et 1.000.000 avec:
# - extend
# - append
# - prefill
# - list comprehension
# Pour les gourmands: faites ça plusieurs fois par méthode
import time


def track_list_creation_time(func, list_size: int) -> float:
    """
    Compute the execution time of a function.
    """
    start = time.time()
    func(list_size=list_size)
    end = time.time()
    return end - start


def create_list_with_append(list_size: int) -> None:
    l = list()
    for i in range(list_size):
        l.append(i)
    # ici: ma liste est crée et je peux sentir


def create_list_with_extend(list_size: int) -> None:
    l = list()
    for i in range(list_size):
        l.extend([i])


def create_list_with_prefill(list_size: int) -> None:
    l = [None] * list_size
    for i in range(list_size):
        l[i] = i


def create_list_with_list_comprehension(list_size: int) -> None:
    l = [i for i in range(list_size)]


if __name__ == "__main__":
    LIST_SIZE = 1_000_000

    append_time = track_list_creation_time(
        func=create_list_with_append, list_size=LIST_SIZE
    )
    print(f"Append time: {append_time:.4f} seconds")

    extend_time = track_list_creation_time(
        func=create_list_with_extend, list_size=LIST_SIZE
    )
    print(f"Extend time: {extend_time:.4f} seconds")

    prefill_time = track_list_creation_time(
        func=create_list_with_prefill, list_size=LIST_SIZE
    )
    print(f"Prefill time: {prefill_time:.4f} seconds")

    comprehension_time = track_list_creation_time(
        func=create_list_with_list_comprehension, list_size=LIST_SIZE
    )
    print(f"Comprehension time: {comprehension_time:.4f} seconds")

    # exercice simple:
    # créer un dictionnaire pour stocker les résultats plutôt qu'une liste
    results = {
        "Append method": append_time,
        "Extend method": extend_time,
        "Prefill method": prefill_time,
        "Comprehension method": comprehension_time,
    }

    print(len(results))
    print(results)
