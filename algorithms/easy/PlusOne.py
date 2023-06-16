from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            result = digits[i] + carry
            carry, digits[i] = divmod(result, 10)
        return digits if not carry else [1] + digits


def getTestData():
    number1 = [1,2,3]
    number2 = [4,3,2,1]
    number3 = [9]
    return [number1, number2, number3]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for number in getTestData():

        result = solution.plusOne(list(number))
        print("add 1 to " + str(number) + " is: " + str(result))


