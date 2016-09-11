# LINEAR ALGEBRA WORKSHEET

import numpy as np 

# vectors, matrices, and dimensions (row x col)
A = np.matrix([[1, 2, 3], [2, 7, 4]]) # 2 x 3
B = np.matrix([[1, -1], [0, 1]]) # 2 x 2
C = np.matrix([[5, -1], [9, 1], [6, 0]]) # 3 x 2
D = np.matrix([[3, -2, -1], [1, 2, 3]]) # 2 x 3
u = np.array([6, 2, -3, 5]) # 1 x 4
v = np.array([3, 5, -1, 4]) # 1 x 4
w = np.array([[1], [8], [0], [5]]) # 4 x 1 (column vector)

# scalar
alpha = 6

print(A)
# [[1 2 3]
#  [2 7 4]]

print(B)
# [[ 1 -1]
#  [ 0  1]]

print(C)
# [[ 5 -1]
#  [ 9  1]
#  [ 6  0]]

print(D)
# [[ 3 -2 -1]
#  [ 1  2  3]]

print(u)
# [ 6  2 -3  5]

print(v)
# [ 3  5 -1  4]

print(w)
# [[1]
#  [8]
#  [0]
#  [5]]

#### 1. MATRIX DIMENSIONS

# 1.1) A is 2 X 3
print(A.shape) # (2, 3)

# 1.2) B is 2 x 2
print(B.shape) # (2, 2)

# 1.3) C is 3 x 2
print(C.shape) # (3, 2)

# 1.4) D is 2 x 3
print(D.shape) # (2, 3)

# 1.5) u is 1 x 4
print(u.shape) # (4,)

# 1.6) w is 4 x 1
print(w.shape) # (4, 1)


#### 2. VECTOR OPERATIONS

# 2.1) u + v
print(np.add(u, v))
# OR
print(u + v) # [ 9  7 -4  9]

# 2.2) u - v
print(np.subtract(u, v))
# OR
print(u - v) # [ 3 -3 -2  1]

# 2.3) a * u, (alpha = 6)
print(np.multiply(alpha, u))
# OR
print(alpha * u) # [ 36  12 -18  30]

# 2.4) u . v, (u dot v)
print(np.dot(u, v))
# OR
print(np.inner(u, v)) # 51

# 2.5) norm(u)
print(np.linalg.norm(u)) # 8.60232526704

# NOTE (to self):
# outer products (col vector x row vector = matrix)

# utranspose * v
# print(np.outer(u, v))
# [[ 18  30  -6  24]
#  [  6  10  -2   8]
#  [ -9 -15   3 -12]
#  [ 15  25  -5  20]]

# vtranspose * u
# print(np.outer(v, u))
# [[ 18   6  -9  15]
#  [ 30  10 -15  25]
#  [ -6  -2   3  -5]
#  [ 24   8 -12  20]]


#### 3. MATRIX OPERATIONS

# 3.1) A + C = NOT DEFINED (must be same dimension)
# print(np.add(A, C))
# ValueError: operands could not be broadcast together with shapes (2,3) (3,2) 

# 3.2) A - Ctranspose
print(np.subtract(A, C.transpose()))
# OR
print(A - C.transpose())
# [[-4 -7 -3]
#  [ 3  6  4]]

# 3.3) Ctranpose + 3 * D
print(np.add(C.transpose(), 3 * D))
# OR
print(C.transpose() + (3 * D))
# [[14  3  3]
#  [ 2  7  9]]

# 3.4) B * A
print(np.dot(B, A))
# OR
print(B * A)
# [[-1 -5 -1]
#  [ 2  7  4]]

# 3.5) B * Atranpose  = NOT DEFINED (B col dim != Atranspose row dim)
# print(B * A.transpose())
# ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# 3.6) B * C = NOT DEFINED (B col dim != C row dim)
# print(B * C)
# ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

# 3.7) C * B
print(C * B)
# [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]

# 3.8) B ** 4
print(B ** 4)
# OR
print(B * B * B * B)
# [[ 1 -4]
#  [ 0  1]]

# 3.9) A * Atranspose
print(A * A.transpose())
# [[14 28]
#  [28 69]]

# 3.10) Dtranspose * D
print(D.transpose() * D)
# [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]

