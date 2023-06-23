from collections import Counter
from typing import List


def getTestData():
    return [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2]
    ]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        valuesCount = {}
        for number in nums:
            if number not in valuesCount:
                valuesCount[number] = 1
            else:
                count = valuesCount[number]
                valuesCount[number] = count + 1
        threshold = len(nums) // 2
        for number, count in valuesCount.items():
            if count > threshold:
                return number

        return -1

    def majorityElementCounter(self, nums: List[int]) -> int:
        valuesCount = Counter(nums)
        threshold = len(nums) // 2
        for number, count in valuesCount.items():
            if count > threshold:
                return number

        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for numbers in getTestData():
        number = solution.majorityElementCounter(numbers)

        print("majority element for numbers " + str(numbers) + " is " + str(number))
