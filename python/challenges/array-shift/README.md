Authors: Matthew Holder and Sean Hawkins

Version: 0.1.0

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/20#issue-536524128)

Problem Domain:
When given a list (array) as an argument, along with a single value as a second argument, we want to be able to insert that value in the middle of the array without removing any pre-existing values in the array. We want to shift the existing values to the right of where the new value is being placed (the middle).

Purpose:
- insert a given value into the center of a given list. If there is an odd number of list values it will insert the new value to the right of the center value. Once inserted all displaced values will be shifted to the right one index.

Use:
- To use `insertShiftArray()` import math and import import the method with the following lines of code:
  - `import math`
  - `from array-shift.array_shift.array_shift import insertShiftArray`
- Arguments: insertShiftArray takes two mandatory arguments (list, value). To call it enter the following code into your code file:
  - insertShiftArray([your, list, goes, here], value)