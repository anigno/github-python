def int_to_roman(num: int) -> str:
    values = [(1000, 'M'),
              (900, 'CM'),
              (500, 'D'),
              (400, 'CD'),
              (100, 'C'),
              (90, 'XC'),
              (50, 'L'),
              (40, 'XL'),
              (10, 'X'),
              (9, 'IX'),
              (5, 'V'),
              (4, 'IV'),
              (1, 'I')]
    roman = ''
    while num > 0:
        for k in range(len(values)):
            if num - values[k][0] >= 0:
                num -= values[k][0]
                roman += values[k][1]
                break
    return roman

if __name__ == '__main__':
    print(int_to_roman(3))
    print(int_to_roman(58))
    print(int_to_roman(1994))
"""
1994    1000    M
994     900     CM
94      90      XC
4       4       IV



"""
