import numpy as np

# Define matrix A
A = np.array([[3, 4, 2],
              [8, 3, 5],
              [6, 6, 7]])
print("Matrix A:")
print(A)

# 1. Matrix Multiplication (A * A)
def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1,matrix2)

# 2. Matrix Transpose
def matrix_transpose(matrix):
    return np.transpose(matrix)

# 3. Matrix Determinant
def matrix_determinant(matrix):
    return  np.linalg.det(matrix)

# 4. Eigenvalues and Eigenvectors
def eigen(matrix):
    return np.linalg.eig(matrix)


# 1. Matrix Multiplication (A * A)
mat_mul = matrix_multiplication(A,A)
print("\nMatrix Multiplication (A * A):")
print(mat_mul)

# 2. Matrix Transpose
mat_trans = matrix_transpose(A)
print("\nMatrix Transpose (A^T):")
print(mat_trans)

# 3. Matrix Determinant
mat_det = matrix_determinant(A)
print("\nMatrix Determinant (det(A)):")
print(mat_det)

# 4. Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = eigen(A)
print("\nEigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
