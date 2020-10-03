n = list(map(int, input().split()))
a = n.index(max(n))
b = n.index(min(n))
n[a], n[b] = n[b], n[a]
print(n)