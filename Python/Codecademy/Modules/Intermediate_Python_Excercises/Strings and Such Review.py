highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print("Highlighted_Poems: " + str(highlighted_poems))

highlighted_poems_list = highlighted_poems.split(",")

print()
print("Highlighted_Poems_List: " + str(highlighted_poems_list))

# .4, Creating an empty list:
highlighted_poems_stripped = []

# 4b, Iterating throgh highlighted_poems_list:
## my method:
for lists in highlighted_poems_list:
  stripped_string = lists.strip()
  highlighted_poems_stripped.append(stripped_string)

print()
print("Highlighted_Poems_Stripped: " + str(highlighted_poems_stripped))

# ## method provided by Chat GPT:
# stripped_list = [s.strip() for s in highlighted_poems_list]
# print()
# print(stripped_list)

# 6. Break up all the information for each poem:
highlighted_poems_details = []

# 7. Iterate through list

highlighted_poems_details = [details.split(":") for details in highlighted_poems_stripped]

# 8. Create three new lists:
titles = []
poets = []
dates = []

print()
print("Highlighted_Poems_Details: " + str(highlighted_poems_details))


for items in highlighted_poems_details:
  items[0] = titles
  items[1] = poets
  items[2] = dates

find_item = highlighted_poem


