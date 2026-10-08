class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a = e = i = o = u = 1

        for _ in range(1, n):
            a, e, i, o, u = (
                e,
                a + i,
                a + e + o + u,
                i + u,
                a
            )

            a %= MOD
            e %= MOD
            i %= MOD
            o %= MOD
            u %= MOD

        return (a + e + i + o + u) % MOD
