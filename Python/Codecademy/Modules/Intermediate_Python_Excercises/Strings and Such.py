#    !! --- Excercise 1 --- !!

first_name = "Reiko"
last_name = "Matsuki"

'My first attempt at writing this code:'
#
# def password_generator(first_name, last_name):
#   len_1 = len(first_name)
#   len_2 = len(last_name)
#   temp_pass = first_name[len_1-3:] + last_name[len_2-3:]
#   return str(temp_pass)

'My second attempt at writing this code:'

def password_generator(first_name, last_name):
    length_1 = len(first_name)
    length_2 = len(last_name)
    last_3_first_name = first_name[length_1-3:]
    last_3_last_name = last_name[length_2-3:]
    password = str(last_3_first_name) + str(last_3_last_name)
    return password

password_generator("Reiko", "Matsuki")

'''Up untill this point, as I ran the code, the only output was: Process finished with exit code 0.
this is because I havent stored the value or created a value to appear as an output, that is what I am doing next
by storing the function call into the variable "temp_password" '''

temp_password = password_generator("Reiko", "Matsuki")

''' still no output, going to print the variable "temp_password" '''

print(temp_password)

"output: ikouki, concatenation complete"

# !! --- Excercise 2 --- !!

def get_length(string):
  count = 0
  for letters in string:
    count += 1
  return count

#  !! --- Excercise 3 --- !!

"First iteration for loop with a check, been a while so syntax out of practice, how else is written"
# def letter_check(word, letter):
#   if letter == word:
#     return True
#   else False

"Correct syntax: "

def letter_check(word, letter):
  if letter == word:
    return True
  else:
      False


#    !! --- Excercise 4 --- !!

# 1st iteation of code:

def common_letters(string_one, string_two):
  in_common = []
  for letters in string_one:
    for items in string_two:
      if letters == items:
        in_common.append(letters)
  return in_common

print("Excercise 4, 1st attempt: "+ str(common_letters("banana", "cream")))

# 2nd iteration of code:

def common_letters(string_one, string_two):
  in_common = []
  if string_one[:] in string_two[:]:
    in_common.append(string_one[:])
  return in_common

print("Excercise 4, 2nd attempt: "+ str(common_letters("banana", "cream")))

# 3rd iteration of code:

def common_letters(string_one, string_two):
  in_common = []
  if string_one in string_two:
    in_common.append(string_one)
  return in_common

print("Excercise 4, 3rd attempt: "+ str(common_letters("banana", "cream")))

#4th iteration: Does not work.

# def common_letters(string_one, string_two):
#   in_common = []
#   if item in string_one and item in string_two:
#       in_common.append(item)
#       return in_common
#
#
#
# print("Excercise 4, 4th attempt: "+ str(common_letters("banana", "cream")))

# 5th iteraton of code:

def common_letters(string_one, string_two):
  in_common = []
  for letters in string_one:
    for items in string_two:
      if letters == items:
        in_common.append(letters)
  return in_common


# correct code:

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print("Excercise 4, 6th attempt, solution: " + str(common_letters("banana", "cream")))


#      !! ----- Excercise 5 ----- !!


def username_generator(first_name, last_name):
    length_1 = len(first_name)
    length_2 = len(last_name)

    if length_1 <= 3:
      first_half_of_name = first_name[:length_1]
    else:
      first_half_of_name = first_name[0:3]
    if length_2 <= 4:
      second_half_of_name = last_name[:length_2]
    else:
      second_half_of_name = last_name[0:4]
      user_name= str(first_half_of_name) + str(second_half_of_name)
    return user_name

print(str("user_name function output: ") + str(username_generator("Abdullah", "Durrani")))


def password_generator(user_name):
  new_name_0 = ""
  new_name_1 = ""
  for letters in user_name[:-1]:
      new_name_0 += letters
  for letters in user_name[-1]:
      new_name_1 += letters
  password = new_name_1 + new_name_0
  return password


print(password_generator("AbdDurr"))


#      !! ----- Good Quiz Question ----- !!

def tell_me_about_icecream(favorite_icecream):
  response = "My favorite icecream is" + favorite_icecream + "."
  print(response)

tell_me_about_icecream("chocolate")


'''This really stumped me because the 'print' is in the function, so the function's end is
to print response so I thought, it would print the word 'response' which I can see if flawed but the answers,
all had the word 'chocolate' in them and I thought the function call would not be able to to pull the word 'chocolate
because it's not in the function, and the 'print' is not in the function call, so I thought if this function is printed
it wold not be done so because of the function call, because the function call, althought has the word 'chocolate', it
doesn't or isn't being called to 'print' the function in the code, so the right answer of what the output would be
is: 'My favorite icecream ischocolate. Which makes sense, because there is no space in the string, inside the function,
between the 'is' and the quotation marks, but I just didn't think or know a function call can still work and print even
if the variable is coming after the function but the print is coming before the call, it's very tricky, 
and a good miss. '''



#      !! ----- Excercise 6 ----- !!

lines_by_lines = ('''I had a good day today.
I am hungry.
I think I'll go and get some  food today.''')

new_lines = lines_by_lines.split('\n')

print(new_lines)




