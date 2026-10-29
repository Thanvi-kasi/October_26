class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums):
            curr = 0
            best = 0
            for num in nums:
                curr = max(0, curr + num)
                best = max(best, curr)
            return best

        total = sum(arr)

        if k == 1:
            return kadane(arr) % MOD

        best_two = kadane(arr * 2)

        if total > 0:
            return (best_two + (k - 2) * total) % MOD

        return best_two % MOD
