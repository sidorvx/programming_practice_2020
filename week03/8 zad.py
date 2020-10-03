n = dict()
a = int(input())
for i in range(a):
    b = input().split()
    n[b[0]] = b[1]
    n[b[1]] = b[0]
c = input()
print(n[c])