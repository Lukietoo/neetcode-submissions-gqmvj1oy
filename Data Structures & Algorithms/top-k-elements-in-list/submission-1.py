class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a counter for each integer in the array for nums.
        # store the each entry in the dictionary into a list
        # then return a list of the entries with a range from 0 to k
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        sorted_keys = sorted(counter, key=lambda x: counter[x], reverse=True)
        return list(sorted_keys[:k]) 
