class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        order = sorted(range(n), key=lambda i: nums[i], reverse=True)
        bit = [0] * (n + 1)

        def add(i):
            i += 1
            while i <= n:
                bit[i] += 1
                i += i & -i

        def prefix(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(k):
            idx = 0
            step = 1 << (n.bit_length() - 1)
            while step:
                nxt = idx + step
                if nxt <= n and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]
                step >>= 1
            return idx

        for i in order:
            left_count = prefix(i)

            if left_count > 0:
                left = kth(left_count)
                if i - left >= 2:
                    ans += 1

            total = prefix(i + 1)
            active = prefix(n)

            if total < active:
                right = kth(total + 1)
                if right - i >= 2:
                    ans += 1

            add(i)

        return ans
