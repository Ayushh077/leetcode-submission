class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        curr = head
        n = 1

        while curr.next:
            curr = curr.next
            n += 1

        curr.next = head
        k = k % n

        steps = n - k
        while steps:
            curr = curr.next
            steps -= 1

        head = curr.next
        curr.next = None

        return head