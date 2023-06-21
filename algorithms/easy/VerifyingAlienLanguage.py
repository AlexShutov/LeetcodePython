from typing import List


def getTestData():
    return [
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
        (["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve", "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge",
          "qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"),
        (["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz"),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
    ]


class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if (len(words)) < 2:
            return True

        orderDict = {c: i for i, c in enumerate(order)}
        orderDict['#'] = -1

        for wordIndex in range(1, len(words)):

            wordOne = words[wordIndex - 1]
            len1 = len(wordOne)
            wordTwo = words[wordIndex]
            len2 = len(wordTwo)

            if len1 > len2:
                wordTwo += '#' * (len1 - len2)
            else:
                wordOne += '#' * (len2 - len1)

            for i in range(len(wordOne)):
                c1 = orderDict[wordOne[i]]
                c2 = orderDict[wordTwo[i]]
                if c1 > c2:
                    return False
                if c1 < c2:
                    break
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    for words, dictionary in getTestData():
        isSorted = solution.isAlienSorted(words, dictionary)
        print(
            "Is words " + str(words) +
            " in alien language with dictionary " + dictionary +
            " sorted? " + str(isSorted)
        )
