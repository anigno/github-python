def roman_to_int(s: str) -> int:
    used = list([False] * len(s))
    values_double = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900}
    values_single = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    value_sum = 0

    for roman in values_double:
        i = s.find(roman)
        if i >= 0:
            value_sum += values_double[roman]
            used[i] = used[i + 1] = True
    for roman in values_single:
        for a in range(len(s)):
            if s[a] == roman and not used[a]:
                value_sum += values_single[roman]
    return value_sum

if __name__ == '__main__':
    print(roman_to_int('III'))
    print(roman_to_int('LVIII'))
    print(roman_to_int('MCMXCIV'))
