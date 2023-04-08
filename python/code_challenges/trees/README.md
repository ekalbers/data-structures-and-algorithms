# Chellenge15 - trees
## [Github Repo](https://github.com/ekalbers/data-structures-and-algorithms)
### Node
- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node
### Binary Tree
- Create a Binary Tree class
  - Define a method for each of the depth first traversals:
    - pre order
    - in order
    - post order
  - Each depth first traversal method should return an array of values, ordered appropriately.
### Binary Search Tree
- Create a binary search tree class
  - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  - Add
    - Arguments: value
    - Return: nothing
    - Adds a new node with that value in the correct location in the binary search tree.
  - Contains
    - Argument: value
    - Returns: boolean indicating whether or not the value is in the tree at least once.

## Whiteboard Process
### `No Whiteboard Required for Challenge05`

## Approach & Efficiency
### Binary Tree
  - pre order
    - function should have root parameter with default None and a values parameter with default of and empty list
      - set root variable equal to self.root
      - append root.value to values
      - check if root has a left attribute
        - if it does call pre_order and pass root.left and values as parameters
      - check if root has a right attribute
        - if it does call pre_order and past root.right and values as parameters
      - return values
  - in order
    - do the same as in order but move the append root.value statement to between if statements checking root.left and root.right
  - post order
    - move append root.value statement to the last line before return statement
### Binary Search Tree
  - add
    - function should have value and root parameters. value is the value to be added to the tree, root is a node in the tree and defaults to None
      - first, check if root is none
        - if it is set root equal to self.root
        - elif self.root is None
          - create a Node with value as the parameter and set self.root equal to the new Node. Then use empty return statement to terminate function
      - check if value is greater than root.value
        - if it is, check if there is a right attribute for root
          - if there is call self.add with value and root.right as parameters
          - else set root.right equal to a new Node instance with value as the parameter
      - if value is not greater than root.value
        - check root for a left attribute
          - if it has left attribute call self.add with value and root.left as parameters
          - else set root.left equal to a new Node instance with value as the parameter
  - contains
    - fucntion should have value and root parameters. value is the value to be checked for existence in the tree, root is a node within the tree, defaults to None
      - first check if root is None
        - if it is set root equal to self.root
      - check if value is equal to root.value
        - if it is return True
      - else check if root.right and root.left
        - if they do, call self.contains within an if statement with root.right or left and the root parameters
        - this will use recursive logic to search the tree and return True all the way up the recursive tree.


## Solution
run tests: 'pytest'
