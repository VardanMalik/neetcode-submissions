class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for num in nums:
            count[num]+=1
        i = 0
        for color in range(3):
            for j in range(count[color]):
                nums[i] = color
                i+=1