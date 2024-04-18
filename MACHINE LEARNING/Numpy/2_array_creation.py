import numpy as np
a1=np.array([[1,2,3],[4,5,6]],dtype='float')
print("array contents are:",a1)

a2=np.array((1,2,3))     #create array from tuple
print("array created from tuple is:",a2)

a3=np.zeros((16,173))     #creating a 16*173 array with all zeros
print("\nan array initialized with all:\n",a3)

one= np.ones((17,17))     #create  a 17*17 array with all ones
print("\nan array initialized with all ones:\n",one)

a4=np.full((17,17),-24.6782)  #creating a order= 17*17, requried number=-24.6782
print("\nan array initialized with all 4.78654 is:\n",a4)

a5=np.random.random((3,2))
print("\na random array:\n",a5)

a6=np.arange(0,40,5)
print("\na sequential array with steps of 5:\n",a6)

a7=np.arange (0,40,4.44)
print("\na sequential array wirh steps of 6:\n",a7)

a8=np.linspace(0,40,5)   #create a seque of 10 val in ramge 0 to 40
print("\na sequential array with 10 values between 0 and 5:\n",a8)  #both star and end point is displayed in res

#flatten array
a11=np.array([[1,2,3],[4,5,6]])
reshaped_array=a11.reshape((1,-1))

reshaped_array_2=a11.reshape((-1,1))
print("\noriginal array:\n",all)
print("reshaped array:\n",reshaped_array)
print("reshaped array:\n",reshaped_array_2)

a=np.array ([[1,2,3,4],
             [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
print("array contents are \n",a1)

#slicing array1
s1=a1[:2,:3]
print("array with first 2 rows and first 3 coloums:\n",s1)

s2=a1[:2,::2]
print("array with first 2 rows and alternative coloums:\n",s2)

a1=np.array([1,2,3,4,5,6])
print("adding 1 to every element:",a1+1)

print("substracting each element by 10:",a1-2)

print("multiplying each element by 10:",a1*10)

print("squaring each element:",a1**2)

a1 *=2  #a1=a1*2
print("double each elements of original array:",a1)

a2=np.array([[1,2,3],[3,4,5],[9,6,0]])
print("\noriginal array:\n",a2)
print("tranpose of array:\n",a2.T)









