class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n % 3 == 0:
            return pow(3, n // 3)
        return pow(3, n // 3 - 1) * 4 if n % 3 == 1 else pow(3, n // 3) * 2
