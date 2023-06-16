from typing import List

def getTestData():
    case1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    case2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    return [case1, case2]

class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = []
        for email in emails:
            first, second = email.split('@')
            first = first.replace('.', '')
            first = first.split('+')[0]
            unique.append(first.lower() + '@' + second.lower())
        return len(set(unique))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    for value in getTestData():
        print(solution.numUniqueEmails(value))

