from typing import List

def getTestData():
    return [3, 0, 1]

class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1, 1]]
        if numRows < 3:
            return result[:numRows]
        for _ in range(numRows -2):
            newRow = [1]
            for i in range(1, len(result[-1])):
                value = result[-1][i-1] + result[-1][i]
                newRow.append(value)
            newRow.append(1)
            result.append(newRow)
        return result

    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        result = [[1], [1, 1]]
        if numRows < 3:
            return result[rowIndex]
        for index in range(2, numRows):
            newRow = [1]
            for i in range(1, len(result[-1])):
                value = result[-1][i-1] + result[-1][i]
                newRow.append(value)
            newRow.append(1)
            result.append(newRow)
            if rowIndex == index:
                return newRow
        return []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for nRow in getTestData():
        row = solution.getRow(nRow)

        print(str(nRow)+ " row for Pascal triangle is: " + str(row))

