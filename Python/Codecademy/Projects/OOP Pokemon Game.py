import random

class Trainer:

    def __init__(self, input_name, input_sex, input_age = 0):
        self.name = input_name
        self.sex = input_sex
        self.age = input_age
        self.pokemon = []

    def saycatchphrase(self):
        return print("Trainer {} says 'Gotta Catch 'Em All!'".format(self.name))
    
    def __repr__(self):
        return "The is trainer {}, he is a {} and he is {} years old!".format(self.name, self.sex, self.age)


# create a trainer
trainer_1 = Trainer("Abdullah", "male", 36)

# test repr for tariner
print(trainer_1)

# test catch phrase method
trainer_1.saycatchphrase()

# new class
class Pokemon:

    # method 1
  def __init__(self, input_name, input_type, input_level =0):
        self.name = input_name
        self.type = input_type
        self.level = input_level
        self.max_health = 100
        self.attacks = []
    
    # method 2
  def __repr__(self):
      return "This is the {} type pokemon {}, it's currently at level {}".format(self.type, self.name, self.level)
  
    # method 3
  def knock_out(self):
      if self.max_health == 0:
          print("{} has knocked out!".format(self.name))
    
    # method 4
  def speak(self):
      random_number = random.randint(1, 3)
      for phrases in self.speech:
          print(random_number)
  
# create a pokemon
wild_charmander = Pokemon("Charmander", "Fire", 5)

#test repr for pokemon
print(wild_charmander)


# create instance varaile
wild_charmander.speech = ["charmander!", "char!", "char, char!"]

print(wild_charmander.speak)


# #def random_number_method(self):
#         random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
#         print(f"Random number: {random_number}")