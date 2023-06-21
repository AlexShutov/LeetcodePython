from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        max = currSum
        i = 0
        j = k

        while j < len(nums):
            currSum -= nums[i]
            currSum += nums[j]
            if currSum > max:
                max = currSum
            i += 1
            j += 1

        return max / k


def getTestData():
    case1 = [1, 12, -5, -6, 50, 3]
    value1 = 4
    case2 = [5]
    value2 = 1
    case3 = [6, 8, 6, 8, 0, 4, 1, 2, 9, 9]
    value3 = 2
    return [(case1, value1), (case2, value2), (case3, value3)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for case in getTestData():
        values, number = case
        average = solution.findMaxAverage(values, number)
        print("values" + str(values) + " average items: " + str(number) + " is " + str(average))
