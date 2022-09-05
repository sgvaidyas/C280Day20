class Node:
    def __init__(self,ele):
        self.data = ele
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertBegin(self,ele):
        temp = Node(ele)
        if self.head is not None:
            temp.next = self.head
            self.head.prev = temp
        else:
            self.tail=temp
        self.head = temp

    def insertEnd(self,ele):
        temp = Node(ele)
        if self.head is None:
            self.head = temp
        else:
            ptr = self.head
            while ptr.next!=None:
                ptr = ptr.next
            ptr.next = temp
            temp.prev = ptr
        self.tail = temp

    def insertPos(self,pos,ele):
        ind=1
        temp = Node(ele)
        ptr = self.head
        while ptr!=None:
            if ind==pos:
                break
            ptr=ptr.next
            ind+=1
        if pos<1 or pos>ind or self.head==None:
            print("Invalid position")
        elif ind==pos and ptr==None:
            self.insertEnd(ele)
        else:
            if ptr==self.head:
                self.insertBegin(ele)
            else:
                pp = ptr.prev
                cp = ptr
                pp.next = temp
                temp.prev = pp
                temp.next = cp
                cp.prev = temp

    def deleteBegin(self):
        if self.head == None:
            print("LIST EMPTY CANT DEL")
        else:
            print("Deleting = ",self.head.data)
            temp = self.head
            self.head = self.head.next
            if self.head !=None:
                self.head.prev =None
            else:
                self.tail = None
            del temp

    def deleteEnd(self):
        if self.head == None:
            print("LIST EMPTY CANT DEL")
        else:
            print("deleting ",self.tail.data)
            temp = self.tail
            self.tail = self.tail.prev
            if self.tail!=None:
                self.tail.next = None
            else:
                self.head = None
            del temp

    def deletePos(self,pos):
        ptr = self.head
        for ind in range(1,pos+1):
            ptr=None if self.head==None else ptr.next
            if ptr==None:
                break
        if (ptr==None and pos>ind) or pos<1 or self.head==None:
            print("Cannot del invalid")
        elif ind==pos and ptr==None:
            self.deleteEnd()
        elif pos==1 and self.head!=None:
            self.deleteBegin()
        else:
            pp = ptr.prev
            pp.prev.next = ptr
            ptr.prev = pp.prev
            print("Deleting  = ",pp.data)
            del pp


    def display(self):
        if self.head is None:
            print("LIST IS EMPTY")
        else:
            print("LIST ELEMENTS")
            ptr = self.head
            while ptr!=None:
                print(ptr.data,end="-->")
                ptr = ptr.next
            print()
