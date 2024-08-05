class Solution:
    def mySqrt(self, x: int) -> int:
        return (int('{:.0f}'.format((x**(1/2))//1)))