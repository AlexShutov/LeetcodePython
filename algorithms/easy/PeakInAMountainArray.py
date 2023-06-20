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

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        return self.peakIndexInMountainArrayRecursive(0, len(arr) -1, arr)

    def peakIndexInMountainArrayRecursive(self, left, right, arr: List[int]) -> int:
        if left >= right:
            return -1
        middle = (left + right) // 2
        if arr[middle -1] < arr[middle] > arr[middle + 1]:
            return middle
        if arr[middle -1] < arr[middle]:
            return self.peakIndexInMountainArrayRecursive(middle, right, arr)
        else:
            return self.peakIndexInMountainArrayRecursive(left, middle, arr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array in getTestData():
        peak = solution.peakIndexInMountainArray(array)

        print("in mountain array " + str(array) + " peak value is: " + str(peak))

