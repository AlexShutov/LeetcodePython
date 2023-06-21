from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getTestCases():
    case1 = [1, 2, 6, 3, 4, 5, 6]
    case2 = []
    case3 = [7, 7, 7, 7]
    return [case1, case2, case3]


def getLinkedList(numbers: [int]):
    dummy = ListNode(0, None)
    head = dummy
    for number in numbers:
        current = ListNode(number, None)
        head.next = current
        head = current
    return dummy.next


def printLinkedList(head: ListNode):
    while head:
        print(head.val)
        head = head.next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    valuesToRemove = [6, 1, 7]
    for index, case in enumerate(getTestCases()):
        list = getLinkedList(case)
        print("Case #" + str(index + 1) + ": ")
        printLinkedList(list)
        value = valuesToRemove[index]
        print("List after removing value " + str(value) + ": ")
        resultList = solution.removeElements(list, value)
        printLinkedList(resultList)
