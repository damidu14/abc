class Node:
    def init(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def init(self):
        self.head = None 
        

def listprint(self):
    printval=self.head
    while printval is not None:
        print (printval.data)
        printval = printval.next

def _inset_at_Begining(self,newdata):
    newNode = Node(newdata)
    newNode.next = self.head

    self.head = newNode        
        
ll = LinkedList()
ll.head = Node("Toyota")
l2 = Node("Bmw")
l3 = Node("Audi")

ll.head.next = 12
l2.next = 13

ll.listprint()
print("")
ll._inset_at_Begining("Benz")
ll.listprint()
ll._inset_at_Begining("Chr")
print("")












