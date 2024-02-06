class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_list

    def merge_sorted_lists(self, list1, list2):
        merged_list = LinkedList()
        current1, current2 = list1.head, list2.head

        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next

        while current1 is not None:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next

        while current2 is not None:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

        return merged_list

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Приклад використання:
llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(4)
llist.insert_at_end(2)

print("До сортування та реверсії:")
llist.print_list()

llist.reverse_linked_list()
llist.insertion_sort()

print("Після сортування та реверсії:")
llist.print_list()

list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

merged_list = llist.merge_sorted_lists(list1, list2)

print("Об'єднаний відсортований список:")
merged_list.print_list()
