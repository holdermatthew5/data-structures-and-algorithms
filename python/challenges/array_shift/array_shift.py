import math

def insertShiftArray(list, n):
    """
    When given a list (array) as an argument, along with a single value as a second argument, we want to be able to insert that value in the middle of the array without removing any pre-existing values in the array. We want to shift the existing values to the right of where the new value is being placed (the middle).
    """
    pos = len(list)/2
    pos = math.ceil(pos)
    list.insert(pos, n)
    return list