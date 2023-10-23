def lengthOfLongestSubstring(s: str) -> int:
    """max length of unique consecutive chars"""
    if not s:
        return 0
    start = 0
    end = 0
    best = 1
    letters_set = set()
    while end < len(s):
        # check if found existing letter in letters_set, if found. move the start index
        # to start new letters_set without the duplicate letter, removing letters from the set
        if s[end] in letters_set:
            # move start to previously found letter
            while s[start] != s[end]:
                letters_set.remove(s[start])
                start += 1
            start += 1
        letters_set.add(s[end])
        best = max(best, end - start + 1)
        end += 1
    return best

# abccbad
#    s
#    e
# 1
if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    # print(lengthOfLongestSubstring('abba'))
    # print(lengthOfLongestSubstring('abccbad'))
