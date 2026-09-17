from math import*
def ob_z(x, y, a):
    c1=5.126*log10(abs(3.3+x**2))
    c2=(x+y**3)**(1/6)
    c3=4*tan(a+x)
    s=c1+c2-c3
    return s
x = float(input("Введіть x"))
y = float(input("Введіть y"))
a = float(input("Введіть a"))
r=ob_z(x, y, a)
print("Z=",r)
