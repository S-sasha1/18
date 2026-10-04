import math
a=float(input("Введіть a:"))
b=float(input("Введіть b:"))
h=float(input("Введіть крок h:"))
n=round((b - a)/ h)+1
for i in range(n):
    x=a+i*h
    y=math.sin(x)*math.cos(2*x)/3**(2*x-1)
    print("x=",round(x,4),"f(x)=",round(y,6))
