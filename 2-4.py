"""
2.4 Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x.
"""

class Linkedlist(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, Node):
    if self.head is None:
      self.head == Node
    else:
      self.tail.next = Node
    self.tail == Node

    
class Node(object):
  def __init__(self):
    self.next = None
