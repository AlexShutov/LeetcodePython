from typing import List

def getTestData():
    return [2, 5]

class Solution:

    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n + 1):
            number = i
            bitsCount = 0
            while number > 0:
                (number, mod) = divmod(number, 2)
                bitsCount += mod
            result.append(bitsCount)
        return result




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for value in getTestData():
        print(solution.countBits(value))

