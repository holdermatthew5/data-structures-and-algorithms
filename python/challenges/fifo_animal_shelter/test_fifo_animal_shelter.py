import pytest
from fifo_animal_shelter import InvalidOperationError, AnimalShelter, PseudoQueue, Stack

def test_enqueue_cat():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    assert shelter.cats.front.value == 'cat'

def test_enqueue_dog():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    assert shelter.dogs.front.value == 'dog'

def test_dequeue_cat():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    assert shelter.dequeue('cat').value == 'cat'

def test_dequeue_dog():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    assert shelter.dequeue('dog').value == 'dog'

def test_enqueue_two_cats():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    assert shelter.cats.front.value == 'cat' and shelter.cats.rear.value == 'cat'

def test_enqueue_two_dogs():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    assert shelter.dogs.front.value == 'dog' and shelter.dogs.rear.value == 'dog'

def test_dequeue_two_cats():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    shelter.dequeue('cat')
    shelter.dequeue('cat')
    assert not shelter.cats.front and not shelter.cats.rear

def test_dequeue_two_dogs():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.dequeue('dog')
    shelter.dequeue('dog')
    assert not shelter.dogs.front and not shelter.dogs.rear