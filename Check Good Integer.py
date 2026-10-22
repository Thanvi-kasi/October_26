class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = str(n)
        digitSum = sum(int(d) for d in digits)
        squareSum = sum(int(d) ** 2 for d in digits)
        return squareSum - digitSum >= 50
