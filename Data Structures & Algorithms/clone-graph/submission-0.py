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
             return
        
        alreadyChecked = {}
        alreadyChecked[node] = Node(node.val)
        hash = {}
        que = deque([node])

        while que:
            nod = que.popleft()
            for neighbor in nod.neighbors:
                if neighbor not in alreadyChecked:
                   alreadyChecked[neighbor] = Node(neighbor.val) 
                   que.append(neighbor)

                alreadyChecked[nod].neighbors.append(alreadyChecked[neighbor])


        return alreadyChecked[node]

