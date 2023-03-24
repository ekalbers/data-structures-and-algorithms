# Chellenge05 - Linked List Implementation
## [Github Repo](https://github.com/ekalbers/data-structures-and-algorithms)
### Node
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
### Linked List
- Create a Linked List class
- Within your Linked List class, include a head property.
  - Upon instantiation, an empty Linked List should be created.
- The class should contain the following methods
  - insert
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.
  - includes
    - Arguments: value
    - Returns: Boolean
    - Indicates whether that value exists as a Node’s value somewhere within the list.
  - to string
    - Arguments: none
    - Returns: a string representing all the values in the Linked List, formatted as:
    - `"{ a } -> { b } -> { c } -> NULL"`

## Whiteboard Process
### `No Whiteboard Required for Challenge05`

## Approach & Efficiency
### insert:
- set `next` value for provided node to `head` and set head to node value provided
- bigO
  - time: O(1)
  - space: O(1)
### includes
- set `current` equal to `head` then use `while` loop to cycle through `LinkedList`. Every time through the loop compare `current` to provided `value`, `if current == value` return `true`, `else` use `next` to go to next node. Terminate loop if `current == None`. Return `False` when loop terminates. Loop should not terminate unless it iterates all the way through `LinkedList` without finding a node with value matching `value` parameter.
- bigO
  - time: O(n)
  - space: O(n)
### to string
- set `current` to `head` print, then use `while` loop to go through `LinkedList` and print each node value and using `current.next` at the end of each loop run. loop end when `current` == `None`.
- bigO
  - time: o(n)
  - space: O(n)

## Solution
run tests: 'pytest'
