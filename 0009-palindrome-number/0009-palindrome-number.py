class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
             return (False)

        d = 0
        r = 0
        while(x // (10**d) != 0):
            r=(r * 10) + (x // (10**d) % 10)
            d += 1
        return(x == r)


