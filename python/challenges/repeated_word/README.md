**Author:** Matthew Holder
**Version:** 0.1

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/39#issue-593551128)

## Problem Domain

- Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in a provided string.

## Description

- first_word: Makes use of check and gather to return the first word to be used twice in a given string.
- check: Removes commas trailing words and returns a normalized word with `.lower()`.
- gather: Returns a list of words formed from strings of all characters between spaces including punctuation.