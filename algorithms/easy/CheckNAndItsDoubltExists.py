from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        history = set()
        for number in arr:
            if number in history:
                return True
            history.add(number * 2)
            history.add(number / 2)
        return False


def getTestData():
    case1 = [10, 2, 5, 3]
    case2 = [3, 1, 7, 11]
    return [case1, case2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for case in getTestData():
        print("case #" + str(case) + " is double exists? " + str(solution.checkIfExist(case)))
