# Your code below: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")

print(preferred_size)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]

print(customer_data)

#Chani switching to regular shipping
customer_data[2][2] = False

#Removing Ben's shipping information
customer_data[1].remove(False)

"""""
print value for test
print(customer_data[1][2])
This prints to False - so I have identified the right index
issue was or seemed to be that I was identifying the exact index id of the False statement - as in going one step further then identifying the sublist [1](Ben is 1, with Ainsley being 0), I also identified the indce number of False, which would be .customer_data[1][2] - this would not work wih .remove(False) but .customer_data[1].remove(False) - worked.
"""

#Final Step
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

