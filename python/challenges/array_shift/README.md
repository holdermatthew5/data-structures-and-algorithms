Authors: Matthew Holder and Sean Hawkins

Version: 0.1.0

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/20#issue-536524128)

Problem Domain:
    When given a list (array) as an argument, along with a single value as a second argument, we want to be able to insert that value in the middle of the array without removing any pre-existing values in the array. We want to shift the existing values to the right of where the new value is being placed (the middle).

Approach & Efficiency:
    We kept it simple by creating a function that takes in a list (array) and a new value to be added. We took the length of the list argument and divided by 2 to get the middle position. In case of an odd length, we then used math.ceil to ensure that length is rounded up. We then used insert() to insert the new value at the correct middle position. Finally, we returned the array with the new value. Big O was O(1) - Constant time algorithms take the same amount of time to be executed. Execution time of O(1) algorithms is independent of input size.

Purpose:
    insert a given value into the center of a given list. If there is an odd number of list values it will insert the new value to the right of the center value. Once inserted all displaced values will be shifted to the right one index.

Use:
    To use `insertShiftArray()` import math and import import the method with the following lines of code:
      - `import math`
      - `from array-shift.array_shift.array_shift import insertShiftArray`

    Arguments: insertShiftArray takes two mandatory arguments (list, value). To call it enter the following code into your code file:
      - insertShiftArray([your, list, goes, here], value)