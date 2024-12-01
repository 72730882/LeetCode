class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n*2):
            i = i%n
            while stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return res