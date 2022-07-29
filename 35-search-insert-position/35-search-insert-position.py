class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target in nums:
            return nums.index(target)
        if target > nums[-1]:
            return len(nums)
        for i in range (1, len(nums)):
            if(nums[i - 1]) < target < nums[i]:
                return i;