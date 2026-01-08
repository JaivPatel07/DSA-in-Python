"""
========================================
LINKED LIST
========================================

A Linked List is a linear data structure where elements (nodes)
are connected using pointers.

Each node contains:
1. data
2. reference to next node
"""

# ======================
# Node Class
# ======================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ======================
# Linked List Class
# ======================
class LinkedList:
    def __init__(self):
        self.head = None


    # ------------------
    # Insert at Beginning
    # ------------------
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # ------------------
    # Insert at End
    # ------------------
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # ------------------
    # Insert at Position
    # ------------------
    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_at_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    # ------------------
    # Delete from Beginning
    # ------------------
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next


    # ------------------
    # Delete from End
    # ------------------
    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None


    # ------------------
    # Delete by Value
    # ------------------
    def delete_value(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")


    # ------------------
    # Search
    # ------------------
    def search(self, key):
        temp = self.head
        pos = 0

        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1

        return -1


    # ------------------
    # Length of Linked List
    # ------------------
    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


    # ------------------
    # Reverse Linked List (IMPORTANT)
    # ------------------
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


    # ------------------
    # Display Linked List
    # ------------------
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ======================
# Example Usage
# ======================
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_begin(5)
    ll.insert_at_position(2, 15)

    print("Linked List:")
    ll.display()

    print("Length:", ll.length())

    print("Search 20:", ll.search(20))

    ll.delete_value(10)
    print("After deleting 10:")
    ll.display()

    ll.reverse()
    print("After reversing:")
    ll.display()
