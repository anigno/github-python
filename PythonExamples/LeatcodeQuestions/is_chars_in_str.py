# verify all chars counts in source are in target counted
def is_chars_in_str(source: str, target: str):
    target_counters = {}
    for c in target:
        if c not in target_counters:
            target_counters[c] = 0
        target_counters[c] += 1
    for c in source:
        if c in target_counters:
            if target_counters[c] > 0:
                target_counters[c] -= 1
            else:
                return False
    return True

if __name__ == '__main__':
    print(is_chars_in_str('AABB', 'ABAB'))
    print(is_chars_in_str('AABB', 'ABAC '))
    print(is_chars_in_str('ABBCCAD', 'FDGSRATSFACADSBAHYCB'))
