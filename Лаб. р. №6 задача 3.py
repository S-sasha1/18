import math
a=float(input("Введіть a: "))
b=float(input("Введіть b: "))
h=float(input("Введіть h: "))
x=a
y=0.0
spisok=[]
while x<=b+0.000001:
    y=math.sin(x)*math.cos(2*x)/math.pow(3,2*x-1)
    spisok.append(y)
    x=x+h
print("Список значень:")
for y in spisok:
    print(round(y,6))
i_min=spisok.index(min(spisok))
i_max=spisok.index(max(spisok))
A=spisok[0:i_min+1]
B=spisok[i_max:len(spisok)]
print("Список A:")
for y in A:
    print(round(y,6),end=" ")
print()
print("Список B:")
for y in B:
    print(round(y,6),end=" ")
print()
print("Спільні елементи:")
for y in A:
    if y in B:
        print(round(y,6),end=" ")
