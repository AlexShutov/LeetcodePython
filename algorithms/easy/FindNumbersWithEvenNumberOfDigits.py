from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for number in nums:
            if self.getNumberOfDigits(number) % 2 == 0:
                count += 1
        return count

    def getNumberOfDigits(self, number) -> int:
        digits = 0
        while number > 0:
            number, _ = divmod(number, 10)

            digits += 1
        return digits


def getTestData():
    return [
        [12, 345, 2, 6, 7896],
        [555, 901, 482, 1771]
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for array in getTestData():
        numberOfEvenDigits = solution.findNumbers(array)
        print("In array " + str(array) + " numbers with even number of digits: " + str(numberOfEvenDigits))
