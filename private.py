class Private:

    def __init__(self, name, alias):
        self.name = name        # public
        self._alias = alias     # private

    def who(self):
        print("name: ", self.name)
        print('alias : ', self._alias)


x = Private(name="Alex", alias="amen")
print(x.name)
# Alex
# public attr can be access through and instance variable

# print(x.alias)
# AttributeError: 'Private' object has no attribute 'alias'
# private attr can't be access

# print(x._alias)
# amen

print(x.who())
# name:  Alex
# alias :  amen



