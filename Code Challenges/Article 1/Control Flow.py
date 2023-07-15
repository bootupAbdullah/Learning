'''
4. Divisble by 10
To make things a bit more challenging, we are going to create a function that determines whether or not 
a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. 
Using this, we can complete this function in a few steps:

Define the function header to accept one input num
Calculate the remainder of the input divided by 10 (use modulus)
Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False

Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, 
and False otherwise. Consider using modulo operator % 
to check for divisibility.

'''

# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
   remainder = num % 10
   if remainder == 0:
      return True
   else:
      return False
print()
print("Answers for 'Divisble_by_ten' challenge:")
      

# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

'''
5. Not Sum To Ten
Finally, we are going to check if the summation of two inputs does not equal ten. 
Our function will accept two inputs and add them together. If the two numbers added together are not equal to ten, 
then we will return True, otherwise, we will return False. Here is what we need to do:

Define the function to accept two parameters, num1 and num2
Add the two parameters together
Test if the result is not equal to 10
If the sum is not equal, return True, otherwise, return False

Create a function named not_sum_to_ten() 
that has two parameters named num1 and num2.

Return True if num1 and num2 do not sum to 10. 
Return False otherwise.
'''

# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
   sum = num1 + num2
   if sum != 10:
     return True
   else:
     return False
print()
print("Answers for 'not_sum' challenge:")
   
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False