n=int(input("Введіть трицифрове число:"))
if n>=100 and n<=999:
    a=n//100
    b=n//10%10
    c=n%10
    if a%2==0 and b%2==0 and c%2!=0:
        s1=a+b
        print("Сума:",s1)
    elif a%2==0 and c%2==0 and b%2!=0:
        s2=a+c
        print("Сума:",s2)
    elif c%2==0 and b%2==0 and a%2!=0:
        s3=c+b
        print("Сума:",s3)
    elif a%2==0 and b%2==0 and c%2==0:
        s4=a+b+c
        print("Сума:",s4)
    elif a%2==0 and b%2!=0 and c%2!=0:
        print("Сума:",a)
    elif b%2==0 and a%2!=0 and c%2!=0:
        print("Сума:",b)
    elif c%2==0 and b%2!=0 and a%2!=0:
        print("Сума:",c)
    elif c%2!=0 and b%2!=0 and a%2!=0:
        print("Сума:",0)
else:
    print("Помилка: число не є трицифровим")
