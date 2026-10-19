class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @lru_cache(None)
        def dp(i, mask, tight, started):
            if i == len(s):
                return int(started)

            limit = int(s[i]) if tight else 9
            ans = 0

            for d in range(limit + 1):
                ntight = tight and (d == limit)

                if not started and d == 0:
                    ans += dp(i + 1, mask, ntight, False)
                elif not (mask & (1 << d)):
                    ans += dp(i + 1, mask | (1 << d), ntight, True)

            return ans

        return dp(0, 0, True, False)
