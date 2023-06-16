from typing import List


class Solution:

    # def checkRecord(self, s: str) -> bool:
    #     abscentCount = s.count('A')
    #     if abscentCount >= 2:
    #         return False
    #     s = s.replace('A', '')
    #     return s.count('LLL') == 0

    def checkRecord(self, s: str) -> bool:
        abscentCount = 0
        lateCount = 0
        for char in s:
            if char == 'A':
                lateCount = 0
                abscentCount += 1
                if abscentCount == 2:
                    return False
                continue

            if char == 'L':
                lateCount += 1
                if lateCount == 3:
                    return False
                continue
            lateCount = 0
        return True



def getTestData():
    return ["PPALLP", "PPALLL", "LALL"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for record in getTestData():
        print("record: " + str(record) + " is eligible? : " + str(solution.checkRecord(record)))



