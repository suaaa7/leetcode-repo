class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}

        for n in nums:
            if n not in hash_table:
                hash_table[n] = 1
            else:
                del hash_table[n]

        return list(hash_table.keys())[0]
