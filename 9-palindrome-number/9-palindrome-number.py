class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = list(str(x))
        ref = num[::-1]
            
        if num == ref:
            return True
        else:
            return False