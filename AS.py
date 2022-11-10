#Array Slicing
'''import numpy as np
x = np.array ([1,2,3,4,5,6,7])
print(x[1:5])
print(x[1])
print(x[:6])'''

'''x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

print(x[0][0])
print(x[0][1:])
print(x[2][1:3])
print(x[3,0:3])
print(x[2,1:3])'''

'''Create three array with three dimensions and put five elements in each array.
x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

Extract the values of these arrays
return 5 to 8
return 3 to 4
reverse the third array elements
return only first array'''

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


print( 2 to 3, 5 to 7, 10 t0 12) with the help of negative and positive indexing.'''


'''x = np.array([[[[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]]])

print( 4, 7 to 8 , 10 to 12, 13 to 16) with the help of positive and negative indexing

x = np.array([[[[1,2,3,4],[5,6,7,8],[9,10,11,12]]]])

find the number 5 to 6, 1 to 3, 9 to 12. with the help of negative and positive indexing.

x = np.array([[[4,6,3,9],[84,22,12,8],[36,89,56,12],[13,14,15,16]]])

find the the number which is divisible by 5 and 6.

Create an array with the five dimesions and array shape would be 5.'''

'''x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
print(x[0,0,0])
print(x[0,0,1:])
print(x[0,2,1:3])
print(x[0,3,1:3])
print(x[0,1,1:3])
print(x[0,3,2:])'''

If you want to select values from your array that fulfill certain conditions, it’s 
straight forward with NumPy.

For example, if you start with this array:'''

#Use of comparision operators with numpy arrays.

x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print(x[x < 5])
print(x[x > 12])
print(x[x >10])
print(x[x<=5])


Find the number which is divisible by 2
x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

z = x[x%2==0]	
print("Number is divisible by 2: ", z)


z = x[x%2!=0]
print("Number is not divisible by 2: ", z)

Use of Logical Operators with the numpy arrays.

you can select elements that satisfy two conditions using the & and | operators:

x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
z = x[(x>2) & (x < 11)]
z = x[(x>1) & (x<16)]
print(z)

x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
z = x[(x<2) | (x>16)]
#z = x[(x<1) | (x>16)]

#if we want to get answer in boolean value.

x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
z = (x>5) | (x == 5)
z = (x<5) | (x > 16)		#if we want to get boolean value.
z = (x<1) | (x > 16)
z = x[(x<1) | (x > 16)]
print(z)



'''You can also use np.nonzero() to select elements or indices from an array.

Starting with this array:'''

'''x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

z = np.nonzero(x''' 


#x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])

'''import numpy as np

x = np. array ([["abc",1,5,4],["xyz",5,6,9]],ndmin=6)
print(x)'''


NumPy Joining Array
Joining NumPy Arrays

Joining means putting contents of two or more arrays in a single array.

NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, 
along with the axis. If axis is not explicitly passed, it is taken as 0.'''

#Join two arrays
import numpy as np

x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.concatenate((x, y))

print(z)

#Join two 2-D arrays :

x = np.array([[1, 2], [3, 4]])		

y = np.array([[5, 6], [7, 8]])		#axis = 1 concatenate acording to column wise

z = np.concatenate((x, y), axis=1)

print(z)

'''x = np.array([[1, 2], [3, 4]])

y = np.array([[5, 6], [7, 8]])		#axis = 0 concatenate acording to row wise

z = np.concatenate((x, y), axis=0)

print(z)'''

'''Joining Arrays Using Stack Functions

Stacking is same as concatenation, the only difference is that stacking is done along a 
new axis.

We can concatenate two 1-D arrays along the second axis which would result in putting 
them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the 
axis. If axis is not explicitly passed it is taken as 0.
Example'''


x = np.array([1, 2, 3])

y = np.array([4, 5, 6])

z = np.stack((x, y), axis=1)

print(z)


'''Stacking Along Rows

NumPy provides a helper function: hstack() to stack along rows.
Example'''

x = np.array([1, 2, 3])

y = np.array([1, 2, 3])		# stack them horizontally with hstack():

z = np.hstack((x, y))

print(z)


'''Stacking Along Columns

NumPy provides a helper function: vstack()  to stack along columns.
Example'''

'''x = np.array([1, 2, 3])

y = np.array([1, 2, 3])		
								#You can stack them vertically with vstack
z = np.vstack((x, y))

print(z)'''


'''Stacking Along Height (depth)

NumPy provides a helper function: dstack() to stack along height, which is the same 
as depth.
Example'''


'''x = np.array([1, 2, 3])

y = np.array([1, 2, 3])

z = np.dstack((x, y))

print(z)'''




# Convert an array in five dimensions:
'''x = np.array([1,2,3,4,5],ndmin = 5)
print(x)'''

'''x = np. array ([["abc",1,5,4],["xyz",5,6,9]],ndmin=6)
print(x)'''



Python automatically converts one data type to another data type. This process does not
need any user involvement Python promotes the conversion of lower data type, for example, 
integer to higher data type says float to avoid data loss. This type of conversion or type 
casting is called UpCasting.'''


Data upcasting:

x = np. array ([2,1,5,4.0])
print(x)
print(x[1].dtype)

x = np. array (["abc",1,5,4.0])
print(x)
print(x.dtype)

x = np. array ([3,4,"abc","we","tr",8j,5.7])
print(x)
print(x.dtype)









'''x = np. array ([1,5,4,6,7,3j,5j])
print(x)
print(x.dtype)'''

'''x = np.arange(6)
print(x)'''


NumPy Splitting Array
Splitting NumPy Arrays

Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into 
multiple.

We use array_split() for splitting arrays, we pass it the array we want to 
split and the 
number of splits.
Example

Split the array in 3 parts:


x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 3)

print(y)

'''Note: The return value is an array containing three arrays.

If the array has less elements than required, it will adjust from the end accordingly.
Example

Split the array in 4 parts:
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 4)

print(y)'''

Note: We also have the method split() available but it will not adjust the 
elements 
when elements are less in source array for splitting like in example above, 
array_split() 
worked properly.

Split Into Arrays

The return value of the array_split() method is an array containing each of the 
split as an array.

If you split an array into 3 arrays, you can access them from the result just 
like any array element:


Access the splitted arrays:
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])

y = np.array_split(x, 3)

print(y[2])
print(y[1])
print(y[0])

Splitting 2-D Arrays

Use the same syntax when splitting 2-D arrays.

Use the array_split() method, pass in the array you want to split and the 
number of splits you want to do.
Example'''

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

y = np.array_split(x, 3)

print(y)






Split the 2-D array into three D arrays.
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

y = np.array_split(x, 3)

print(y)


'''The example above returns three 2-D arrays.

Let's look at another example, this time each element in the 2-D arrays contains 3 elements.
Example

Split the 2-D array into three 2-D arrays.
import numpy as np


The example above returns three 2-D arrays.

In addition, you can specify which axis you want to do the split around.

The example below also returns three 2-D arrays, but they are split along the row (axis=1).
Example

Split the 2-D array into three 2-D arrays along rows.
import numpy as np'''

'''x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

y = np.array_split(x, 3, axis=1)

print(y)'''

'''An alternate solution is using hsplit() opposite of hstack()
Example

Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
import numpy as np'''

'''x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

y = np.hsplit(x, 3)

print(y)'''

#Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().




What is cumsum in numpy

numpy.cumsum() function is used when we want to compute the cumulative 
sum of array elements over a given axis.

Examples:

import numpy as np 
x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x)
print(y)


x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x,axis=1)
print(y)


x = np.array([[2,4,6],[1,3,5]])
#print(x)
y = np.cumsum(x,axis=0)
print(y)'''


'''x = pd.DataFrame({"Name":["Abc","xyz","Awd"], "Marks": [78,67,92],"data 1": [8,7,6], "data 2":[9,5,4]})
#print(x)
z =x['data 1'].groupby(x['Name'])
#print(z)
print(z.mean())'''
