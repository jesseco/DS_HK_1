Linear Algebra.py

def vectorMultiply(vector, value):
    return [x*value for x in vector]

def matrixTranspose(matrix):
     return [ [row[i] for row in matrix] for i in range(len(matrix[0]))]


def vectorMatrixMult(vector, matrix):
	row = 0
	col = 0
	for row in matrix
		for col in matrix
			vector[row] = matrix2 [row][col] = matrix[row][col] * vector[col]

			m1 = [[1,2],[3,4]]
			v1 = [1,2]
			