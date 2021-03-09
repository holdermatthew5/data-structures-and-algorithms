# Quick Sort Function

Takes in an array
Sets a "pivot point" (the last value in the list if sorting in ascending order and first value if sorting in descending order)
Compares all other values in the list on this recursion against the pivot point
Places each value in a less/more list to be recursed
Finally, returns the less list concatenated with the pivot point in list form and the more list in that order.

test [8,4,23,42,16,15]:
    arr = [8,4,23,42,16,15]
    pivot = 15
    arr = [8,4,23,42,16]
    less = [8,4]
        arr = [8,4]
        pivot = 4
        arr = [8]
        less = []
        more = [8]
            arr = [8]
            return [8]
        return [] + [4] + [8]
    more = [23,42,16]
        arr = [23,42,16]
        pivot = 16
        arr = [23,42]
        less = []
        more = [23,42]
            arr = [23,42]
            pivot = 42
            arr = [23]
            less = [23]
                arr = [23]
                return [23]
            more = []
            return [23] + [42] + []
        return [] + [16] + [23,42]
    return [4,8] + [15]  + [16,23,42]
    quick_sort([8,4,23,42,16,15]) == [4,8,15,16,23,42]