def remove_middle(my_list, start, end):
  return(my_list[:start] + my_list[end:])
 
print()
print("Remove Middle Function:")
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

print()
print("Reults Desrired:")
print([4, 23, 43])

print()
print("We Want '16' Gone.")

print()
print("How do we do that?")

def remove_middle(my_list, start, end):
  return(my_list[:start] + my_list[end+1:])
 
print()
print("Remove Middle Function, +1, which will include the index that is part of the middle:")
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))





 
