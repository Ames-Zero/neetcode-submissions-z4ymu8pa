"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# let us maintain a hashmap: key n value pairs will be nodes
# iterate through each node and adjust the next and random
# simply return the address of the head in the hashmap
# O(n)

from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyList = {None:None}
        curr = head
        while curr:
            copyList[curr] = Node(curr.val)
            # copyList[curr].val = curr.val

            curr = curr.next

        res = head
        while res:
            # copy
            copyList[res].next = copyList[res.next]
            copyList[res].random = copyList[res.random]

            res = res.next

        return copyList[head]
                    