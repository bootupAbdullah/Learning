destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

print()
print("LA's Destination Index: " + str(get_destination_index("Los Angeles, USA")))
print("Paris' Destination Index: " + str(get_destination_index("Paris, France")))
# print(get_destination_index("Hyderabad, India"))

# 15.
def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# 20.
test_destination_index = get_traveler_location(test_traveler)

print("Test Destination Index:" + str(test_destination_index))

# 24. - 25.
attractions = [[] for destination in destinations]

# 26.
print("attractions:" + str(attractions))

# 27. - 32.
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  return attractions_for_destination.append(attraction)

# 33.
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])

#34.
print(attractions)