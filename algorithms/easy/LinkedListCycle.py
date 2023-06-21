from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getTestCases():
    return [
        ([1, 2], -1),
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1)
    ]


def getLinkedList(numbers: [int]):
    dummy = ListNode(0, None)
    head = dummy
    for number in numbers:
        current = ListNode(number, None)
        head.next = current
        head = current
    return dummy.next


def makeLoopTo(head: ListNode, position: int):
    if position == -1:
        return
    tail = head
    if not head:
        return
    while tail.next:
        tail = tail.next

    loop = head
    for _ in range(position):
        loop = loop.next
    tail.next = loop


def printLinkedList(head: ListNode, size: int):
    listValues = []
    i = 0
    while head and i < size:
        listValues.append(head.val)
        head = head.next
        i = i + 1
    print(listValues)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


if __name__ == '__main__':

    solution = Solution()

    for numbers, loopPosition in getTestCases():
        print("for linked list from numbers " + str(numbers) + " with loop at position " + str(loopPosition) + " :")
        list = getLinkedList(numbers)

        makeLoopTo(list, loopPosition)
        printLinkedList(list, 10)

        hasCycle = solution.hasCycle(list)
        print("Does list has a cycle? " + str(hasCycle))
        print("")
