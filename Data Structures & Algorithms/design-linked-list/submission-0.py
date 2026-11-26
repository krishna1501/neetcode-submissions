class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)  

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        cur = self.head.next
        count = 0

        while cur is not None:
            if count == index:
                return cur.val

            cur = cur.next
            count += 1

        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return

        cur = self.head
        count = 0

        while count < index and cur.next is not None:
            cur = cur.next
            count += 1

        if count == index:
            node = ListNode(val)
            node.next = cur.next
            cur.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        cur = self.head
        count = 0

        while count < index and cur.next is not None:
            cur = cur.next
            count += 1

        if count == index and cur.next is not None:
            cur.next = cur.next.next