class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum = 0 # initial sum is 0
        product = 1 # initial product is 1

        # Example = 234
        while temp > 0:
            result = temp % 10 # result = 4 # 23 % 10 =3
            temp //= 10 # 23 # 2

            sum += result # 0+4 = 4 # 4+3 = 7
            product *= result # 1*4 = 4 # 4*3 = 12

        return product - sum