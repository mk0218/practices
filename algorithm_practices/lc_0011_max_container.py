class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 1, len(height)
        sorted_lines = sorted(((h, i+1) for i, h in enumerate(height)), reverse=True)
        max_area = 0
        done = set()
        for y, x in reversed(sorted_lines[1:]):
            max_area = max(max_area, max(x-left, right-x) * y)
            done.add(x)
            while left in done:
                left += 1
            while right in done:
                right -= 1

        return max_area
