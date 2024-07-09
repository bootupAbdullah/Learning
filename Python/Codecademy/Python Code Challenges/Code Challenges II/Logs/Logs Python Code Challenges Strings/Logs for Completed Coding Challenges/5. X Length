#Logs

X Length
Let’s use the split method in a different way. We need a new function that 
is able to accept two inputs: one for a sentence and another for a number. 
The function returns True if every single word in the sentence has a greater than or equal to the number provided.
These are the steps:

1. Define the function to accept two parameters, one string, and one number
2. Split up the sentence into an array of words
3. Loop through the words. If the length of any of the words is less than the provided number return False
4. If we made it through the loop without returning False then return True


# Initial attempt
# def x_length_words(sentence, x):
#     split_sentence = sentence.split()
#     for words in split_sentence:
#         if len(words) in split_sentence >= x:
#             return False
#         else:
#             return True

# # Uncomment these function calls to test your function:
# print(x_length_words("i like apples", 2))
# # should print False
# print(x_length_words("he likes apples", 2))
# # should print True

Issues Identified in Initial Attempt:
The condition if len(words) in split_sentence >= x was incorrect.
This condition was intended to check if the length of the word is greater than or equal to x, but it was syntactically incorrect and illogical.
It returned False prematurely and didn't check all words.

First Correction Attempt:
# Attempt to correct the logic
# def x_length_words(sentence, x):
#     split_sentence = sentence.split()
#     for words in split_sentence:
#         if len(words) >= x:
#             return False
#     return True

# # Uncomment these function calls to test your function:
# print(x_length_words("i like apples", 2))
# # should print False
# print(x_length_words("he likes apples", 2))
# # should print True


Issues Identified in First Correction Attempt:
The logic was still incorrect.
The condition if len(words) >= x would return False if any word was greater than or equal to x, which is the opposite of the intended logic.
The function needed to return False if any word was less than x.


Final Working Solution:
def x_length_words(sentence, x):
    split_sentence = sentence.split()  # Split the sentence into words
    for words in split_sentence:       # Loop through each word
        if len(words) < x:             # Check if the word length is less than x
            return False               # Return False if any word is shorter
    return True                        # Return True if all words are long enough

# Testing the final solution
print(x_length_words("i like apples", 2))  # should print True
print(x_length_words("he likes apples", 2))  # should print True
print(x_length_words("i like apples", 3))  # should print False
print(x_length_words("he likes apples", 6))  # should print False
Summary of Corrections:
Syntax and Condition Correction:

Changed if len(words) in split_sentence >= x to if len(words) < x.
Indentation Correction:

Ensured correct indentation levels for if statements and return statements.
Logic Correction:

Ensured the function checks if any word's length is less than x and returns False if found.
The function returns True only if all words meet the condition.
Final Code Explanation:
Split Sentence:

The sentence is split into a list of words using split().
Loop Through Words:

The function iterates over each word in the list.
Check Word Length:

For each word, it checks if the length of the word is less than x.
If a word is found that is shorter than x, the function returns False.
Return True:

If the loop completes without finding any word shorter than x, the function returns True.
This final solution meets the requirements and ensures that the function behaves as expected for the provided test cases.