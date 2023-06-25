from typing import List


def getTestData():
    return [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3]
    ]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftToRight = [1]
        for i in range(1, len(nums)):
            product = leftToRight[-1] * nums[i - 1]
            leftToRight.append(product)
        rightToLeft = [1]
        for i in reversed(range(0, len(nums) - 1)):
            product = rightToLeft[0] * nums[i + 1]
            rightToLeft.insert(0, product)
        result = []
        for i in range(len(leftToRight)):
            result.append(leftToRight[i] * rightToLeft[i])

        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array in getTestData():
        product = solution.productExceptSelf(array)
        print("Product of array itself for " + str(array) + " is " + str(product))
