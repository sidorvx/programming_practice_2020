n = list(map(int, input().split()))
a = 0
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] == n[j]: a += 1
print(a)