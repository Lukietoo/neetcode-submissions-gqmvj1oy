class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        result = []
        pre = 1
        suf = 1
        for num in nums:
            prefix.append(pre)
            pre *= num
        for num in reversed(nums):
            suffix.append(suf)
            suf *= num
        suffix.reverse()
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result