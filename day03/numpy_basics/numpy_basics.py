import numpy as np


#=================================Block 1=================================#
a = np.array([1, 2, 3, 4, 5])

#type(a)
#print(f'{a.shape, a.ndim, a.size, a.dtype}')

'''
a + 10
a * 2
a ** 2
a / 2
'''

b = np.array([10, 20, 30, 40, 50])

#print(a*b)

#=================================Block 2=================================#

#A = np.array([
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#])

'''
A.shape
A.ndim
A[0]
A[:, 0]
A[1, 2]
A[:2, :2]
'''

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

'''
A + B
A * B
A @ B
'''

#=================================Block 3=================================#

#x = np.arange(1, 101)

'''
sum(x)
sum(x)/len(x)
min(x) max(x)
x[(x>30)&(x<60)]
x**2
'''


#x = np.arange(0, 11)

#y = x^2 + 2x + 1

#y = x**2 + 2*x + 1
#print(y)

#=================================Block 4=================================#

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 7])

def avg(x):
    return sum(x)/len(x)

#print(avg(x),avg(y))
#print(max(y))
#print(x[np.argmax(y)])
#print(y-x)
#print(avg(y-x))
