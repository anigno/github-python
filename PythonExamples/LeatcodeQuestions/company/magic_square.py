square1 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

def is_magic(square) -> bool:
    magic_sum = 0
    length = len(square)
    for i in square[0]:
        magic_sum += i

    row_sum = [0] * length
    diag1 = 0
    diag2 = 0
    for b in range(length):
        line = square[b]
        line_sum = 0
        for a in range(length):
            line_sum += line[a]
            row_sum[a] += line[a]
            if a == b:
                diag1 += line[a]
            if a == length - b - 1:
                diag2 += line[a]
        if line_sum != magic_sum:
            return False
    for row in row_sum:
        if row != magic_sum:
            return False
    if diag1 != magic_sum:
        return False
    if diag2 != magic_sum:
        return False
    return True

if __name__ == '__main__':
    print(is_magic(square1))
