# Let's create our first class
# syntax: class is the key word then name of the class

class Animals():
    pass  # pass is a key word used to by pass the code


class Animal():
    name = "Dog"  # class variable

    def __init__(self):  # self refers to the current class
        self.alive = True  # Attributes/variables
        self.spine = True
        self.lungs = True

    def move(self):
        return "moving left, right and centre"

    def eat(self):
        return "keep eating to stay alive"

    def breath(self):
        return "keep breathing if you want to live"


cat = Animal()  # this will store all the data available in the animal class
oriental_long_hair = Animal()
print(cat.eat())  # eat() is now ABSTRACTED
print(oriental_long_hair.lungs)
oriental_long_hair.lungs = False  # Polymorphism here we utilised to override the value of lungs
# particularly for oriental_long_hair cat
print(oriental_long_hair.lungs)
