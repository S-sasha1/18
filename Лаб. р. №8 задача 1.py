from array import*
import random
A = array('i',[])
for i in range(24):
    A.append(random.randint(1, 30))
print("Масив A:", A)
B = array('i', [])
for x in A:
    if x not in B:        
        B.append(x)
print("Масив B:", B)
suma=0
for x in B:
    suma=suma+x
seredne=suma/len(B)
print("Сума B:", suma)
print("Середнє арифметичне B:", seredne)
