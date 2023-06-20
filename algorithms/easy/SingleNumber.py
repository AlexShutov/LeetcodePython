from typing import List

def getTestData():
    return [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1]
        ]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        history = set()
        for number in nums:
            if number in history:
                history.remove(number)
            else:
                history.add(number)
        return history.pop()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for numbers in getTestData():
        number = solution.singleNumber(numbers)

        print("single number from " + str(numbers) + " is " + str(number))

