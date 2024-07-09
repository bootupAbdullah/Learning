#testing find() function

# new_string = "people like to eat potato"

# people_location = new_string.find("people")
# like_location = new_string.find("like")
# hello_location = new_string.find("hello")
# to_location = new_string.find("to")


# print(people_location)
# print(like_location)
# print(hello_location)
# print(to_location)

'''

4. Substring Between

Here is a challenging problem. We need a function that is able to extract a 
portion of a string between two characters. The function will take three parameters 
where the first parameter is the string we are going to extract the substring from, 
the second input is the starting character of our substring and the third character 
is the ending character of our substring. Here are the steps we can use:

Define the function to accept three parameters, one string and two characters
find the starting index of our substring using the second input parameter
find the ending index of our substring using the third input parameter
If neither of the indices are -1, return the portion of the first input parameter 
string between the starting and ending indices (not including the starting and ending index)
If either of the indices are -1, that means the start or end of the substring 
didn’t exist in our string. Return the original string in this case.


'''

def substring_between_letters(word, start, end):
    if start in word and end in word:
        start_location = word.find(start) + 1
        end_location = word.find(end)
        return word[start_location:end_location]
    else:
        return word


print(substring_between_letters("exist", "e", "t"))

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


