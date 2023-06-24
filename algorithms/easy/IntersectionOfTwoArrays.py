from typing import List


def getTestData():
    return [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4])
    ]


class Solution:
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = set(nums1).intersection(set(nums2))
        return [num for num in intersect]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = []
        for val in set1:
            if val in set2:
                result.append(val)
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for array1, array2 in getTestData():
        intersect = solution.intersection(array1, array2)

        print("intersection of " + str(array1) + " and " + str(array1) + " is: " + str(intersect))
