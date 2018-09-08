import numpy as np
#
# data1 = [6, 7.3, 5.0, 7, 9]
# arr1 = np.array(data1)
# #print(arr1)
# data2 = [50, 50, 40, 4, 5, 3, 2]
# arr2 = np.array(data2)
# print(arr2)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.dtype)
# print(np.empty((2,1,3))) # 2 blocks 1 row 3 columns
# print(np.ones_like(arr2))
# print(np.eye(10))
# print(np.identity(10))
# print(id(arr1))
# print.arang(10,10)

# arr3 = np.array([1,2,3], dtype=np.float64)
# arr6 = arr3.astype(np.int64)
# print(arr6.dtype)
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr*arr)
# print(arr ** 0.5)

# arr = np.arange(10)
# print(arr)
# arr[5:9] = 12
# print(arr)
# arr_slice = arr[5:9]
# print(arr_slice)
# arr_slice[1] = 12345
# print(arr_slice)
# arr_slice[ : ] = 64
# print(arr_slice)

# arr2d = np.array([[1,2,3],[4,5,6],[6,7,8]])
# print(arr2d)
# print(arr2d[2][0])

# arr1d = np.array([[[1,2,3],[5,6,7]],[[3,4,5],[5,6,7]]])
# print(arr1d[0][1][0])
# old_value = arr1d.copy()
# arr1d[0][1][0] = 64
# print(arr1d[1,1])
# print(arr1d[ :1])

# names = np.array(['bob','joe','will','bob','will','Joe','Joe'])
# data = np.random.randn(7,4)  # blocks , rows, columns
# # print(data)
# # print(names[0])
# # print(names == 'will')
# print(data)
# print('\n')
# #print(data[names == 'will'])
# #print(data[names == 'bob',0:3])
# print(data[~(names == 'bob')]) #not
#
#
# arr = np.empty((8,4))
# print(arr)
# for i in range(8):
#     arr[i] = i
# print(arr)
# print(arr[[4,3,0,6]])
# print(arr[[-3,-5,-7]])


# arr = np.arange(32).reshape((8,4))
# print(arr)
# print(arr[[1,5,7,2],[0,3,1,2]]) #rows and columns
# print(arr[np.ix_([1,5,7,2],[0,3,1,2])]) # index values and arrangement of those values

# arr = np.arange(15).reshape((3,5))
# # print(arr.T)
# # print(arr)#tansposing arrays and swapping axes
# arr = np.random.rand(6,3)
# arrdot = np.dot(arr.T,arr)
# print(arrdot)

# arr = np.arange(16).reshape((2,2,4))
# print(arr)
# print(arr.T)

# points = np.arange(-5,5,0.01)
# xs,ys = np.meshgrid(points,points)
# import matplotlib.pyplot as plt
# z = np.sqrt(xs**2 + ys**2)
# print(z)

# xarr = np.array([1.1,1.2,1.3,1.4,1.5])
# yarr = np.array([2.1,2.2,2.3,2.4,2.5])
# cond = np.array([True,False,True,True,False])
# result = [(x if c else y)
#           for x,y,c in zip(xarr,yarr,cond)]
# print(result)
# result = np.where(cond,xarr,yarr)
# # print (result)
# # arr = np.random.randn(4,4)
# # print(arr)
# # np.where(arr>0,2,-2)
# # np.where(arr>0,2,arr)

# arr = np.random.rand(1, 10)
# print(arr.mean())
# print(np.mean(arr))
# print(np.sum(arr))
# print(arr.mean(axis=1))

# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr.cumsum(0))
# print(arr.cumprod(0))

# arr = np.random.rand(8)
# arr.sort()
# print(arr)
# arr = np.random.rand(1,10)
#
# arr.T.sort(1)
# print(arr)

# large_arr = np.random.randn(10)
# print(large_arr)
# print(len(large_arr))
# large_arr.sort()
# print(large_arr[int(0.01*len(large_arr))])
# names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
# print(np.unique(names))

# arr = np.arange(10)
# np.save('some_array',arr)
# arr = np.load('some_array.npy')
# print(arr)
#
# np.savez('array_arch.npz', a = arr, b = arr)
# arch = np.load('array_arch.npz')
# print(arch['b'])

# x = np.array([[1,2,3],[4,5,6]])
# y = np.array([[6,23],[-1,7],[8,9]])
# print(x.dot(y))
# print(np.dot(x,np.ones(3)))

# from numpy.linalg import inv,qr
# x = np.random.randn(5,5)
# mat = x.T.dot(x)
# # print(inv(mat))   # inverse of the matrix
# # print(mat.dot(inv(mat)))
# q,r = qr(mat) # quartiles
# print(r)

# nsteps = 1000
# draws = np.random.randint(0,2,size = nsteps)
# steps = np.where(draws>0,1,-1)
# walk = steps.cumsum()
# print(walk.min())
# print(walk.max())
# print((np.abs(walk)>=10).argmax())


nwalks = 5000
nsteps = 1000
draws = np.random.randint(0,2,size=(nwalks,nsteps))
steps = np.where(draws>0,1,-1)
walks = steps.cumsum(1)
print(walks)
hits30 = (np.abs(walks)>=30).any(1) # abs means absolute values  and changes the negative values to postive
print(hits30)
print(hits30.sum())
crossing_times = (np.abs(walks[hits30])>=30).argmax(1)
print(crossing_times.mean())
