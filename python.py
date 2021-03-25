from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False  # Polymorphism of an attribute overrides the attribute from Snake

    def climb(self):
        return "up we go..."

    def swallow(self):
        return "can't be bothered to chew"

    def hunt(self):  # Polymorphism of method overrides method from Reptile class
        return "I'm hungry must hunt"


python_object = Python()
print(python_object.alive)  # alive is inherited from the Animal class
print(python_object.use_tongue_to_smell())  # use_tongue_to-smell is inherited from the Snake class
print(python_object.cold_blooded)  # cold_blooded is inherited from the Reptile class
print(python_object.climb())  # climb() is inherited from the Python class


# def have_venom(snake):
#     return snake.venom
#
#
# snake_object = Snake()
#
# print(have_venom(python_object))
# print(have_venom(snake_object))
