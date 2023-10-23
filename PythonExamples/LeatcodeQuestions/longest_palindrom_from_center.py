class Solution:
    """find palindromes, best to look from center to sides. (two possibilities: abba or aba)"""

    def longestPalindromeFromCenter(self, s: str) -> str:
        """from any char pos n in s try to expend in both directions (n,n+1 as center is possible)"""
        length = len(s)
        sret = ''
        best = 0
        for a in range(length):
            if a < len(s) - 1 and s[a] == s[a + 1]:
                se = self.expend_even(s, a)
            else:
                se = self.expend_odd(s, a)
            if len(se) > best:
                best = len(se)
                sret = se
        return sret

    def expend_odd(self, s: str, i: int) -> str:
        j = 0
        sret = s[i]
        while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
            sret = s[i - j:i + j + 1]
            j += 1
        return sret

    def expend_even(self, s: str, i: int) -> str:
        j = 0
        sret = s[i:i + 1]
        while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i + j + 1]:
            sret = s[i - j:i + j + 2]
            j += 1
        return sret

# qqqabccbaw
# s
# e
# 1
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeFromCenter('qqqabccbaw'))
    print(s.longestPalindromeFromCenter('qqqabcbaw'))
