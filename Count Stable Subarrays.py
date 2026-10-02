from typing import List

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        left = [0] * n

        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                left[i] = left[i - 1]
            else:
                left[i] = i

        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + (i - left[i] + 1)

        ans = []

        for l, r in queries:
            lo, hi = l, r
            p = r + 1

            while lo <= hi:
                mid = (lo + hi) // 2

                if left[mid] >= l:
                    p = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            length = p - l
            res = length * (length + 1) // 2
            res += pref[r + 1] - pref[p]

            ans.append(res)

        return ans
