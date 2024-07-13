'''
5. X Length
Let’s use the split method in a different way. We need a new function that 
is able to accept two inputs: one for a sentence and another for a number. 
#! The function returns True if every single word in the sentence has a greater than or equal to the number provided.
These are the steps:

1. Define the function to accept two parameters, one string, and one number
2. Split up the sentence into an array of words
3. Loop through the words. If the length of any of the words is less than the provided number return False
4. If we made it through the loop without returning False then return True
'''

# ! Did not work because after the loop is started, the conditional statment includes 
# def x_length_words(sentence, x):
#     split_sentence = sentence.split()
#     for words in split_sentence:
#         if len(words) in split_sentence >= x:
#             return False
#         else:
#             return True

# # Uncomment these function calls to test your tip function:
# print(x_length_words("i like apples", 2))
# # should print False
# print(x_length_words("he likes apples", 2))
# # should print True



# ! Did not work.
# def x_length_words(sentence, x):
#     split_sentence = sentence.split()
#     for words in split_sentence:
#         if len(words) >= x:
#             return False
#     return True

# ! Final iteration:

def x_length_words(sentence, x):
    split_sentence = sentence.split()  # Split the sentence into words
    for words in split_sentence:       # Loop through each word
        if len(words) < x:             # Check if the word length is less than x
            return False               # Return False if any word is shorter
    return True                        # Return True if all words are long enough

print(x_length_words("i like apples", 2))
# # should print False
print(x_length_words("he likes apples", 2))
# # should print True