class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 2
        right = x // 2

        while left <= right:
            middle = (left + right) // 2
            sq = middle * middle
            if sq == x:
                return middle
            if sq < x:
                left = middle + 1
            else:
                right = middle - 1

        return right


def getTestData():
    return [8, 4]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for number in getTestData():
        root = solution.mySqrt(number)
        print("root from " + str(number) + " is: " + str(root))
