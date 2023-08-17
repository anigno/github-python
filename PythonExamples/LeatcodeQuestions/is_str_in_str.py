# find first source str in target str
def find_str_in_str(source: str, target: str) -> int:
    sc = 0
    tc = 0
    good_start = 0
    while tc < len(target):
        while source[sc] == target[tc]:
            sc += 1
            tc += 1
            if sc == len(source):
                return good_start
        good_start += 1
        tc = good_start
        sc = 0
    return -1

if __name__ == '__main__':
    print(find_str_in_str('ABC', 'AABCC'))
    print(find_str_in_str('ABC', 'AABACC'))
    print(find_str_in_str('ABC', 'AABABDAACCABC'))
