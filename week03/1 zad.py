n = list(map(int, input().split()))
a = 0
for i in range(1, len(n)-1):
    if n[i]>n[i-1] and n[i]>n[i+1]: a += 1
print(a)