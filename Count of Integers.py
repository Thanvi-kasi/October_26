class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def solve(s):
            n = len(s)
            dp = [[0] * (max_sum + 1) for _ in range(2)]
            dp[1][0] = 1

            for ch in s:
                digit = int(ch)
                ndp = [[0] * (max_sum + 1) for _ in range(2)]

                for tight in range(2):
                    limit = digit if tight == 1 else 9

                    for total in range(max_sum + 1):
                        ways = dp[tight][total]
                        if ways == 0:
                            continue

                        for d in range(limit + 1):
                            new_sum = total + d
                            if new_sum > max_sum:
                                break

                            new_tight = 1 if tight == 1 and d == digit else 0
                            ndp[new_tight][new_sum] = (
                                ndp[new_tight][new_sum] + ways
                            ) % MOD

                dp = ndp

            ans = 0
            for tight in range(2):
                for total in range(min_sum, max_sum + 1):
                    ans = (ans + dp[tight][total]) % MOD

            return ans

        def decrement(s):
            digits = list(s)
            i = len(digits) - 1

            while digits[i] == '0':
                digits[i] = '9'
                i -= 1

            digits[i] = str(int(digits[i]) - 1)
            return ''.join(digits).lstrip('0') or '0'

        return (solve(num2) - solve(decrement(num1))) % MOD
