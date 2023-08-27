import math

def Tmatrix (matrix1, matrix2):
    #multiply two matrices
    
    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix2[0])):
            result[i].append(0)
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
        


# fun barycentric coords with cross product
def Bcoords(A, B, C, P):
    areaPCB = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])
    areaABC = (B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1])
    areaACP = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])

    try:
        u = areaPCB / areaABC
        v = areaACP / areaABC
        w = 1 - u - v
    except:
        u = v = w = -1
    return u, v, w


def smatrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def cofactor(matrix, i, j):
    return ((-1)**(i+j)) * determinante(smatrix(matrix, i, j))

def determinante(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for j in range(len(matrix)):
        det += matrix[0][j] * cofactor(matrix, 0, j)
    return det

# fun transpose
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# fun inverse
def inverse(matrix):
    det = determinante(matrix)
    # special case for 2x2 matrix:
    if len(matrix) == 2:
        return [[matrix[1][1]/det, -1*matrix[0][1]/det],
                [-1*matrix[1][0]/det, matrix[0][0]/det]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            cofactorRow.append(cofactor(matrix, r, c))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / det
    return cofactors

# fun subvector
def svector(vector, i):
    return vector[:i] + vector[i+1:]

# fun normal vector
def VectorN(vector):
    return math.sqrt(sum([x*x for x in vector]))

# fun cross product
def crossProduct(vector1, vector2):
    return [vector1[1]*vector2[2] - vector1[2]*vector2[1],
            vector1[2]*vector2[0] - vector1[0]*vector2[2],
            vector1[0]*vector2[1] - vector1[1]*vector2[0]]

def dotProduct(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

# Función para normalizar un vector
def normalize(v):
    norm = math.sqrt(sum(x * x for x in v))
    return [x / norm for x in v]