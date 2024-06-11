import random
import time
import textwrap

# intro screen
def display_pokemon_intro():
    pokemon_logo = textwrap.dedent("""
                                  ,'\\
    _.----.        ____         ,'  _\\   ___    ___     ____
_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.
\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |
 \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |
   \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |
     \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |
      \\    \\ \\      /       `-.`.___,-' |  |\\  /| \\      /  | |   |
       \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |
        \\_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
    """)
    print(pokemon_logo)
    time.sleep(3)  # Wait for 5 seconds
    input("Please hit enter to continue")

# Call the function to display the logo
display_pokemon_intro()

print()
print()
print("Welcome to the World of Pokemon!")
print()
time.sleep(3)  # Wait for 3 seconds

player_one_name = input("Please enter your name!")
time.sleep(3)  # Wait for 3 seconds

print()
print("Thanks {}!".format(player_one_name))
time.sleep(3)  # Wait for 3 seconds

print()
print("Okay, let's get started!")
time.sleep(3)  # Wait for 3 seconds

print()
print("It's time to pick you starter pokemon!")
time.sleep(3)  # Wait for 3 seconds

print()
choice_1 = input('''
Which one would you like?

1. Pikachu 
2. Squirtle
3. Bulbasaur

** hint: You can also enter the number of the pokemon!''')
time.sleep(5)  # Wait for 5 seconds

if choice_1 == '1':
    player_1_selection = "Pikachu"
elif choice_1 == '2':
    player_1_selection = "Squirtle"
elif choice_1 == '3':
    player_1_selection = "Bulbasaur"
else:
    player_1_selection = "Unknown"
    print("Invalid choice, please try again.")

print()
print("Great, you selected: {}".format(player_1_selection))
time.sleep(5)  # Wait for 5 seconds


print()
print("Now that you have your starter it's time to headout into the wild!")
time.sleep(5)  # Wait for 5 seconds

# create a trainer class
class Trainer:

    def __init__(self, input_name):
        self.name = input_name
        self.pokemon = []

    def saycatchphrase(self):
        return print("Trainer {} says: 'Gotta Catch 'Em All!'".format(self.name))
    
    def throwpokeball(self):
        print("Trainer {} threw the pokeball!".format(self.name))
    
    def add_pokemon(self, pokemon):
        if type(pokemon) == Pokemon:
            self.pokemon.append(pokemon)
        else: 
            pass
    


# create an instance of the trainer class
trainer_1 = Trainer(player_one_name)

# test catch phrase method
print()
trainer_1.saycatchphrase()
time.sleep(5)  # Wait for 5 seconds

# new class, pokemon
class Pokemon:

    # method 1
  def __init__(self, input_name, input_type, input_level =0):
        self.name = input_name
        self.type = input_type
        self.level = input_level
        self.max_health = 100
        self.attacks = []
    
    # method 2
class Pokemon:
    def __init__(self, input_name, input_type, input_level=0):
        self.name = input_name
        self.type = input_type
        self.level = input_level

    def __repr__(self):
        return (
            "A wild Pokemon appeared!\n"
            "This is the {} type pokemon {}, it's currently at level {}"
        ).format(self.type, self.name, self.level)
  
    # method 3
    def knock_out(self):
      if self.max_health == 0:
          print("{} has knocked out!".format(self.name))
    
    # method 4
    def speak(self):
        index = random.randint(0, 2)
        print("The wild {} said \"{}\".".format(self.name, self.speech[index]))
      
    #print("I said \"Hello\"") 
  
# create an instance of the pokemon class
charmander = Pokemon("Charmander", "Fire", 5)

#test repr for pokemon
print()
print(charmander)
time.sleep(3)  # Wait for 3 seconds

# create instance varaible
charmander.speech = ["charmander!", "char!", "char, char!"]

# test pokemon speak method
charmander.speak()
time.sleep(5)  # Wait for 5 seconds

class Encounter:
    def __init__(self, trainer, pokemon):
        choice = input("Would you like to throw your Pokeball? (press 'Y' or 'N'): ")
        
        if choice.lower() == 'y':
            print("You threw your Pokeball!")
            trainer.add_pokemon(pokemon)
            animate_pokeball()
            print("Congratulations, you caught a {}!".format(pokemon.name))           
            
        elif choice.lower() == 'n':
            print("You chose not to throw your Pokeball.")
            
        else:
            print("Invalid choice. Please press 'y' or 'n'.")

# animation for pokeball
def animate_pokeball():
    frames = ["(o)", " o ", "(o)", " o "]
    for _ in range(3):
        for frame in frames:
            print(frame, end='\r')
            time.sleep(0.2)


print()
encounter = Encounter(trainer_1,charmander)

