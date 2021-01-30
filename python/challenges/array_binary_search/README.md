Authors: Matthew Holder and Alex Angelico

Version: 0.1.0

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/21#issue-539991106)

Problem Domain:
    When given a list and integer this function will find the integer in the list and return its index. If the integer is not present in the list it will return -1 instead.

Approach & Efficiency:
    We really wanted to code this in programmatically instead of hardcoding it to view every indices value, but there was a point at which we would have to have created an equation to keep track of the index in the original list otherwise it could end up narrowing down the list to one with only the correct value at which point the index would return 0. With the equation finding 5 in [1,2,3,4,5,6,7] would return 4 instead of 0. After coming close to class being over and still not having a working equation we decided it would be best to hardcode it and come back to it in our own time.

Use:
    To use the binary_search function simply call it passing in an ordered list of integers as the first argument and an integer to be located. This can be done with the following line of code (remember list and int are both reserved words and should not be used as variables for passing in as arguments):
      - `binary_search(li, integer)`