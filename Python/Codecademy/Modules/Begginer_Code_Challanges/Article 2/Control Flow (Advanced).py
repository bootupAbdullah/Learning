
# 3. Always False
'''
There are some situations that you normally want to avoid when programming using conditional statements. 
One example is a contradiction. This occurs when your condition will always be false no matter what value you pass into it. 
Let’s create an example of a function that contains a contradiction. It will contain a few steps:

Define the function to accept a single parameter called num
Use a combination of <, > and and to create a contradiction in an if statement.
If the condition is true, return True, otherwise return False. 
The trick here is that because we’ve written a contradiction, 
the condition should never be true, so we should expect to always return False.
'''

# Coding Question
'''
Create a function named always_false() that has one parameter named num.

Using an if statement, your variable num, and the operators >, and <, 
make it so your function will return False no matter what number is stored in num.

An if statement that is always false is called a contradiction. 
You will rarely want to do this while programming, 
but it is important to realize it is possible to do this.
'''

# Write your always_false function here:
def always_false(num):
    if num >= 0 and num <=0:
     return False
    return False
    
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
#should print False
print(always_false(1))
#should print False

'''
4. Movie Review
We want to create a function that will help us rate movies. Our function will split 
the ratings into different ranges and tell the user how the movie was based on the 
movie’s rating. Here are the steps needed:

1. Define our function to accept a single number called rating
2. If the rating is equal to or less than 5, return "Avoid at all costs!"
3. If the rating was less than 9, return "This one was fun."
4. If neither of the if statement conditions were met, return "Outstanding!"

Coding question
Create a function named movie_review() that has one parameter named rating.

If rating is less than or equal to 5, return "Avoid at all costs!". If rating is 
between 5 and 9, return "This one was fun.". If rating is 9 or above, return 
"Outstanding!"
'''
# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  if (rating >= 5 and 
    rating < 9):
      return "This one was fun."
  if (rating >= 9):
      return "Outstanding!"
  
print()
print()

# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
#should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

'''
5. Max Number
For the final challenge, we are going to select which number from three input 
values is the greatest using conditional statements. To do this, we need to check 
the different combinations of values to see which number is greater than the 
other two. Here is what we need to do:

1. Define a function that has three input parameters, num1, num2, and num3
2. Test if num1 is greater than the other two numbers
    3. If so, return num1
4. Test if num2 is greater than the other two numbers
    5. If so, return num2
6. Test if num3 is greater than the other two numbers
    7. If so, return num3
8. If there was a tie between the two largest numbers, then return "It's a 
tie!"

Coding question

Create a function called max_num() that has three parameters named num1, num2, 
and num3.

The function should return the largest of these three numbers. If any of two 
numbers tie as the largest, you should return "It's a tie!".
'''
# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"  

print()
print("Control Flow (Advanced)")
print("5. Max Number:")
print()
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
