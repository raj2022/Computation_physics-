import numpy as np

#swap the row with max leftmost value to top
def swap_max(row_i,row,matrix):
    large = row_i
    for i in range(row_i,row):
        if matrix[large][row_i] <= matrix[i][row_i]:
            large = i
            matrix[large][row_i] = matrix[i][row_i]
    temp = matrix[row_i].copy()
    matrix[row_i] = matrix[large]
    matrix[large] = temp
    return matrix

def Gauss_Jordan(matrix):
    row = len(matrix)
    col = len(matrix[0])
    d = 0
    scalar_prod = 1
    det =1
    #swap zero rows to last
    zeros = []
    for i in range(row):
        if matrix[i][1] == 0:
            zeros.append(i)
            for j in range(col):
                if matrix[i][j] != 0:
                    zeros.remove(i)
                    break
    matrix = np.delete(matrix,zeros,0)   # remove the rows with only zeros
    for i in zeros:
        matrix = np.append(matrix,np.zeros(col).reshape(1,col),0)        #add the removed zero rows to the last
    for i in range(row):
        matrix_ini = matrix.copy()
        matrix = swap_max(i,row,matrix)
        if (matrix != matrix_ini).any():
            d = d+1
        if abs(matrix[i][i]) <= 1e-12:
                matrix[i][i] = 0
        scalar = matrix[i][i]            #add a scalar prod multiplier to use in calculating determinant
        if scalar == 0:
            break
        matrix[i] = matrix[i]/scalar
        #print("matrix after div with scalar is ",matrix)
        scalar_prod = scalar_prod*scalar
        for j in range(row):
            if j != i:
                scalar = matrix[j][i]
                #print("scalar[",j,"][",i, "]is ",scalar)
                #if scalar == 0:
                 #   print("breaking")
                  #  break
                matrix[j] = matrix[j] - (scalar*matrix[i])
            if abs(matrix[i][j]) <= 1e-12:
                matrix[i][j] = 0
            #print("matrix after subt is ",matrix)
    for i in range(row):
        det = det*matrix[i][i]
    det = pow(-1,d)*scalar_prod*det
    for i in range(row):
        for j in range(col):
            if abs(matrix[i][j]) <= 1e-12:
                matrix[i][j] = 0
    np.set_printoptions(precision=12,suppress=True)        
    #print(matrix)
    return matrix, det

def make_aug(matrix_A, matrix_b):
    row_A = len(matrix_A)
    col_A = len(matrix_A[0])
    row_b = len(matrix_b)
    col_b = len(matrix_b[0])
    if row_A == row_b:
        aug_matrix = np.append(matrix_A,matrix_b,axis=1)
    elif row_A == col_b:
        aug_matrix = np.append(matrix_A,np.reshape(matrix_b,(col_b,1)))
    else:
        raise Exception("unique soln probably not possible")
    return aug_matrix

def extract_inv(matrix):
    row = len(matrix)
    col = len(matrix[0])
    col_e = math.floor(col/2)      # column next to halfway
    matrix_e = np.reshape(matrix[:,col_e],(math.floor(col/2),1))     #reshape the extracted array from [1,n] to [n,1]
    col_e = col_e + 1
    for i in range(math.floor(col/2)-1):
        matrix_col = np.reshape(matrix[:,col_e],(math.floor(col/2),1))
        matrix_e = np.append(matrix_e,matrix_col,axis=1)             #append along axis=1, i.e, column wise
        #print("matrix_e is ",matrix_e)
        col_e = col_e + 1
    return matrix_e

