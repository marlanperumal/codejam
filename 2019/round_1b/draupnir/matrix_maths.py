from numpy.linalg import inv
import numpy as np

X = np.array([
    [2**(i // j) for j in range(1, 7)] for i in range(1, 7)
])
Xi = inv(X)
Xil = [
    [i for i in row] for row in Xi.tolist()
]

print(X)
print(Xi)
print(Xil)
print(np.dot(X, np.array(Xi)))
