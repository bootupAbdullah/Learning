import random

class Trainer:

    def __init__(self, input_name, input_sex, input_age = 0):
        self.name = input_name
        self.sex = input_sex
        self.age = input_age
        self.pokemon = []

    def saycatchphrase(self):
        return print("Trainer {} says: 'Gotta Catch 'Em All!'".format(self.name))
    
    def throwpokeball(self):
        print("Trainer {} threw the pokeball!".format(self.name))

    
    def __repr__(self):
        return "The is trainer {}, he is a {} and he is {} years old!".format(self.name, self.sex, self.age)


# create a trainer
abdullah = Trainer("Abdullah", "male", 36)

# test repr for tariner
print()
print(abdullah)

# test catch phrase method
abdullah.saycatchphrase()

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
    index = random.randint(0, 2)
    print("The wild {} said \"{}\".".format(self.name, self.speech[index]))
      
    #print("I said \"Hello\"") 
  
# create a pokemon
charmander = Pokemon("Charmander", "Fire", 5)

#test repr for pokemon
print()
print(charmander)

# create instance varaible
charmander.speech = ["charmander!", "char!", "char, char!"]


charmander.speak()


class Encounter:
    def __init__(self, trainer, pokemon):
        print("A wild {} appeared!".format(pokemon.name))
        choice = input("Would you like to throw your Pokeball? (press 'Y' or 'N'): ")
        
        if choice.lower() == 'y':
            print("You threw your Pokeball!")
            
        elif choice.lower() == 'n':
            print("You chose not to throw your Pokeball.")
            # Add logic for not throwing the Pokeball
        else:
            print("Invalid choice. Please press 'y' or 'n'.")

print()
encounter = Encounter(abdullah,charmander)

