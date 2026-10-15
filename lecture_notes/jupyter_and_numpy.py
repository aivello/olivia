import numpy as np
'''
array > np.array([list1])
list1 + list2 = [5, 7, 9] # with the numpy array
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]
np.array([list1)]
print(list1 + list2)

# important functions:
# np.arrange(stop, start, step)
    # returns an array ranging from start, stop with a specified step size
        # np.arrage(1, 3, 2) 
        # *stop is excluded
# np.full(shape, fill_value) 
    # returns an array of specified shape and value
        # np.full(3, 7) = [7, 7, 7]

'''
--- Math Functions in Numpy ---
np.pi
np.e
np.sin(x)
np.exp (5, 2) # raises 5 to the power of 2
'''
