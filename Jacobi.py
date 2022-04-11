import numpy as np

def Jacobi(matrix_A,matrix_b):
    mat = matrix_A.copy()
    b = matrix_b.copy()
    row = len(mat)
    col = len(mat[0])
    x_new = np.zeros(row)
    x_old = np.zeros(row)
    comp = np.ones(row)
    while(comp.sum()>=1e-4):
        #print(comp.any()>100)
        if comp.sum()<100.:
            x_old = x_new.copy()
        #print(comp)
            for i in range(row):
                sum = 0.
                for j in range(row):
                    if j!=i:
                        sum = sum + mat[i][j]*x_old[j]
                x_new[i] = (b[i] - sum)/mat[i][i]
            comp = np.abs(x_new - x_old)
            #print(x_new)
            #print(x_old)
            #print(comp)
        else:
            print("Solution not possible, method diverges")
            print("comp ",comp.sum())
            break
    print("comp ",comp.sum())
    return x_new

        