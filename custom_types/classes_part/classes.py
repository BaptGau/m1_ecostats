class MaClass:
     def __init__(self) -> None:
         print("MaClass constructor")
         self.internal_variable = 0

if __name__ == "__main__":
    ma_class = MaClass()
    print(ma_class.internal_variable)
    ma_class.internal_variable = 1
    print(ma_class.internal_variable)

    ma_class_2 = MaClass()
    print(ma_class_2.internal_variable)

    print(id(ma_class), id(ma_class_2))

