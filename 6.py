pervoe = int(input())
vtoroe = int(input())
if pervoe<vtoroe: pervoe, vtoroe = vtoroe, pervoe
n = int(input())
while n != 0:
    if n>pervoe: vtoroe, pervoe = pervoe, n
    elif n>vtoroe: vtoroe = n
    n = int(input())
print(vtoroe)
