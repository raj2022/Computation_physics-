import numpy as np

def LU_decomp(mat):
    matrix = mat.copy()
    row = len(matrix)
    col = len(matrix[0])
    A = []
    for i in range(row):
        for j in range(i,row):
            sum = 0.
            #print("j is ",j,"sum is",sum)
            if j>=1:    
                for k in range(i):
                    if i!=0:
                        sum = sum + matrix[i][k]*matrix[k][j]
            matrix[i][j] = matrix[i][j] - sum
            #print("matrix[",i+1,"][",j+1,"] is ",matrix[i][j],"sum was",sum)
            sum = 0.
            #print("j is ",j,"sum is",sum)
            for k in range(i):
                sum = sum + matrix[j][k]*matrix[k][i]
            if j!=i:
                matrix[j][i] = (matrix[j][i]- sum)/matrix[i][i]
                #print("matrix[",j+1,"][",i+1,"] is ",matrix[j][i],"sum was",sum)
    return matrix

def extract_LU(matrix):
    row = len(matrix)
    col = len(matrix[0])
    L = np.zeros((row,col))
    U = np.zeros((row,col))
    for i in range(row):
        L[i][i] = 1
        U[i][i] = matrix[i][i]
        for j in range(i+1,col):
            L[j][i] = matrix[j][i]
        for j in range(i):
            U[j][i] = matrix[j][i]
            
    return L,U

def inv_LU(mat):
    matrix = mat.copy()
    row = len(matrix)
    col = len(matrix[0])
    y = np.zeros((row,col))
    x = np.zeros((row,col))
    b = np.identity(row)

def solve_LU(mat,b_mat):
    matrix = mat.copy()
    b = b_mat.copy()
    row = len(matrix)
    col = len(matrix[0])
    y = np.zeros((row,1))
    x = np.zeros((row,1))
    
    for i in range(row):
        sum = 0.
        for j in range(i):
            if i>j:
                sum = sum + matrix[i][j]*y[j]
            if i==j:
                sum = sum + y[j]
        y[i] = b[i] - sum
    for i in range(row):
        sum = 0.
        for j in range(row-i,row):
            if row-1-i<j:
                #print("i ",row-1-i,"j ",j)
                sum = sum + matrix[row-1-i][j]*x[j]
        #print(sum)
        x[row-1-i] = (y[row-1-i]-sum)/matrix[row-1-i][row-1-i]
        
    return x

