class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2

        for x in range(1, n + 1):
            if x * x == total:
                return x

        return -1
