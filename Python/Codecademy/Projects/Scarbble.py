letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# 1. Creating new dictionary with key,value of letter and the points each letter is worth
letter_to_points = {key: value for key, value in zip(letters, points)}

# print(letter_to_points)

# 2. adding a score of '0' for blank space
letter_to_points[" "] = 0
print()
print("How the letters are scored: ")
print()
print(letter_to_points)


# 3. -  6. This function takes a word and assigns points for each letter in the word
def score_word(word):
    point_total = 0
    word_uppercase = word.upper()
    for letter in word_uppercase:
        if letter in letter_to_points.keys():
            point_total += letter_to_points[letter]
        else:
            point_total += 0
    return point_total

# 7. - 8. Thi is a test to determine if the score_word function is working properly.
print("Funition test, 'Score_word': ")
brownie_points = score_word("brownie")
print(brownie_points)
print()

print()
print("Gameplay")
print()

# 9. This is list of players (first iteration) and a list of words each player has
player_to_words = {"player1":["blue", "tennis", "exit"], "wordNerd":["EARTH", "EYES", "MACHINE"],
"Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["zap", "coma", "period"]}

# 10.
player_to_points = {}

# 11.
#Calculate initial points for each player
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
        player_to_points[player] = player_points

# additional practice:

def play_word():
    player_to_points[players] = player_points

print()
print("current score: " + str(player_to_points))

# -- Extended Practice -- #

#Function to add a new word to a player's list
def play_word(player, word):
    print()
    print("{} just played a new word! Word: \"{} \" ".format(player,word))
    print()
    player_to_words[player].append(word)
    return print(player_to_words)



play_word("player1", "rain")


#update point totals
def update_point_totals():
    for players, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
            player_to_points[players] = player_points
    print()
    print("Updating current score...")
    return print("Current score: " + str(player_to_points))


update_point_totals()