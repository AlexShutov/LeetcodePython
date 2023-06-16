from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                l = middle + 1
            else:
                r = middle -1
        return -1

    def searchRecursive(self, nums: List[int], target: int) -> int:

        def searchRecursive(left, right, target) -> int:
            if left > right:
                return -1
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle -1
            else:
                left = middle + 1
            return searchRecursive(left, right, target)

        return searchRecursive(0, len(nums) -1, target)





def getTestData():
    array1 = [-1,0,3,5,9,12]
    target1 = 9
    array2 = [-1,0,3,5,9,12]
    target2 = 2
    array3 = [5]
    target3 = 5
    return [(array1, target1), (array2, target2), (array3, target3)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for (array, target) in getTestData():
        index = solution.searchRecursive(array, target)
        isContained = "not contained" if index == -1 else " with index " + str(index)
        print("Is number " + str(target) + " contained in array " + str(array) + " : " + isContained)