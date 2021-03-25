## Object-oriented programming

### What is OOP?
- Method of structuring a software program into bundles of related attributes and behaviours
- It is designed to create simple and reusable pieces of code that any programmer or program can use it.

### Why use OOP?
- It makes your code reusable and logical and it makes inheritance easier to implement.
- It follows the DRY principle which makes programs more efficient.

### Four pillars of OOP
- The four pillars of OOP are:
    - Inheritance
    - Abstraction
    - Encapsulation
    - Polymorphism

#### Inheritance
- Inheritance is a way of creating a new class for using details of a class without modifying it.
- The existing class is known as the parent class, and the derived class is known as the child class.

#### Abstraction
- Abstraction is the method of hiding some information from the user that the user does not require in order to
  run the program.

#### Encapsulation
- Encapsulation prevents data from direct modification by restricting access to methods and variables.
- Private attributes are denoted by an underscore either single or double.

#### Polymorphism
- Polymorphism is an ability to use a common interface for multiple data types.
- You can inherit from the parent class as well as override the data

### Creating a class
- Syntax: class is the key word then name of the class
```
class Animal():
    pass  # pass is a key word used to by pass the code
```
- A class with attributes and methods.
```
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
```

- Importing Animal class for use in a new file.
```
from animal import Animal # this is
```
- Creating a child class that inherits from the Animal class.
```
class Reptile(Animal):  # we need to pass the animal class as an arg in our Reptile class
    def __init__(self):
        super().__init__() # super is to make everything available from parent class
        self.cold_blooded = True
        self. tetrapod = None
        self.heart_chambers = [3,4]

    def hunt(self):
        return "working hard to catch the next meal"

    def use_venom(self):
        return "I use it if i've got it"

    def seek_heat(self):
        return "looking for sunshine"
```

- Let's see amazing benefits of inheritance
`reptile_object = Reptile()`
- Time to see the magic of OOP
```
print(reptile_object.hunt())
print(reptile_object.breath())
```

