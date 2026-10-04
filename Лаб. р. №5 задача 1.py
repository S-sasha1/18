import math
x=float(input("Введіть значення x: "))
if x>=1:
    f=2/x+2.31*math.exp(2*x)
elif -1<x<1:
    arg=0.2*x+0.3
    f=math.asin(arg)
else: 
    f=math.cos(x+0.4*math.log(abs(x+0.2)))
print(f"f({x})={f:.6f}")
