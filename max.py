#Write your function here
def max_num(nums):
  default_max = nums[0]
  for number in nums:
    if number > default_max:
     return number
  
  # return default_max


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

