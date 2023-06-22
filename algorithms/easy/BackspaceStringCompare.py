class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.removeBackSpaces(s) == self.removeBackSpaces(t)

    def removeBackSpaces(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


def getTestData():
    return [
        ("ab#c", "ad#c"),
        ("ab##", "c#d#"),
        ("a#c", "b")
    ]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for s, t in getTestData():
        isBackSpaceTypingEquals = solution.backspaceCompare(s, t)
        print("Are strings " + s + " and " + t + " backspace typing equals? " + str(isBackSpaceTypingEquals))
