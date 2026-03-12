class Solution:
    def twoSum(self,num,target):
        n = len(num)
        arr = [(num[i], i) for i in range(n)]
        arr.sort()

        i = 0
        j = n-1

        while i<j:
            sum_val = arr[i][0] + arr[j][0]

            if sum_val == target:
                 return [arr[i][1] , arr[j][1]]

            elif sum_val > target:
                j -= 1

            else:
                i += 1
        return[]
       

        