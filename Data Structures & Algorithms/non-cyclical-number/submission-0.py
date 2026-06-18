class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()
        x = n
        while x is not 1:
            if x in hash:
                return False

            hash.add(x)
            ans = 0

            while x:
                digit = x % 10
                digit = digit ** 2
                ans += digit
                x = x // 10
            x = ans
        return True

