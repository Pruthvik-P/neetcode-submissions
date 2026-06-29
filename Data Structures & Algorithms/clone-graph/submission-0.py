"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for neig in curr.neighbors:
                if neig not in oldToNew:
                    oldToNew[neig] = Node(neig.val)
                    q.append(neig)
                oldToNew[curr].neighbors.append(oldToNew[neig])

        return oldToNew[node]