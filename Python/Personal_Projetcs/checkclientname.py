# client_check.py

# List of client names
client_names = [
    "Abel, Joseph", "Arbogast, Sally", "Atlee Roofing", "Ayers Property Management",
    "Ayers, Kermit", "Ayers, Sally", "Bailey, David", "Barrett, Brenda", "Battle, Berry",
    "Battle, Tanya", "Berkel, Phyllis", "Berquin, Bessie", "Bethkey, Barbara",
    "Borkowski, Marcy", "Borkowski, Stephen", "Bronson, Melinda", "Brookwell, Christopher",
    "Browning, Emily", "Buchbinder, Paige", "Carpet Cuts", "Chupp, Aaron",
    "Classic Automotive", "Coffey, Edward", "Collier, Kevin",
    "Concepts For-Profit", "Covington, Ashley", "Crider, Amy", "Daniels, Elana",
    "Dawson, Christian", "Dawson, Michelle", "Denvil, Alasdair", "Dittus, Jamie",
    "Douglas Painting", "Dowdy, Earl", "Eck, Mary", "Eckhart, Sarah",
    "Era, Amber", "Era, Joseph", "Fox, Robert", "Francisco, Michael", "Flippen, William",
    "Flickenger, Marc", "Floyd, Laura", "Feltner, Wandalyn", "Gambill, Robert",
    "Glover, Gerald", "Gollwitzer, Betty", "Gordon, Miles", "Gould-Champ, Patricia",
    "Gillette, John", "Goode, Francis", "Goodman, Mary", "Garland, Carl",
    "Going Green Inc", "Hensley, Edna", "Moss Holdren, Sidney", "Huffman, Michelle",
    "Henderson, Ruby", "Holman, Anne", "Lockhart, Bruce", "Ogden, Thomas",
    "Payne, Emily", "Peterson, Melissa", "Pitts, Ann", "Pliodzinskas, Andrius",
    "Powell, William", "Pritchett, Tim", "Quinn, Taylor", "Rains, Betty" "Rains, Randall",
    "Randolph, Bryan", "Reinhold, Adrienne", "Reinik, Amber", "Richardson, Jackie",
    "Robinson, Joseph", "Ross, Jean", "Rudlin, Craig", "Sabatino, Rosemary",
    "Samuel, Linda", "Scheffler, Betty", "Scott, Montgomery", "Scott, Hillary", "Scott, Thomas",
    "Seabury, Beau and Emily", "Self, April and Hugh", "Shue, Brad", "Shue, Dee", "Simon, Michael",
    "Michael, Joseph", "Michael, Katherine", "Smith, Renita", "Snyder, Karla", "Snyder, Larry",
    "Staley, Heidemarie", "Staley, William", "Stevens, Page", "Attaway, James", "Ayers, Kenneth & Sally",
    "Costner, David", "Dawson, Christina", "Dominon Payroll", "Dotson, Savannah",
    "Fazakas, George", "Feltner, Wandalyn", "Fox, Marianne", "Herod, Charles",
    "Jordan, Barbara", "Lafferty, BJ", "Limoges, Christopher & Michelle", "McGregor, Lynn",
    "Mesco, Adam & Sarah", "Neander Sr, Vicky & Gerald", "Ormond, Heather", "Pitts, Norma",
    "Sarkees, Denise & Travis", "Shores, Rodney", "Taney, Linda", "Thomas, Karen",
    "Toy, Bryan", "Trezza, Frank & Milagros", "Tucker, Ashley", "Tucker, Samuel",
    "Uhline, Shelly", "Walnut holdings", "Waite, Shane", "Wade, Travis", "Wood, Linda & Louise",
    "Wiley, Timothy and Tara", "Wright, Melissa and Christine", "Young, Forest",
    "Zimmerman, Ann & Bill", "Marcel, Gregory", "Martin, Greg", "Martin, Katelyn",
    "McCarthy, William", "Meade, Matthew and Monica", "Medical, Mann", "Midkiff, Tyler",
    "Minock, Larry", "Mitchell, James", "Morgan, Deborah", "Moser, Madison",
    "Montagino, Joshua", "Moore, Darren and Alyssa", "Moore, Regina", "Moore, Stewart",
    "Moran, Sandra", "Miller, Derek and Abby", "Miller, Stephen", "Nick Davis Photography",
    "Norell, Jessica and Oliver", "Norman, Timothy", "Noshe, Matthew and Monica"
]

# Function to check if a name is in the list
def check(name):
    if name in client_names:
        return print(True)
    else:
        return print(False)


check("Ayers, Sally")

