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

# new class
class Pokemon:

  def __init__(self, input_name, input_type, input_level =0):
        self.name = input_name
        self.type = input_type
        self.level = input_level
        self.max_health = 100
        self.attacks = []
        
  def __repr__(self):
      return "This is the {} type pokemon {}, it's currently at level {}".format(self.type, self.name, self.level)
  
# create a pokemon
pokemon_1 = Pokemon("Charmander", "Fire", 5)

#test repr for pokemon
print(pokemon_1)


# test catch phrase method
trainer_1.saycatchphrase()
