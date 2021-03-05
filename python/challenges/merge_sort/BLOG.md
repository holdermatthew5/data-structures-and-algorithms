## The function:

The function `merge_sort` takes in one list of integers.

It divides the list into a `right` and `left` list, then recurses for each list until the 1st list has only one integer remaining (`left` list takes 1 extra value when the list being divided has an odd number of values).

In that same recursion it continues to the 2nd list and if it has more than one value it recurses again.

In the sorting section it iteratively compares the values at index 0 of each list, adds the smaller int to a `new` list and removes it from it's original list (`left` or `right`).

If a list is not empty it adds the remaining values to new (because the function continues to the sorting section, in each recursion, both left and right are sorted at the very last level so they merge nicely).

Finally the `new` list is return to its caller whether that be the recursion statement or a proper use of the function.

## Test case:

[8,4,23,42,16,15]
    right = [8,4,23]
        right = [8]
        left = [4,23]
            right = [4]
            left = [23]
            return [4,23]
        return [4,8,23]
    left = [42,16,15]
        right = [42]
        left = [16,15]
            right = [16]
            left = [15]
            return [15,16]
        return [15,16,42]
    return [4,8,15,16,23,42]