from math import factorial
n = int(input())
summa = 0
for i in range(1, n+1): summa += factorial(i)
print (summa)
