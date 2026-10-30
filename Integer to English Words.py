class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        thousands = [
            "", "Thousand", "Million", "Billion"
        ]

        def helper(n):
            if n == 0:
                return ""

            elif n < 20:
                return below_20[n]

            elif n < 100:
                return tens[n // 10] + (
                    " " + helper(n % 10) if n % 10 else ""
                )

            else:
                return below_20[n // 100] + " Hundred" + (
                    " " + helper(n % 100) if n % 100 else ""
                )

        result = []
        index = 0

        while num > 0:
            if num % 1000 != 0:
                part = helper(num % 1000)

                if thousands[index]:
                    part += " " + thousands[index]

                result.append(part)

            num //= 1000
            index += 1

        return " ".join(result[::-1])
