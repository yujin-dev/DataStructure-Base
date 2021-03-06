from linked_list.singly_linked_list import SinglyLinkedList

def checkLength(linkedList):
    count = 0
    temp = linkedList.head
    while(temp!=None):
        count += 1
        temp = temp.next
    return count

if __name__ == "__main__":
    myLinkedList = SinglyLinkedList()
    for i in range(10):
        myLinkedList.insertAtStart(i)
    myLinkedList.printLinkedList()
    print()
    print("Length: ", checkLength(myLinkedList))
