class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}

        for n in nums:
            if n not in hash_table:
                hash_table[n] = 1
            else:
                hash_table[n] += 1

            if hash_table[n] > len(nums)/2:
                return n
