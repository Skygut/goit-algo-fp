class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def get_middle(self, head):
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sorted_lists(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.value < right.value:
            left.next = self.merge_sorted_lists(left.next, right)
            return left
        else:
            right.next = self.merge_sorted_lists(left, right.next)
            return right

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge_sorted_lists(left, right)
        return sorted_list

    def sort(self):
        self.head = self.merge_sort(self.head)

    @staticmethod
    def merge_two_sorted_lists(l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("Original List:")
    ll.print_list()
    ll.reverse()
    print("Reversed List:")
    ll.print_list()

    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print("\nOriginal List:")
    ll.print_list()
    ll.sort()
    print("Sorted List:")
    ll.print_list()

    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    print("\nList 1:")
    ll1.print_list()
    print("List 2:")
    ll2.print_list()
    merged_list = LinkedList()
    merged_list.head = LinkedList.merge_two_sorted_lists(ll1.head, ll2.head)
    print("Merged Sorted List:")
    merged_list.print_list()


if __name__ == "__main__":
    main()
