import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.array([2,5,7,9,11,16,19,23,22,29,29,35,37,40,46])
y = np.array([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

x_train = x[:7]
y_train = y[:7]
x_test = x[7:]
y_test = y[7:]

print(x.shape[0])

x0 = 0
y0 = 0
x1 = 0
y1 = 0

for i in range(x_train.shape[0]):
    x0 = (x0 + x_train[i])
    y0 = (y0 + y_train[i])

x0 = x0/x_train.shape[0]
y0 = y0/y_train.shape[0]

for i in range(x_test.shape[0]):
    x1 = (x1 + x_test[i])
    y1 = (y1 + y_test[i])

x1 = x1/x_test.shape[0]
y1 = y1/y_test.shape[0]

a = (y1 - y0)/(x1 - x0)
b = y0 - x0*(y1 - y0)/(x1 - x0)

y_pt = a*x+b

x_predict = 46
y_predict = a*x_predict+b

plt.plot(x, y, 'ro')
plt.plot(x, y_pt)
print(y_predict)
plt.show()
