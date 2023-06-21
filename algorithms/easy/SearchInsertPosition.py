from typing import List

def getTestData():
    return [
        ([1,3,5,6], 5),
        ([1,3,5,6], 2),
        ([1,3,5,6], 7)
    ]
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array, number in getTestData():
        position = solution.searchInsert(array, number)
        print("inserting " + str(number) + " in array " + str(array) + " at position: " + str(position))

