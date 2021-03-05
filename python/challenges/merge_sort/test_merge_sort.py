import pytest
from merge_sort import merge_sort

def test_sort1():
    assert merge_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]

def test_sort2():
    assert merge_sort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]

def test_sort3():
    assert merge_sort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12]

def test_sort4():
    assert merge_sort([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]