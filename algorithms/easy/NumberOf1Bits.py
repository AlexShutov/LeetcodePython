class Solution:
    def hammingWeight(self, n: int) -> int:
        bitsCount = 0
        while n > 0:
            bitsCount += n & 1
            n >>= 1
        return bitsCount


def getTestData():
    return [
        1011,
        10000000,
        11111111111111111111111111111101
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for number in getTestData():
        bitsCount = solution.hammingWeight(number)
        print("For number " + str(number) + " Hamming weight is: " + str(bitsCount))
