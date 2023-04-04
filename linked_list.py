#!/usr/bin/pydoc3.10

class linked_list:
    def __init__(self):
        self.next=self
        self.prev=self
        self.value=None
def insert_new(a,val=None):
    b=linked_list()
    b.next=a.next
    b.prev=a
    a.next=b
    b.value=val

def remove_elem(a):
    if a.next==a:
        a=None
        return
    a.next.prev=a.prev
    a.prev.next=a.next

def print_list(l):
    i=l
    while True:
        print(i.value)
        i=i.next
        if i==l: break

def generate_example_list(val1=None,val2=None,a=linked_list(),b=linked_list()):
    a.value,a.next,a.prev=val1,b,b
    b.value,b.next,b.prev=val2,a,a

if __name__ == "__main__":
    a=linked_list()
    generate_example_list(1,2,a)
    insert_new(a.next,5)
    print_list(a)
    print()
    remove_elem(a.next)
    print_list(a)
