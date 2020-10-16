a = float(input())
n = int(input())


def power(a, n):
    b = 1
    for i in range(n):
        b *= a
    return(b)


print(power(a, n))
