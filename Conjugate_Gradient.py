import numpy as np

from itertools import product

def Conjugate_Gradient(mat_A,mat_b,x_old,tol=1e-4):
    x_new = x_old.copy()
    r_new = mat_b - np.dot(mat_A,x_new)
    d_new = r_new
    r_new_norm = np.linalg.norm(r_new)
    
    num_iter = 0
    x = [x_new]
    while r_new_norm > tol:
        A_d_new = np.dot(mat_A,d_new)
        r_new_r_new = np.dot(r_new,r_new)
        
        alpha = r_new_r_new/np.dot(d_new,A_d_new)
        x_new = x_new + (alpha*d_new)
        r_new = r_new - (alpha*A_d_new)
        beta = np.dot(r_new, r_new) / r_new_r_new
        d_new = r_new + (beta * d_new)
        
        num_iter += 1
        #if(np.linalg.norm(r_new)>=r_new_norm):
        #    break
        x.append(x_new)
        r_new_norm = np.linalg.norm(r_new)
        if(num_iter>=30000):
            break
    print('Iteration: {} \t x = {} \t residual = {:.4f}'.format(num_iter, x_new, r_new_norm))    
    print('\nSolution: \t x = {}'.format(x_new))
        
    return np.array(x)
