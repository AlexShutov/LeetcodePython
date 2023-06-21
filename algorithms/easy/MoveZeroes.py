from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for seeker in range(len(nums)):
            if nums[write] == 0 and nums[seeker] != 0:
                nums[seeker], nums[write] = nums[write], nums[seeker]

            if nums[write] != 0:
                write += 1


def getTestData():
    case1 = [0, 1, 0, 3, 12]
    case2 = [0]
    return [case1, case2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for (index, case) in enumerate(getTestData()):
        print("case #" + str(index + 1))
        print("Initial values: " + str(case))
        solution.moveZeroes(case)
        print("values after moving zeroes: " + str(case))
