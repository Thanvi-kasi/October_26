class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            mn = mx = nums[i]

            for j in range(i, n):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                ans += mx - mn

        return ans
