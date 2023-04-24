# Insertion Sort
Insertion Sort is a sorting algorithm that traverses through a list and inserts the current value at the correct position within a newly built sorted list

## Pseudocode
~~~
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
~~~

## Trace
~~~
InsertionSort([8,4,23,42,16,15])
  Initial:
    input: [8,4,23,42,16,15]
    sorted: [8]

    FOR i = 1 up to i = input.length
      i = 1
        Insert([8], 4)
          4 < 8
          sorted = [4,8]
      i = 2
        Insert([4,8], 23)
          23 > 4
          23 > 8
          sorted = [4,8,23]
      i = 3
        Insert([4,8,23], 42)
          42 > 4
          42 > 8
          42 > 23
          sorted = [4,8,23,42]
      i = 4
        Insert([4,8,23,42], 16)
          16 > 4
          16 > 8
          16 < 23
          sorted = [4,8,16,23,42]
      i = 5
        Insert([4,8,16,23,42], 15)
          15 > 4
          15 > 8
          15 < 16
          sorted = [4,8,15,16,23,42]
    RETURN sorted = [4,8,15,16,23,42]

~~~

## Efficiency
time: O(N^2)
space: O(N)

## Testing
`pytest tests/code_challenges/test_insertion_sort.py`
