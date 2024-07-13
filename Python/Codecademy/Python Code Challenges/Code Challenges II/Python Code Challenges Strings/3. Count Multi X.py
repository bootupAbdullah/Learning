# Write your count_multi_char_x function here:
# def count_multi_char_x(word, x):
#   counter = 0
#   delimiter = []
#   for letters in word:
#     delimiter.append(x)
#     if delimiter in word:
#       counter += 1
#     return counter

def count_multi_char_x(word, x):
    for letters in word:
        parts = word.split(x)
        occurences = len(parts) - 1
    return occurences




# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

