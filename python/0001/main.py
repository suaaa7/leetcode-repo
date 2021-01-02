class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        result = []
        for i, n in enumerate(nums):
            if hash_map.get(n) is None:
                hash_map[target-n] = i
            else:
                result = [hash_map[n], i]
        return result
