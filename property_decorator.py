class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print(f"get name: {self._name}")
        return self._name

    @name.setter
    def name(self, newname):
        print(f"set name: {self.newname}")
        self._name = newname


std = Person("Swati")
print(std.name)    # Swati

std._name = "Dipa"
print(std.name)    # Dipa

print(std._name)    # still accessible
# Dipa