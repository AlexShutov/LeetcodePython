from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            middle = int((l + r) / 2)
            currSquare = middle * middle
            if currSquare == num:
                return True
            if currSquare > num:
                r = middle - 1
            else:
                l = middle + 1
        return False

def getTestData():
    return [ 14, 16]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for value in getTestData():
        print(solution.isPerfectSquare(value))



