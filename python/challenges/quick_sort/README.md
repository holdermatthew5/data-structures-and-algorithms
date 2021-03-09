**Author:** Matthew Holder
**Version:** 0.1

[PR]()

Problem Domain:

Write a quick_sort function in python which recursively sorts a list by defining a pivot point, comparing remaining values to pivot point and placing values larger than pivot point after pivot point and smaller values before pivot point, and returning the sorted list.

Description:

This sorting function makes use of `less` and `more` lists which hold appropriate values from the original list.
It then calls itself passing in `less`.
It then calls itself passing in `more`.
If either list has `less` than 2 indices it is automatically returned for use as is.
The `less` list, pivot point in list form, and `more` list are then concatinated and returned.