import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
da=a/2
db=b/2
A=(da,db)
B=(-da,db)
C=(-da,-db)
D=(da,-db)
print("Координати вершин прямокутника:",A,B,C,D)
