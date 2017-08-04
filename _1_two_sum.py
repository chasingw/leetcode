class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictNums = {}
        # for index in range(len(fruits)):
        for index in range(len(nums)):
           needvalue = target - nums[index]
           if dictNums.__contains__(needvalue):
               return [dictNums[needvalue], index]
           else:
               dictNums[nums[index]] = index
