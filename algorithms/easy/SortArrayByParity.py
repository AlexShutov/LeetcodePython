from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted = nums.copy()
        writeIndex = 0
        for readIndex in range(len(sorted)):
            if sorted[readIndex] % 2 == 0:
                sorted[readIndex], sorted[writeIndex] = sorted[writeIndex], sorted[readIndex]
                writeIndex += 1

        return sorted

    def isEven(n):
        return n % 2 == 0


def getTestData():
    return [
        [3, 1, 2, 4],
        [0]
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array in getTestData():
        sortedArray = solution.sortArrayByParity(array)
        print("Array " + str(array) + " sorted by parity is: " + str(sortedArray))
