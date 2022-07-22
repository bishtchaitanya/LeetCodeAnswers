class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        sum = 0
        for i in range(len(nums)-1):
            sum = nums[i]
            for j in range(i+1,len(nums)):
                sum = sum + nums[j]
                if sum == target:
                    temp.append(i)
                    temp.append(j)
                sum = nums[i]
        return temp
