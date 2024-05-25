class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

class Add:
  def __init__(self):
    print(1+1)

number = Add()


# working on __repr__

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  # add a __repr__ method
  def __repr__(self):
    return "{} with radius {}".format(self.name, self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

medium_pizza.name = "medium pizza box"
teaching_table.name = "teaching table"
round_room.name = "round room"

# print out Circles
print(medium_pizza)
print(teaching_table)
print(round_room)


# building a game in python for Codecademy
# code from artcile on classes below

class Dog:
  # To create a Dog, give it a name, breed, and age. age is in years. 
  # If you don't give an age, we'll say it's 0 years old (a puppy).
  # All dogs also start as friendly!
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness = True):
    # self.name is this specific dog's name
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_friendly = input_friendliness


    dog_one = Dog("Sparky", "Golden Retriever", 5)

    

