class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        next_non_zero_index = 0

        for n in nums:
            if n != 0:
                nums[next_non_zero_index] = n
                next_non_zero_index += 1

        for i in range(1, zero_count + 1):
            nums[-i] = 0
