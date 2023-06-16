from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

def getTestData():
    return [
        "abbaca",
        "azxxzy"
    ]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for string in getTestData():
        print("String: " + str(string) + " without adjacent duplicates is: " + solution.removeDuplicates(string))

