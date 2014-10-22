"""
2.6
Given a circular linked list, implement an algorithm which returns the node at
the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points
to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A - > B - > C - > D - > E - > C [the same C as earlier]
Output: C
"""
from collections import defaultdict
class Node(object):
  def __init__(self, value):
    self.next = None
    self.value = value

class Linkedlist(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def Addnode(self, Node):
    if self.head == None:
      self.head = Node
    else:
      self.tail.next = Node
    self.tail = Node

def iscircular(a):
  seen = defaultdict(int)
  cur = a.head
  while cur:
    if cur not in seen:
      seen.setdefault(cur)
    else:
      return cur.value
    cur = cur.next

# Sanity Checks
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
linked = Linkedlist()
l = [a,b,c,d,e, c]
for i in l:
  linked.Addnode(i)

print iscircular(linked)









