# Chellenge05 - Stack and Queue Implementation
## [Github Repo](https://github.com/ekalbers/data-structures-and-algorithms)
### Node
- Imported from linked_list.py
### Stack
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
  - This object should be aware of a default empty value assigned to top when the stack is created.
  - The class should contain the following methods:
  - push
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.
  - pop
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    - Should raise exception when called on empty stack
  - peek
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty.

### Queue
- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
  - This object should be aware of a default empty value assigned to front when the queue is created.
  - The class should contain the following methods:
  - enqueue
    - Arguments: value
    - adds a new node with that value to the back of the queue with an O(1) Time performance.
  - dequeue
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
  - peek
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the queue is empty

## Whiteboard Process
### `No Whiteboard Required for Challenge05`

## Approach & Efficiency
### Stack
- push
  - create variable top
  - set self.top equal to new Node with top as `next` parameter
- pop
  - set stack_top variable equal to self.top
  - set self.top equal to self.top.next
  - return stack_top
- peek
  - return self.top
- is empty
  - if self.top is not None return False otherwise return True

### Queue
- enqueue
  - make self.back equall to a new node with self.back as `next` parameter
- dequeue
  - traverse through queue using current variable until current.next is none
  - also track last node with last variable through traversal
  - after traversing set self.head equal to last and set last.next equal to None
  - return current
- peek
  - return self.front
- is empty
  - if self.front is not none return False otherwise return True

## Solution
run tests: 'pytest'
