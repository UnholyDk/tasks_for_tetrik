import sys

def check_cell(i, j, matrix):
    available_values = set(range(1, 10))
    for k in range(9):
        available_values.discard(matrix[i][k])
    for k in range(9):
        available_values.discard(matrix[k][j])
    
    for p in range(i // 3 * 3, i // 3 * 3 + 3):
        for q in range(j // 3 * 3, j // 3 * 3 + 3):
            available_values.discard(matrix[p][q])
    
    if len(available_values) == 1:
        for x in available_values:
            return (True, x)
    return (False, None)


file_name = sys.argv[1]

count_zero = 0
coordinates_of_zeros = []

rows = open(file_name, 'r').readlines()
matrix = [[0] * 9 for i in range(9)]
for i, row in enumerate(rows):
    for j, x in enumerate(row.strip()):
        matrix[i][j] = int(x)
        if x == '0':
            count_zero += 1
            coordinates_of_zeros.append((i, j))

while count_zero != 0:
    flag = False
    for i in range(count_zero):
        x, y = coordinates_of_zeros[i]
        result = check_cell(x, y, matrix)
        if result[0]:
            matrix[x][y] = result[1]
            coordinates_of_zeros[i], coordinates_of_zeros[count_zero - 1] = \
                coordinates_of_zeros[count_zero - 1], coordinates_of_zeros[i]
            flag = True
            break
    count_zero -= flag

for row in matrix:
    print(''.join(map(str, row)))

