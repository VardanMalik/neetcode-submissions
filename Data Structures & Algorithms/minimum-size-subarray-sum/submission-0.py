class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, SUM = 0,0
        res =float("inf")
        for r in range(len(nums)):
            SUM+=nums[r]
            while SUM>=target:
                res = min(res, r-l+1)
                SUM-=nums[l]
                l+=1
        return 0 if res==float("inf") else res
