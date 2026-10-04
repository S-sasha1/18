import math
a=float(input("Введіть a:"))
b=float(input("Введіть b:"))
h=float(input("Введіть крок h:"))
x=a
while x<=b+0.000001:
    y=math.sin(x)*math.cos(2*x)/3**(2*x-1)
    print("x=",round(x,4),"f(x)=",round(y, 6))
    x=x+h
