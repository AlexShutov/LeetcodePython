from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

def getTestData():
    case1 = [1,2,3,1]
    case2 = [1,2,3,4]
    case3 = [1,1,1,3,3,4,3,2,4,2]
    return [case1, case2, case3]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for case in getTestData():
        print(solution.containsDuplicate(case))

