destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

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

# 34.
print(attractions)

# 35.
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# 38. - 47.
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for items in attractions_in_city:
        possible_attractions = items
        attractions_tags = items[1]
        for interest in interests:
            if interest in attractions_tags:
                attractions_with_interest.append
                # 49. Append index to [0] to remove tags
                (possible_attractions[0])
                return attractions_with_interest


la_arts = find_attractions("Los Angeles, USA", ['art'])

# 48.
print(la_arts)


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + str(traveler[0]) + " , we think you'll like these places around  "
    for attraction in traveler_attractions:
        interest_string += attraction
    return interest_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', 'monument'])

print(smills_france)
