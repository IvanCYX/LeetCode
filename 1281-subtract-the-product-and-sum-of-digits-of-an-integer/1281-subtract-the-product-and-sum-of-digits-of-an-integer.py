class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        i = 0
        
        while (n != 0):
            i = n % 10
            product *= i
            sum += i
            
            n //= 10
            
        return product - sum