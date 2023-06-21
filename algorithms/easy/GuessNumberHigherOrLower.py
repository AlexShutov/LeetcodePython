from typing import List

def getTestData():
    return [
        (2, 2),
        (10, 6),
        (1, 1),
        (2, 1)
    ]

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def __init__(self):
        self.pick = 0

    def guess(self, num: int) -> int:
        if num == pick:
            return 0
        if num > pick:
            return -1
        else:
            return 1

    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            check = self.guess(middle)
            if check == 0:
                return middle
            if check < 0:
                right = middle - 1
            else:
                left = middle + 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for n, pick in getTestData():
        solution.pick = pick
        guess = solution.guessNumber(n)
        print("picked value is: " + str(pick) + " max guessed number: " + str(n) + " and guessed number is: " + str(guess))

