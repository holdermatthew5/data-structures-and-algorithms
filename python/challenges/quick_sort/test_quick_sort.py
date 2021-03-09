import pytest
from quick_sort import quick_sort

def test_quick_sort1():
    assert quick_sort([8,4,23,42,16,15]) == [4,8,15,16,23,42]

def test_quick_sort2():
    assert quick_sort([20,18,12,8,5,-2]) == [-2,5,8,12,18,20]

def test_quick_sort3():
    assert quick_sort([5,12,7,5,5,7]) == [5,5,5,7,7,12]

def test_quick_sort4():
    assert quick_sort([2,3,5,7,13,11]) == [2,3,5,7,11,13]