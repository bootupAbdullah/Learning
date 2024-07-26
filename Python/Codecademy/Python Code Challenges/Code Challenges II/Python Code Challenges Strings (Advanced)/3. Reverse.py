# 1. Define the function to accept one parameter for the string
# 2. Create a new empty string to hold the reversed string
# 3. Loop through the input string by starting at the end, and working towards the beginning
# 4. Inside the loop, append the character at the current location to the new string we initialized earlier
# 5. Return the result


# def reverse_string(word):   
#     empty_string = ""
#     for letters in word:
#         empty_string += word[-1]
#     return empty_string

# print(reverse_string)   #! brain is half fried - I am calling the functin itself here withut a parameter. I am really struggling.

# def reverse_string(word):
#     empty_string = ""
#     for letters in word:
#         empty_string += word[-1] #! wanting to use [-1] a staring point but instead limiting scope to 'letter' at single index.
#     return empty_string

# print(reverse_string("countenance"))  #! first word that comes to mind when resolving parameter issue, appropos.
# output is: eeeeeeeeeee

# ! I can taregt the last letter - great - how do I target the last letter as the start of the loop? My old nemesis: The slice!
# ! it's going to take some trial and error in understanding where to place them.

# def reverse_string(word):
#     empty_string = ""
#     for letters in word[-1:0]
#         empty_string += letters
#     return empty_string

# print(reverse_string("countenance"))

# def reverse_string(word):
#     empty_string = ""
#     for letters in word[-1:0]: #! COLON!
#         empty_string += letters
#     return empty_string

# print(reverse_string("countenance"))

#! That doesn't seem to be working. There is not output. I am gonna have to brush up on my slicing, brb!

def reverse_string(word):
    empty_string = ""
    for letters in word[::-1]: # !so, the issue was that I was needing double ":" in the index brackets, the "-1" at the step value essentially tells python to go through the string in reverse.
        empty_string += letters
    return empty_string

print(reverse_string("countenance"))



