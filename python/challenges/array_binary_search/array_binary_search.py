def binary_search(li, key):
    '''
        This function takes in an ordered list and an integer. It returns the index of the integer. If the integer is not in the list it returns -1.
    '''
    i = 0
    while i < len(li):
        if li[i] == key:
            return i
    return -1

# Tests
def test_search():
    assert binary_search([1,2,3,4,5,6,7,8], 3) == 2

def test_search():
    assert binary_search([0,1,2,3,4,5,6,7,8], 9) == -1

def test_search_three():
    assert binary_search([54,66,73,82,99], 82) == 3

def test_search_two():
    assert binary_search([54,66,73,82,99], 72) == -1