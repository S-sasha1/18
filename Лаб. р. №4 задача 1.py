import math
x=float(input("Введіть х"))
c=(7*x+math.cos(x)+math.sqrt(x))**(3*x-1)
z=math.exp(1.5*x)
y=(c/z)-math.log(abs(x))
print(y)
