
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        number = 0
        while x > 0:
            (x, mod) = divmod(x, 10)
            number = number * 10 + mod
        return original == number


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    testValues = [121, -121, 10]
    for value in testValues:
        print(solution.isPalindrome(value))

