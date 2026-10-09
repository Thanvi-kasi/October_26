class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for x in range(low, high + 1):
            s = str(x)
            n = len(s)

            if n % 2 != 0:
                continue

            mid = n // 2

            if sum(int(c) for c in s[:mid]) == sum(int(c) for c in s[mid:]):
                count += 1

        return count
