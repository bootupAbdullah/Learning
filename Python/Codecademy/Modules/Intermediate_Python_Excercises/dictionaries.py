songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# 1.
plays = {key: value for key, value in zip(songs, playcounts)}

# 2.
#print(plays)

# 3.
plays["Purple Haze"] = 1
print(plays)

# 4.
plays["Respect"] = 94

# 5.
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print()
print(library)





