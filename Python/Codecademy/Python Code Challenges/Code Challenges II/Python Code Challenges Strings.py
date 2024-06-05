# Challenge: Count Unique Letters
# Count the number of unique letters in a string. Ignore duplicates, counting each letter only once.

#  letter_count += 1

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def  unique_english_letters(word):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  count = 0
  for word in letters:
    if letters in word:
      count += 1
  return count
 
  
  #  all_letters = 0
  #  upper_case_letters = 0
  #  lower_case_letters = 0
  #  for letters in word:
  #   if letters == letters.lower():
  #     lower_case_letters += 1
  #   if letters == letters.upper():
  #     upper_case_letters += 1
  #     all_letters = upper_case_letters + lower_case_letters
  #  return ("\n" + "Lower Case Letters:" + str(lower_case_letters) + "\n" + "\nUpper Case Letters:" + str(upper_case_letters) + "\n" + "\nAll Letters:" + str(all_letters))


print(unique_english_letters("HellO"))
   


