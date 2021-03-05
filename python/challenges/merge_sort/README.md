**Author:** Matthew Holder
**Version:** 0.1

[PR]()

## Problem Domain:

Write a function merge_sort which sorts a list by recursively diving into 2 parts and iteratively merging the greater number of the 2 at index 0 of right and left halves into the result list.

## Description:

The function `merge_sort` takes in one list of integers.

It divides the list into a `right` and `left` list, then recurses for each list until the 1st list has only one integer remaining (`left` list takes 1 extra value when the list being divided has an odd number of values).

In that same recursion it continues to the 2nd list and if it has more than one value it recurses again.

In the sorting section it iteratively compares the values at index 0 of each list, adds the smaller int to a `new` list and removes it from it's original list (`left` or `right`).

If a list is not empty it adds the remaining values to new (because the function continues to the sorting section, in each recursion, both left and right are sorted at the very last level so they merge nicely).

Finally the `new` list is return to its caller whether that be the recursion statement or a proper use of the function.