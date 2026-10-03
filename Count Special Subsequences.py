class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        left = defaultdict(int)

        for r in range(4, n):
            q = r - 2

            for p in range(q - 1):
                a, b = nums[p], nums[q]
                g = gcd(a, b)
                left[(a // g, b // g)] += 1

            for s in range(r + 2, n):
                a, b = nums[s], nums[r]
                g = gcd(a, b)
                ans += left[(a // g, b // g)]

        return ans
