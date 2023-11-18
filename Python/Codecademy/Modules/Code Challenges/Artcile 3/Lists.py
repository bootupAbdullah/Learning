'''
1. Append Size
For the first code challenge, we are going to calculate the length of alist and then 
append the value to the end of the list. Here is what we need to do:

1. Define the function to accept one parameter for our list 
2. Get the length of the list
3. Append the length of the list to the end of the list
4. Return the modified list

Coding question
Create a function called append_size that has one parameter named my_list.

The function should append the size of my_list (inclusive) to the end of my_list. 
The function should then return this new list.

For example, if my_list was [23, 42, 108], the function should return [23, 42, 
108, 3] because the size of my_list was originally 3.
'''
'''
Attempt 1:
def append_size(my_list):
  my_list.count()
  return variable
  my_list.append(varibale)
  return my_list
'''
#Attempt 2:
# def append_size(my_list):
#   length_of_list = len(my_list)
#   return length_of_list
#   my_list.append(length_of_list)
#   return my_list
# output: 3

#Attempt 3:
#Write your function here
def append_size(my_list):
  length_of_list = len(my_list)
  my_list.append(length_of_list)
  return my_list

print()
print("Output for '1. Append Size' Challenge:")
#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# Solution given by Codecademy:
# def append_size(my_list):
#   my_list.append(len(my_list))
#   return my_list

'''
2. Append Sum
Let’s create a function that calculates the sum of the last two elements of a list 
and appends it to the end. After doing so, it will repeat this process two more 
times and return the resulting list. You can choose to use a loop or manually use 
three lines. Here are the steps we need:

1. Define the function to accept one parameter for our list of numbers
2. Add the last and second-to-last elements from our list together
3. Append the calculated value to the end of our list.
4. Repeat steps 2 and 3 two more times
5. Return the modified list

Coding question
Write a function named append_sum that has one parameter — a list named 
named my_list.

The function should add the last two elements of my_list together and append 
the result to my_list. It should do this process three times and then return 
my_list.

For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 
3, 5, 8].

'''
def append_sum(my_list):
  for i in range(3):
   num = my_list[-1] + my_list[-2]
   my_list.append(num)
  return my_list

print()
print("Output for '2. Append Sum' Challenge:")

print(append_sum([1, 1, 2]))
