n = int(input())
a = dict()
for i in range(n):
    b = input().split()
    for j in b:
        a[j] = a.get(j, 0) + 1
max_val = max(a.values())
a_sort = [i for i, j in a.items() if j == max_val]
print(min(a_sort))
