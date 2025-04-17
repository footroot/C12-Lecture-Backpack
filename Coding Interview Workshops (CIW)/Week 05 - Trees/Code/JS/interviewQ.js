/**
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

 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// Binary Tree Node
class TreeNode {
    constructor(val = 0, left = null, right = null) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
  }
  
  function findNode(root, findVal) {
      if (root) {
          if (root.val == findVal){
              return root
          }
  
          x = findNode(root.left, findVal)
          if (x) {
              return x
          }
  
          x = findNode(root.right, findVal)
          if (x) {
              return x
          }
      }
      return null
  }
  
  /**
  node1 = new TreeNode(15)
  node2 = new TreeNode(17)
  node3 = new TreeNode(19)
  node4 = new TreeNode(20, node1, node2)
  node5 = new TreeNode(80, node3)
  root = new TreeNode(50, node4, node5)
  
  console.log(findNode(root, 15).val)
   */
  
  /**
   * @param {number[][]} descriptions
   * @return {TreeNode}
   */
  var createBinaryTree = function(descriptions) {
      let root = null;
      for (let i = 0; i < descriptions.length; i++) {
          desc = descriptions[i];
          node = findNode(root, desc[0]);
          if (node) {
              child = new TreeNode(desc[1]);
          } else {
              node = new TreeNode(desc[0]);
              child = findNode(root, desc[1]);
              root = node;
              if (child == null) {
                  child = new TreeNode(desc[1]);
              }
          }
  
          if (desc[2]) {
              node.left = child;
          } else {
              node.right = child;
          } 
      }
      return root;
  };
  
  