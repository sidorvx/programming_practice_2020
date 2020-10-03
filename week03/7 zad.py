n = int(input())
a = set()
for i in range(n):
    s = input().replace('\n', ' ').split()
    for j in s:
        a.add(j)
print(len(a))