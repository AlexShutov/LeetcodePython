from collections import Counter
from typing import List


def getTestData():
    return [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4])
    ]


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersectUnique = set(nums1).intersection(set(nums2))
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result = []
        for key in intersectUnique:
            repeats = min(counter1[key], counter2[key])
            for i in range(repeats):
                result.append(key)
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array1, array2 in getTestData():
        intersect = solution.intersect(array1, array2)

        print("intersection of " + str(array1) + " and " + str(array1) + " is: " + str(intersect))
