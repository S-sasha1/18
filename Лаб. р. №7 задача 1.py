s = input("Введіть рядок: ")
print("Індекси цифр:")
for i in range(len(s)):
    if s[i].isdigit():
        print(i, end=" ")
print()
result=""
for c in s:
    if not c.isdigit():
        result=result+c
print("Рядок без цифр:", result)
