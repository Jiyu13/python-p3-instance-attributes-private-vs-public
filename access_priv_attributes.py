class Student:
    _schoolName = 'XYZ School'  # protected class attribute

    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute


std = Student("Swati", 25)
print(std._name)        # Swati
print(std._age)         # 25

std._name = "Dipa"
print(std._name)        # Dipa

