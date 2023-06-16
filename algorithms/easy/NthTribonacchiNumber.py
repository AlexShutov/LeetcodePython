from typing import List

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for i in range(3, n + 1):
            value = dp[i-1] + dp[i-2] + dp[i-3]
            dp.append(value)
        return dp[-1]

def getTestData():
    return [4, 25]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for number in getTestData():
        print("Tribonnacchi number for n = " + str(number) + " is: " + str(solution.tribonacci(number)))