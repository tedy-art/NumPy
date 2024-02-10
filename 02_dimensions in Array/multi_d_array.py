import numpy as np

x = np.array(42)
y = np.array([1,2,3,4,5])
z = np.array([[1,2,3],[4,5,6]])
w = np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])
print(x.ndim)
print(y.ndim)
print(z.ndim)
print(w.ndim)