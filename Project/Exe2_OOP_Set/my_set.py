from typing import List, Optional, Any


class MySet:
    def __init__(self, elements: Optional[List[Any]] = None) -> None:
        """
        Initialize a new MySet instance.

        :param elements: List of initial elements. Duplicates will be removed.
        """
        self.data: List[Any] = []
        if elements:
            for element in elements:
                if element not in self.data:
                    self.data.append(element)

    def __str__(self) -> str:
        """
        Return a string representation of the MySet, with items separated by commas.
        """
        return ', '.join(str(item) for item in self.data)

    def __len__(self) -> int:
        """
        Return the number of unique elements in the MySet.
        """
        return len(self.data)

    def __repr__(self) -> str:
        """
        Provide a string representation of the MySet.
        """
        return f"MySet({self.data})"

    def union(self, other: 'MySet') -> 'MySet':
        """
        Return a new MySet containing all unique elements from this set and the other set.

        :param other: Another MySet instance.
        :return: A new MySet instance with the union of elements.
        """
        combined_elements = self.data + [item for item in other.data if item not in self.data]
        return MySet(combined_elements)

    def intersection(self, other: 'MySet') -> 'MySet':
        """
        Return a new MySet containing only elements present in both this set and the other set.

        :param other: Another MySet instance.
        :return: A new MySet instance with the intersection of elements.
        """
        common_elements = [item for item in self.data if item in other.data]
        return MySet(common_elements)

    def __sub__(self, other: Union['MySet', Any]) -> 'MySet':
        """
        Return a new MySet with the elements from the current set minus those in 'other'.
        If 'other' is a MySet, the result is the set difference.
        If 'other' is a single item, that item is removed from the set if it exists.

        :param other: Another MySet instance or a single item to be removed.
        :return: A new MySet instance with the subtraction of elements.
        """
        if isinstance(other, MySet):
            # Subtracting another MySet
            result_elements = [item for item in self.data if item not in other.data]
        else:
            # Subtracting a single item
            result_elements = [item for item in self.data if item != other]

        return MySet(result_elements)

    def powerset(self) -> 'MySet':
        """
        Return the powerset of the current set. The powerset is a set of all subsets,
        including the empty set and the set itself.

        :return: A new MySet instance containing all subsets of the current set.
        """
        if len(self.data) == 0:
            # Base case: the powerset of an empty set is a set containing the empty set
            return MySet([MySet()])

        # Recursive case: choose an item (first item) and generate all subsets
        first_item = self.data[0]
        remaining_items = MySet(self.data[1:])

        # Get the powerset of the remaining items
        smaller_powerset = remaining_items.powerset()

        # Create a new list to hold the powerset
        full_powerset: List[MySet] = []

        for subset in smaller_powerset.data:
            # Add the subset itself (without the first item)
            full_powerset.append(subset)
            # Add the subset with the first item included
            full_powerset.append(MySet([first_item] + subset.data))

        return MySet(full_powerset)


# Example usage:
A = MySet([1, 2, 3])
powerset_A = A.powerset()

for subset in powerset_A.data:
    print(subset)  # Output should be each subset of A
