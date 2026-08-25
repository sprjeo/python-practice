import numpy as np
import matplotlib.pyplot as plt


#=================================Block 1=================================#
a = np.array([3, 7, 2, 9, 12, 5, 8, 4, 15, 6])

def task_1(a):
    print(np.sum(a))
    print(np.mean(a))
    print(np.min(a),np.max(a))
    print(np.argmin(a), np.argmax(a))
    return
#task_1(a)

#print(a[a>7])
#print(a[a%2==0])
#print(a[(a%2==0)&(a>6)])
#print(a[(a>=5)&(a<=12)])

#=================================Block 2=================================#

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

def task_2(A):
    print(A.shape) #num of rows num of columns 
    print(np.sum(A)) #sum of all values  
    print(np.sum(A, axis=0)) #sum by columns
    print(np.sum(A, axis=1)) #sum by rows
#task_2(A)

def task_3(A):
    for x in range(A.shape[1]):
        print(f'sum of {x+1} column {np.sum(A,axis=0)[x]}, it\'s mean: {np.mean(A,axis=0)[x]}, it\'s max: {np.max(A,axis=0)[x]}')
    for x in range(A.shape[0]):
        print(f'sum of {x+1} row {np.sum(A,axis=1)[x]}, it\'s mean: {np.mean(A,axis=1)[x]}, it\'s max: {np.max(A,axis=1)[x]}')


#task_3(A)

#=================================Block 3=================================#

x = np.array([0, 1, 2, 3, 4, 5]) #time
y = np.array([1.2, 2.1, 4.2, 8.8, 15.9, 26.1]) #value

def task_4(x,y):
    print(f'y mean: {np.mean(y)}, min: {np.min(y)}, max: {np.max(y)}')
    print(f'y reaches it\'s max at x = {x[np.argmax(y)]}')
    print(f'y values above average: {y[y>np.mean(y)]} corresponding x-values: {x[np.where(y>np.mean(y))]}')


#task_4(x,y)

#=================================Block 4=================================#

plt.plot(x, y)
plt.title('data visualization')
plt.xlabel('time')
plt.ylabel('value')
plt.grid(True)
plt.show()

plt.scatter(x,y)
plt.title('data visualization')
plt.xlabel('time')
plt.ylabel('value')
plt.grid(True)
plt.show()