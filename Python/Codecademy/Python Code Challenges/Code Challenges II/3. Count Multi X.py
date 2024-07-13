# Write your count_multi_char_x function here:

# ! Code from previous challenge:
# def count_char_x(word, x):
#     counter = 0
#     for letters in word:
#         if letters == x:
#             counter += 1
#     return counter


# ! 1st attempt(ish), did not work.
# def count_multi_char_x(word, x):
#   counter = 0
#   delimiter = []
#   for letters in word:
#     delimiter.append(x)
#     if delimiter in word:
#       counter += 1
#     return counter

# def count_multi_char_x(word, x):
#     counter = 0
#     for letters in word: # ! This loop iterates over each letter in the string word. For word = "mississippi", it iterates over 'm', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i'.
#         if x in word: # ! On the first iteration, letters is 'm'. The condition if x in word: checks if x (e.g., "iss") is in the entire string word, not in letters. Since "iss" is in "mississippi", the condition is True.
#             word.split(x) # ! word.split(x) splits the word but does nothing with the result.
#             counter += 1 # ! counter += 1 increments counter by 1.
#     return counter # ! The loop then reaches return counter, which exits the function and returns counter.

# def count_multi_char_x(word, x):
#     counter = 0
#     for letters in word:
#         if letters == x: 
#             couner += 1
#         return counter # ! counter returns '0' because 'iss' is not in 'letters'

def count_multi_char_x(word, x):
    split_string = word.split(x)
    return split_string, len(split_string) - 1

        
  
  


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1