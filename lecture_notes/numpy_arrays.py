import numpy as np
'''
Difference between list and array: list is just a variable, an array has numpy's properties
How to make an array: np.array([])
NumPy functions: zeros, arrange, 
What happens in the following cases: adding a list to a list will combine the lists to make them longer, adding
an array to an array will add up the numbers in their corresponding positions
'''

'''
array = np.array([[2, 2, 2, 2]
                [2, 2, 2, 2]
                [2, 2, 2, 2]])

print(array.shape)
(3, 4)

np.shape prints a tuple of the the columns and rows of a nested list
'''

'''
for i in range(arr.shape[0]):
    print i

for i in range (arr.shape)

the np.shape outcome is a tuple that is iterable data
'''
arr = np.zeros((3, 3))
print(arr)