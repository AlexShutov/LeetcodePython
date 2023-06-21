from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in history:
                secondIndex = history[complement]
                return [index, secondIndex]
            history[number] = index
        return []


def getTestData():
    nums1 = [2, 7, 11, 15]
    target1 = 9
    nums2 = [3, 2, 4]
    target2 = 6
    nums3 = [3, 3]
    target3 = 6
    return [(nums1, target1), (nums2, target2), (nums3, target3)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for nums, target in getTestData():
        sumValues = solution.twoSum(nums, target)
        print("nums: " + str(nums) + " target: " + str(target) + " " + str(sumValues))
