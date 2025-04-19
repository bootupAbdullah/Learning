# a = [4, 0, 1, -2, 3]

# def make_the_duplicate_array(array):
#     #create an empty 'b' array to place the first value
#     b = []
#     # create a varaiable for the sum of the first parameters given
#     sum1 = 0 + array[0] + a[1]
#     # using append method place the sum of first paramater at index 0 of new list
#     b.append(sum1)
#     # return new list    
#     return b

# # call function while placing list 'a' as an argument and print the results.
# print(f" line 14: this is the duplicate_array_function: {make_the_duplicate_array(a)}")

# this successfully places the the desired sum of the first paramater at index 0
# of the new list now to consider edge cases like what is the list is longer or
# shorter than the current given example?


# # testing the len() method with given argument/array
# def make_the_duplicate_array_2(array):
#     # create a variable with for the length of the argument/array given
#     length_of_given_array = len(array)

#     # test to see if working correctly
#     print(f" line 27: this is the duplicate_array_2_function: {length_of_given_array}")

# # calling second function as test len() function
# make_the_duplicate_array_2(a)


# def make_the_duplicate_array_3(array):
#     length_of_given_array = len(array)

#     #testing to see how loop works with len()

#     for i in range(length_of_given_array):
#         if i == 0:
#             i = 0
#             for 

# def list_loop(array):
#     for i in array:
#         print(f"item index: {[i]}")

# list_loop(a)



# def test_range(array):
#     for i in range(len(array)):
#         print("Hello")


# test_range(a)

my_list = [5, 10, 15, 20]

# def make_pair(array):

#     for i in array:
#         print(range(len(array) - 2))
              
# make_pair(my_list)


def get_the_item(array):
    for i in array: 
        print(i)

print('this function prints the items in the list themselves: ') 
get_the_item(my_list)

def get_the_index(array):
    for i in range(len(array)):
        print(i)

print('this function prints the index of the items in the list: ') 
get_the_index(my_list)



