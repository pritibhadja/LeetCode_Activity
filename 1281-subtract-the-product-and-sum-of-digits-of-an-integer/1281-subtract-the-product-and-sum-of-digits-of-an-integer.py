class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum = 0
        product = 1

        while temp > 0:
            result = temp % 10
            temp //= 10

            sum += result
            product *= result

        return product - sum