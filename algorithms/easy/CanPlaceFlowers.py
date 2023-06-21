from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


def getTestData():
    case1 = [1, 0, 0, 0, 0, 1]
    flowers1 = 2
    case2 = [1, 0, 0, 0, 1]
    flowers2 = 1
    case3 = [1, 0, 0, 0, 1]
    flowers3 = 2
    return [(case1, flowers1), (case2, flowers2), (case3, flowers3)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for (flowerBed, flowers) in getTestData():
        canPlace = solution.canPlaceFlowers(flowerBed, flowers)
        print("can place " + str(flowers) + " in flowerbed " + str(flowerBed) + " ? " + str(canPlace))
