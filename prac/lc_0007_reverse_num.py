class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            sign = '-'
            s = s[1:]
        else:
            sign = ''
        ans = int(sign + s[::-1])
        if (ans < -2**31) or (ans > 2**31 - 1):
            return 0
        else:
            return ans
