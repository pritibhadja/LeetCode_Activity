class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = n - 1

            # abs = difference ne possitive bnave
            while j < k:
                result_sum = nums[i] + nums[j] + nums[k]
                
                # distance of current ans = abs(result_sum - target
                # distance of best ans = abs(closest - target)
                # abs = convert neg to pos
                if abs(result_sum - target) < abs(closest - target):
                    closest = result_sum

                if result_sum == target:
                    return result_sum

                elif result_sum < target:
                    j += 1

                else:
                    k -= 1

        return closest

