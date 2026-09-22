class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        nums = []
        nums.append([1])
        for i in range(numRows - 1):
            row = [1]
            for j in range(i):
                row.append(nums[i][j] + nums[i][j+1])
            row.append(1)
            nums.append(row)
        return nums
    