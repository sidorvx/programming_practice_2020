n = list(map(int, input().split()))
m = list(map(int, input().split()))
a = []
for i in n:
    if i in m: a.append(i)
print(sorted(a))