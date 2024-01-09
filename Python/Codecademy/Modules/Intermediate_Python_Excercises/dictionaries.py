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

# Delete a Key Excercise
print()
print()
print("Delete a Key Excercise:")

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# 1.
for items, value:
  if "stamina grains" > 0:
  "stamina grains" + health_points



