class Solution(object):
    def plusOne(self, digits):
        #initialize empty tem pvar
        s = ""
        for i in digits:
            #iterate over each element, convert to string and append to the previous
            s = s + str(i)
            #at the end, convert the whole number to int, +1
            #then convert the whole thing to a string
        a = str(int(s) + 1)
        return list(a)
            
        