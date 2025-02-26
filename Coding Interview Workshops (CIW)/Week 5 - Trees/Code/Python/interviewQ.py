'''
1. Assumptions
- Binary tree always valid
- Descriptions are always valid
- Data structures are not very big, not small
- [P, C, L]

2. Plan

a. look at description
b. check if the parent node is in the tree
    -> if it is, create a new node with child, add it on l/r of parent
    -> if not, create a new node with parent, check if child is in tree
        -> if it is, store child node
        -> if not, create new child node
        add child node to new parent node on l/r

checking if in tree:
-> keep an array of nodes in tree -> space, time, a little bit complex
-> search the tree -> is complex, traverse the tree, level order

1. Start with check if node in tree (find method)
2. construction function
3. Done!


3. Code!

 '''

'''
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 '''

# Binary Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findNode(root, findVal):
    if (root): 
        if (root.val == findVal):
            return root
        

        x = findNode(root.left, findVal)
        if (x):
            return x
        

        x = findNode(root.right, findVal)
        if (x):
            return x

    return None


class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        root = None
        for desc in descriptions:
            node = findNode(root, desc[0])
            if (node):
                child = TreeNode(desc[1])
            else:
                node = TreeNode(desc[0])
                child = findNode(root, desc[1])
                root = node
                if (child == None):
                    child = TreeNode(desc[1])
            

            if (desc[2]):
                node.left = child
            else:
                node.right = child

        return root

sol = Solution()
print(sol.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]).right)