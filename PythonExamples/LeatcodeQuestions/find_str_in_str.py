def find_str_in_str(source: str, target: str) -> int:
    """find first source str in target str,
    as long as chars match, continue. else start from next char is source"""
    source_i = 0
    target_i = 0
    good_start = 0
    while target_i < len(target):
        while source[source_i] == target[target_i]:
            source_i += 1
            target_i += 1
            if source_i == len(source):
                return good_start
        good_start += 1
        target_i = good_start
        source_i = 0
    return -1



if __name__ == '__main__':
    print(find_str_in_str('ABC', 'AABCC'))
    print(find_str_in_str('ABC', 'AABACC'))
    print(find_str_in_str('ABC', 'AABABDAACCABC'))
