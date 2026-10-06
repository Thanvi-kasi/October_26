class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for i in range(1, n + 1):
            digit_sum = sum(map(int, str(i)))
            groups[digit_sum] = groups.get(digit_sum, 0) + 1

        maximum = max(groups.values())

        return sum(1 for count in groups.values() if count == maximum)
