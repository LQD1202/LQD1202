import numpy as np
import matplotlib
import matplotlib.pyplot as plt

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [2, 1, 3, 6, 9, 11, 13, 15, 17, 20]

plt.plot(A,B, 'ro')

A = np.array([A]).T
B = np.array([B]).T

C = np.ones((A.shape[0],1), dtype=np.int8)

D = np.concatenate((A, C), axis=1)

x = np.linalg.inv(D.transpose().dot(D)).dot(D.transpose().dot(B))

x0 = np.array([1, 12]).T
y0 = x0*x[0][0] + x[1][0]

plt.plot(x0,y0)
plt.show()
