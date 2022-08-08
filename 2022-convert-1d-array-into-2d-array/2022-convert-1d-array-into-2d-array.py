class Solution(object):
    def construct2DArray(self, original, m, n):
        #check if array can be converted to 2D array
        if (len(original) != m*n):
            #if not, return empty array
            return []
        
        newArray = []
        #range(start, stop, step)
        for i in range (0, len(original), n):
            if original[i:i+n] != []:
                newArray.append(original[i:i+n])
                
        return newArray
        
        