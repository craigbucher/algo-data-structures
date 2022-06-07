class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self, head = None):
        self.head = head

    def add(self, new_data):
        # write your code to ADD (push??) an element to the Linked List
        new_node = Node(new_data)  # allocate node and put in data
        new_node.next = self.head  # make next of new_node as head
        self.head = new_node       # move the head to point to new_node

    def remove(self, key):
        # write your code to REMOVE an (first occurrence) element/key from the Linked List
        temp = self.head  #store head node
        # if head node itself has key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        
        # search for key to be deleted
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key not present
        if (temp == None): 
            return

        # unlink the node from the linked list
        prev.next = temp.next
        temp = None  # <== why?

    def get(self, element_to_get): #element_to_get = index
        # write you code to GET and return an element from the Linked List
        current = self.head  # initialize temp
        count = 0

        while(current):  # loop until end of linked list
            if (count == element_to_get):
                return(current.data)
            count += 1
            current = current.next

        assert(False)  # if index is not found
        return 0

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

##################################

if __name__ == '__main__':

    llist = LinkList() # start with an empty list
    
    ### Add method proven through tests of other methods

    # llist.head = Node(1) ### for print_list
    # second = Node(2)
    # third = Node(3)
    # llist.head.next = second; # Link first node with second
    # second.next = third; # Link second node with the third node
    # llist.print_list()

    # llist.add(1) ### for get
    # llist.add(4) # constructs list 1 -> 12 -> 1 -> 4 -> 1
    # llist.add(1)
    # llist.add(12)
    # llist.add(1)
    # print("Element at index 3 is :", llist.get(3))

    llist.add(7) ### for remove
    llist.add(1) # contructs list 2 -> 3 -> 1 -> 7
    llist.add(3)
    llist.add(2)
    print('Current list:')
    llist.print_list()
    llist.remove(1)
    print('Amended list:')
    llist.print_list()




    #https://www.geeksforgeeks.org/linked-list-set-1-introduction/