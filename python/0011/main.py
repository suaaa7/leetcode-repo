class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        largest_area = 0
        prev_start_height = 0
        prev_end_height = 0

        while start < end:
            if height[start] < prev_start_height:
                start += 1
                continue
            if height[end] < prev_end_height:
                end -= 1
                continue

            current_area = min(height[start], height[end]) * (end - start)
            if current_area > largest_area:
                largest_area = current_area

            if height[start] < height[end]:
                prev_start_height = height[start]
                start += 1
            else:
                prev_end_height = height[end]
                end -= 1

        return largest_area
