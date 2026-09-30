class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        primes = []

        for x in range(2, 1000):
            is_prime = True
            for d in range(2, int(x ** 0.5) + 1):
                if x % d == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(x)

        prev = 0

        for num in nums:
            best = num

            for p in primes:
                if p >= num:
                    break
                if num - p > prev:
                    best = num - p

            if best <= prev:
                return False

            prev = best

        return True
