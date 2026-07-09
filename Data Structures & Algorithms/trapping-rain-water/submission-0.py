class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        Maxleft, Maxright = height[l], height[r]
        res = 0
        while l < r:
            if Maxleft < Maxright:
                l += 1
                Maxleft = max(Maxleft, height[l])
                res += Maxleft - height[l]
            else:
                r -= 1
                Maxright = max(Maxright, height[r])
                res += Maxright - height[r]
        return res

