from typing import Dict

class Solution:
    def match_arrays(self, array1: str, array2: str) -> bool:
        """match exactly all chars in array1 and array2,
        add array1 to dict, count chars. check array2 chars, decrease chars count removing count==0 chars.
        check for empty dict"""
        # if not array1 or not array2:
        if len(array1) != len(array2):
            return False
        counter_dict: Dict[str, int] = {}
        # count chars in array1
        for c in array1:
            if c not in counter_dict:
                counter_dict[c] = 0
            counter_dict[c] += 1
        # match chars from array2
        for c in array2:
            if c not in counter_dict:
                return False
            counter_dict[c] -= 1
        # check results
        for k in counter_dict:
            if counter_dict[k] != 0:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    tests = [[None, ''],
             ['', ''],
             ['aabc', 'baac'],
             ['a', 'b'],
             ['a', 'a']]
    for test in tests:
        print(f'[{test[0]}] [{test[1]}] result={solution.match_arrays(test[0], test[1])}')
