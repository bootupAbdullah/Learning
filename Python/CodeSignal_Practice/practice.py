# Will create the first list that will be pulled from/dupliated in someway.

a = [1,2,3,4,5]

# define a function to take in arrays and apply desired functionality
def take_this_array(array):
    
    # we will need an empty list
    b = []

    # here is the formula I need to implement:
    # create a variable that conatins the length of the given array (argument)
    length_of_a = len(array)

    #I need to create a loop that will go through argument array and apply logic to each the corresponding indexes of array b

    i = 0
     
    # this produced an error: 'list assignment index out of range'
    # b[i] = 0 + array[0] + array[1]

    # alternative, save the 'sum' of the first equation needed to variable and append to array 'b':
    first_sum_for_b_array = array[i - 1] + array[i] + array[i + 1]
    b.append(first_sum_for_b_array)
    #TODO: try to figure out when the left or right should be 0
    
    # we will need to a return a list that contains ints made up from the specific math required
    #for list 'b'.  
    return b

    #testing out the 'length_of_a' varaible to see results.
    # print(length_of_a)


#calling function to see results for 'length_of_a':
print(take_this_array(a))