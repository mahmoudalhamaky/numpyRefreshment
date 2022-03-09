# just start
import numpy as np
# creating a list
num = [1,2,3,4,5] 
# show the type of the list
print (type(num))
numvec = np.array(num)
# show the type of array
print ("type of list is: ", type(numvec))
# create the list
num2 = [[1,2],[3,4],[3,5]]
print ("type of vector is: " ,num2)
numvec2 = np.array(num2)
print ("type of vesctor is: ",type(numvec2))
print ("length of list: ",len (num))
print ("length of vector: ",len (numvec2))