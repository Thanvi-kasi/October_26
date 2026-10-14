class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b = 0, 1

        while True:
            c = a + b
            total = a + b + c

            if total == n:
                return True

            if total > n:
                return False

            a, b = b, c
