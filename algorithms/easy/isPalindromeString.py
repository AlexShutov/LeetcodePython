class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            charLeft = s[left]
            if not self.isCharacter(charLeft):
                left += 1
                continue
            charRight = s[right]
            if not self.isCharacter(charRight):
                right -= 1
                continue
            if charLeft.lower() != charRight.lower():
                return False
            left += 1
            right -= 1

        return True

    def isCharacter(self, c: str) -> bool:
        return c.isalpha() or c.isnumeric()


def getTestData():
    return [
        "0P",
        "A man, a plan, a canal: Panama",
        "race a car",
        " "
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        isPalindrome = solution.isPalindrome(string)
        print("Is string: " + string + " is palindrome? " + str(isPalindrome))
