class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        self.subsets_helper(nums, solution, [], 0)
        return solution
    
    def subsets_helper(
        self,
        nums: List[int],
        solution: List[List[int]],
        current: List[int],
        index: int
    ) -> None:
        solution.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.subsets_helper(nums, solution, current, i + 1)
            current.pop()
