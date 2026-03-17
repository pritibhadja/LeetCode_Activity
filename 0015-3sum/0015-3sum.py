class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        # n-2 sudhi j loop chalse
        for i in range(len(nums) - 2):
             
             #skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    #duplicate left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    #duplicate right
                    while left < right and nums[right] ==  nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return res


