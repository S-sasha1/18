import random
a="abcdefghijklmnopqrstuvwxyz"
t=input("Введіть повідомлення: ")
b=""
for ch in t:
    b=b+ch+random.choice(a)
print("Зашифровано:",b)
