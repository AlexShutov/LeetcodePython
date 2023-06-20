from typing import List

def getTestData():
    return [
        [0,1,0],
        [0,2,1,0],
        [0,5, 10,2]
        ]

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid -1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid -1] < arr[mid]:
                l = mid
            else:
                r = mid

        return -1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array in getTestData():
        peak = solution.peakIndexInMountainArray(array)

        print("in mountain array " + str(array) + " peak value is: " + str(peak))

