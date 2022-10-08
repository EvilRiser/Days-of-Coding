import sys

sys.stdout = open("./output.txt","w")
sys.stdin = open("./input.txt","r")

## LinkedList

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def printLL(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        llstr = ""
        #print(self.head.data)
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next

        print(llstr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index > self.get_length()-1:
            print("invalid Index")
            return
        if index == 0 :
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            count += 1
            if count == index:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length()-1:
            print("invalid Index")
            return
        if index == 0 :
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        
        while itr:
            count += 1
            
            if index == count:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(9)
    ll.insert_at_begining(45)
    ll.printLL()
    ll.insert_at_end(35)
    ll.printLL()
    a = LinkedList()
    a.insert_at_end(32)
    a.printLL()
    data_list = ["banana","apple","mango","grapes"]
    ll.insert_values(data_list)
    ll.printLL()
    print(ll.get_length())
    ll.remove_at(3)
    ll.printLL()
    ll.insert_at(2,"orange")
    ll.printLL()
