class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers. l and r. start at the first index and last item
        # if numbers[l] + numbers[r] is less then increase l by 1
        # if greater then reduce r by 1
        # we just use a while loop i think when numbers[l] + numbers[r] does not equal value
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1
