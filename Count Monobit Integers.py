class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1
        x = 1

        while x <= n:
            count += 1
            x = x * 2 + 1

        return count
