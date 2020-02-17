class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def pre(digits, fact, k):
            if not digits:
                return ""

            fact = fact // len(digits)
            idx = int(math.ceil(k/fact))
            d = digits[idx-1]

            digits.remove(d)

            return str(d) + pre(digits, fact, k % fact)


        return pre(list(range(1, n+1)), math.factorial(n), k)
