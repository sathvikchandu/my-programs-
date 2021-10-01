"""
x, y=input().split()
x= int(x)
y= float(y)
if(x%5==0):
    if(y>=x+0.5):
        print("{:.2f}".format(y-x-0.5))
    else:
        print(y)
else:
    print(y)
"""

import numpy as np

# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)

# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using " 
      "passed tuple:\n", arr)