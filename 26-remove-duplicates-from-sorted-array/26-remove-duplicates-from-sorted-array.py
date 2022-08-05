class Solution(object):
    def removeDuplicates(self, nums):
        test = ""
        count = 0
        
        for x in nums:
            #if we've alredy seen the number then continue
            if test == x:
                continue
            else:
                #set "test" to the current number
                test = x
                #element in nums array is set to "test" value
                nums[count] = test
                #count value increments to move onto next index
                count += 1
        return count