def task9(n: int) -> None:
    matrix = []
    for i in range(n):
        matrix.append([None] * n)
    x, y = 0, 0
    dx, dy = 0, 1

    matrix[0][0] = 1
    number = 2
    while number <= n ** 2:
        if 0 <= x + dx <= n - 1 and 0 <= y + dy <= n - 1 and not matrix[x + dx][y + dy]:
            matrix[x + dx][y + dy] = number
            number += 1
            x += dx
            y += dy
        else:
            if dx == 1:
                dx = 0
                dy = -1
            elif dy == 1:
                dy = 0
                dx = 1
            elif dx == -1:
                dx = 0
                dy = 1
            elif dy == -1:
                dy = 0
                dx = -1

    for i in range(n):
        print(matrix[i])

    
# task9(10)
