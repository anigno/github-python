def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    start = 0
    end = 0
    best = 1
    letters = set()
    while end < len(s):
        if s[end] in letters:
            # move start to previously found letter
            while s[start] != s[end]:
                letters.remove(s[start])
                start += 1
            start += 1
        letters.add(s[end])
        best = max(best, end - start + 1)
        end += 1
    return best

# abccbad
#    s
#    e
# 1
if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring('abba'))
    print(lengthOfLongestSubstring('abccbad'))
