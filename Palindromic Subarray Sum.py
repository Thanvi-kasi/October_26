from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        l, r = 0, -1
        d1 = [0] * n

        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)

            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
                k += 1

            d1[i] = k
            ans = max(ans, prefix[i + k] - prefix[i - k + 1])

            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        l, r = 0, -1
        d2 = [0] * n

        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)

            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
                k += 1

            d2[i] = k

            if k > 0:
                ans = max(ans, prefix[i + k] - prefix[i - k])

            if i + k - 1 > r:
                l, r = i - k, i + k - 1

        return ans
