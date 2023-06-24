from typing import List


def getTestData():
    return [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1)
    ]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left + 1, right + 1]
            if currentSum < target:
                left += 1
            else:
                right -= 1

        return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array, number in getTestData():
        twoSumIndicies = solution.twoSum(array, number)

        print(
            "two sub items from " + str(array) + " equals to " + str(number) + " has indicies: " + str(twoSumIndicies))
