from typing import Optional, List, Any

from Project.Exe2_OOP_Set.my_set import MySet


class IntSet(MySet):
    def __init__(self, elements: Optional[List[Any]] = None) -> None:
        """
        Initialize a new IntSet instance. Ensures all elements are integers.

        :param elements: List of initial elements. All elements must be integers.
        :raises ValueError: If any element is not an integer.
        """
        if elements:
            for element in elements:
                if not isinstance(element, int):
                    raise ValueError("All elements should be ints")

        # Call the constructor of the parent class MySet
        super().__init__(elements)


# Example usage:
try:
    valid_int_set = IntSet([1, 2, 3])
    print(valid_int_set)  # Should print: 1, 2, 3

    invalid_int_set = IntSet([1, 2, 'a'])  # Should raise ValueError
except ValueError as e:
    print(e)  # Should print: "All elements should be ints"
