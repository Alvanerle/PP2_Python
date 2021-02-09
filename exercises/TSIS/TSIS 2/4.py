#1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        tmp = 0
        for i in gain:
            tmp += i
            mx = max(mx, tmp)
        return mx