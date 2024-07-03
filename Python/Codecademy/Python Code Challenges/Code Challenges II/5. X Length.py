'''
5. X Length
Let’s use the split method in a different way. We need a new function that 
is able to accept two inputs: one for a sentence and another for a number. 
The function returns True if every single word in the sentence has a 
length greater than or equal to the number provided. These are the steps:

1. Define the function to accept two parameters, one string, and one number
2. Split up the sentence into an array of words
3. Loop through the words. If the length of any of the words is less than the provided number return False
4. If we made it through the loop without returning False then return True
'''

def x_length_words(sentence, number):
    split_sentence = sentence.split()
    for words in split_sentence:
        if len(words) >= number:
            return True
        else:
            return False 

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples marathons", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True