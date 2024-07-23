'''
2. Every Other Letter
For this next challenge, we are going to create a function that 
extracts every other letter from a string and returns the 
resulting string. There are a few different ways you can 
solve this problem. Here are the steps needed for one of the ways:

#! 1. Define the function to accept one parameter for the string
#! 2. Create a new empty string to hold every other letter from the input string
#! 3. Loop through the input string while incrementing by two every time
#! 4. Inside the loop, append the character at the current location to the new string we initialized earlier
#! 5. Return the new string

Create a function named every_other_letter that takes a 
string named word as a parameter. The function should 
return a string containing every other letter in word.

'''
# Write your every_other_letter function here:

def every_other_letter(word):
    new_word = word.split()
    new_string = " "
    for letters in range(0, len(new_word), 2):
        new_word.append(new_string)
    print(new_string)

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 
