class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m = len(nums)//2
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[m+i])
        return output
