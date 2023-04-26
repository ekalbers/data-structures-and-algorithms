# Merge Sort
Merge sort divides a list into sub-lists, sorts the sub lists, then merges the sub lists back together into a single sorted list.

## Pseudocode
~~~
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
~~~

## Trace
~~~
lst = [8, 4, 23, 42, 16, 15]

Mergesort(lst)
  [8, 4, 23, 42, 16, 15]
  left:[8, 4, 23] right:[42, 16, 15]
  left:(left:[8, 4] right:[23]) right:(left:[42, 16] right:[15])
  left:(left:(left:[8] right:[4]) right:[23]) right:(left:(left:[42] right:[16]) right:[15])
  ***List has been split into smallest parts, sorting begins
  left:(left:[4, 8] right:[23]) right:(left:[16, 42] right:[15])
  left:[4, 8, 23] right:[15, 16, 42]
  [4, 8, 15, 16, 23, 42]

lst = [4, 8, 15, 16, 23, 42]
~~~

## Efficiency
time: O(N)
space: O(N)

## Testing
`pytest tests/code_challenges/test_merge_sort.py`
