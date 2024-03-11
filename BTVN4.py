class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_node(head, index):
    if index == 0:
        if head:
            deleted_node = head
            head = head.next
            deleted_node.next = None  
            return deleted_node

    current = head
    for _ in range(index - 1):
        if current is None or current.next is None:
            return None  

        current = current.next

    if current and current.next:
        deleted_node = current.next
        current.next = current.next.next
        deleted_node.next = None  
        return deleted_node
    else:
        return None  

linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Danh sách liên kết gốc:")
current_node = linked_list
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")


deleted_node = delete_node(linked_list, 2)
if deleted_node:
    print("Nút đã bị xóa:", deleted_node.value)

print("Danh sách liên kết sau khi xóa nút ở chỉ mục 2:")
current_node = linked_list
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
