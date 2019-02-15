# pip install numpy  #only once, 
import numpy as np
#import time
#import sys
def ListvsNumpy():
    a=np.array([2,3,4])
    print(a) # prints [2,3,4]
    print(a[0],a[1],a[2]) # prints 2 3 4
    # We have Python Lists , then why  numpy array
    # (1) Less Memory, List holds objects(14 bytes) array holds(4 byte) objects
    SIZE=100
    list1=range(SIZE)
    print(sys.getsizeof(5)*len(list1)) # 5 is any integer
    array=np.arange(SIZE)
    print(array.size*array.itemsize)
    #(2) Fast since numpy is vectorized
    SIZE=100000
    l1=range(SIZE)
    l2=range(SIZE)
    start=time.time()
    result=[(x+y) for x,y in zip(l1,l2)]
    print("python list took", time.time()-start)
    a1=np.arange(SIZE)
    a2=np.arange(SIZE)
    start = time.time()
    result=a1+a2
    print("numpy took", time.time()-start)
    #(3) Convenient
    #Two numpy lists can be added, subtracted, multiplied...
    a1*a2
    a1+a2
    a1[a1==0]=1
    a2/a1
    a1-a2
#########################################################
a1d=np.array([2,3,4])
b2d=np.array([
a2d=np.array([[2,3,4],[4,5,6],[2,1,3]])
a2d=np.array([[2,3,4],[4,5,6],[2,1,3]],dtype=np.float64)
a2dc=np.array([[2,3,4],[4,5,6],[2,1,3]],dtype=complex)
print("a1d dim=",a1d.ndim,",a2d dim=",a2d.ndim)
print("a1d itemsize=",a1d.itemsize,",a2d itemsize=",a2d.itemsize)
print(a2d.size,a2d.shape,type(a2d))
seq1=np.arange(1,10) # will not include 10
seq2=np.arange(1,10,2)
seq3=np.linspace(1,10,20) #linearly spaced 20 number
seq1.reshape(3,3)
a2d.ravel() # flatten
print(a2d.min(),a2d.max(),a2d.sum())
print(a2d.sum(axis=1),a2d.sum(axis=0)) # row(1) and column(0) sums
print(a2d.mean(),a2d.std(),np.sqrt(a2d))
print(np.dot(a2d,a2d)) # matrix multiplication
print("Row 2=",a2d[1,:],",Col 1=",a2d[:,0],",3,2=",a2d[2,1])
print("Last row=",a2d[-1],"Second Last col=",a2d[:,-2])
#########################################################
#ListvsNumpy()
    

