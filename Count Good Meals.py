class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        MOD = 10**9 + 7
        freq = {}
        ans = 0

        for x in deliciousness:
            for p in range(22):
                target = (1 << p) - x
                ans += freq.get(target, 0)
            freq[x] = freq.get(x, 0) + 1

        return ans % MOD
