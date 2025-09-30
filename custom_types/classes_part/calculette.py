class Calculette:
    def __init__(self):
        self.performed_operations = list()

    def add(self, x: int | float, y: int | float) -> int | float:
        add_result = x + y

        self.performed_operations.append(f"{x}+{y}={add_result}")

        return add_result

    def subtract(self, x: int | float, y: int | float) -> int | float:
        ...

    def divide(self, x: int | float, y: int | float) -> int | float:
        ...

    def multiply(self, x: int | float, y: int | float) -> int | float:
        ...

# utilisation
calculette = Calculette()
add_result = calculette.add(x=1, y=2)
print(add_result)
print(calculette.performed_operations)







