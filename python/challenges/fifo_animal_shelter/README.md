**Author:** Matthew Holder
**Version:** 0.1.0

[PR](https://github.com/holdermatthew5/data-structures-and-algorithms/pull/28#issue-554663040)

Problem Domain:

    I would like to be able to create an animal shelter. It should be able to add both cats and dogs on request. It should be able to remove cats or dogs in a FIFO fashion. When no preference is stated it should remove null.

Description:

    AnimalShelter() - Holds two PseudoQueue() instances for housing dogs and cats.
      - enqueue(animal) - Adds a cat or dog to the shelter as stated by animal (`enqueue('cat')`/`enqueue('dog')`).
      - dequeue(preference) - Removes animal of user preference from the shelter for adoption (`dequeue('cat')`/`dequeue('dog')`). Removes null if no preference is stated.

Credits:
- InvalidOperationError copied from [Class Repo](https://github.com/codefellows/seattle-python-401n2/blob/main/class-10/demo/stacks_and_queues/stacks_and_queues.py)
- Remaining classes (not including AnimalShelter) copied from `../queue_with_stacks.py`