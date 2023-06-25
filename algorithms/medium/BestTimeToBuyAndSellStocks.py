from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = float('-inf')

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit


def getTestData():
    return [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array in getTestData():
        maximalProfit = solution.maxProfit(array)
        print("For prices " + str(array) + " maximal profit is: " + str(maximalProfit))
