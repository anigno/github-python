class Solution:

    def __init__(self):
        self.data = {}

    def is_palindrome_dynamic(self, s, start, end) -> int:
        t = s[start:end + 1]
        if t in self.data:
            return self.data[t]
        p = self.is_palindrome(s, start, end)
        self.data[t] = p
        return p

    def is_palindrome(self, s, start, end) -> int:
        m = (end - start) // 2
        i = 0
        while i <= m:
            if s[start + i] != s[end - i]:
                return -1
            i += 1
        return end - start + 1

    def longestPalindrome(self, s: str) -> str:
        start = 0
        best = 1
        best_pal = s[0]
        while start < len(s):
            end = 0
            while end < len(s):
                if end - start + 1 > best:
                    t = self.is_palindrome_dynamic(s, start, end)
                    if t >= best:
                        best = t
                        best_pal = s[start:end + 1]
                end += 1
            start += 1
        return best_pal

# qqqabccbaw
# s
# e
# 1
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('qqqabccbaw'))
