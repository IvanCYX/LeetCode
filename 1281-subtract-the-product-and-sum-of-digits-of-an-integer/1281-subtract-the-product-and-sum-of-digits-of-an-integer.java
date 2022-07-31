class Solution {
    public int subtractProductAndSum(int n) {
        int product = 1, sum = 0;
        int i;
        
        while(n != 0) {
            //use modulo to get the remainder
            i = n % 10;
            product *= i;
            sum += i;
            //divide by 10 to take advantage of truncation
            n /= 10; 
        }
        return product - sum;
    }
}