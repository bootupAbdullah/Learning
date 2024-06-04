# Challenge: Count Unique Letters
# Count the number of unique letters in a string. Ignore duplicates, counting each letter only once.

#  letter_count += 1

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def  unique_english_letters(word):
   all_letters = 0
   upper_case_letters = 0
   lower_case_letters = 0
   for letters in word:
    if letters.lower():
      lower_case_letters += 1
    if letters.upper():
      upper_case_letters += 1
    all_letters = upper_case_letters + lower_case_letters
    return all_letters


print(unique_english_letters("HeLlO"))
   


