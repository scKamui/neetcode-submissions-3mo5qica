class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nlist = {}  # val -> index

        for i, n in enumerate(nums):
            nlist[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nlist and nlist[diff] != i:
                return [i, nlist[diff]]
        return []
       

