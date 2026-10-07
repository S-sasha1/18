import numpy as np
from array import*
N=int(input("Введіть N: "))
F=np.zeros((N,N),dtype=int)
ch=51
for i in range(N):
    for j in range(N):
        F[i][j] = ch
        ch=ch+1
print("Матриця F:")
print(F)
A = array('i',[])
B = array('i',[])
for i in range(N):
    for j in range(N):
        if i+j < N-1:
            A.append(int(F[i][j]))
        elif i+j>N-1:
            B.append(int(F[i][j]))
print("Масив A (вище побічної):", A)
print("Масив B (нижче побічної):", B)
