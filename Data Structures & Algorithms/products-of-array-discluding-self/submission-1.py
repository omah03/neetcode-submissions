from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1] * (len(nums))
        output = [1] * (len(nums))
        suffix = 1

        for i in range(1,len(nums)):
            output[i] = nums[i-1] * output[i-1]
        
        for j in range(len(nums)-1,-1,-1):
            output[j] = output[j] * suffix
            suffix = suffix * nums[j]
        return output





            
        
        