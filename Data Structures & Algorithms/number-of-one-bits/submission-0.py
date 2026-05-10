class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 0
        for i in range(32):
            if (1 << i) & n:
                x += 1
        return x
