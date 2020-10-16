def DiagonalMat(matrix, *, additional=None):
    if additional is not None:
        return sum([matrix[i][len(matrix)-i-1] for i in range(len(matrix))])
    else:
        return sum([matrix[i][i] for i in range(len(matrix))])


mat = []
size = int(input('Размер:'))
print('Матрица:\n')
for i in range(size):
    row = list(map(float, input().split()))
    mat.append(row)
print('1. Главная')
print('2. Побочная')
ans = input()
if ans == '1':
    print('Ответ: {}'.format(DiagonalMat(mat)))
elif ans == '2':
    print('Ответ: {}'.format(DiagonalMat(mat, additional=True)))
else:
    print('Boy next door')