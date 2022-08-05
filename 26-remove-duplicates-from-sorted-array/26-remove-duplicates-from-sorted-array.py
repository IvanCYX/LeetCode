class Solution(object):
    def removeDuplicates(self, nums):
        test = ""
        count = 0
        
        for x in nums:
            if test == x:
                continue
            else:
                test = x
                nums[count] = test
                count += 1
        return count