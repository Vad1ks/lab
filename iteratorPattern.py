from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: StudentsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class StudentsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def __getitem__(self, item):
        return item

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    students = StudentsCollection()
    students.add_item("Diploma Student needs 1 more month to do his task")
    students.add_item("Course Project Student needs 1 more day to do his task")
    students.add_item("Lab task Student needs 1 more hour to do his task")

    print("Straight traversal:")
    print("\n".join(students))
    print("")

    print("Reverse traversal:")
    print("\n".join(students.get_reverse_iterator()), end="")
