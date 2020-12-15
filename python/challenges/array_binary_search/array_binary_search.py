def binary_search(li, key):
    i = 0
    while i < len(li):
        if li[i] == key:
            return i
    return -1