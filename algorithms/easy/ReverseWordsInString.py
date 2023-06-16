from typing import List


class Solution:

    def reverseWords(self, s: str) -> str:
        return s


def getTestData():
    return [
        "Let's take LeetCode contest",
        "God Ding"
    ]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        print("Original string: " + "".join(string) + " reversed: " + solution.reverseWords(string))

