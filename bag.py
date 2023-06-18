# PLEASE NOTE: Skeleton code and test cases were provided by Oregon State University's Data Structures (CS 261) course.

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the Bag
        """
        self._da.append(value)


    def remove(self, value: object) -> bool:
        """
        Removes object from Bag
        Returns True if object removed
        Returns False if object not removed
        """
        # if Bag is empty
        if self.size() == 0:
            return False
        for index in range(self.size()):
            # if value found and is removed
            if self._da[index] == value:
                self._da.remove_at_index(index)
                return True
            # if value does not exist in array
            elif index == self.size() - 1 and self._da[index] != value:
                return False


    def count(self, value: object) -> int:
        """
        Returns the number of elements in a Bag that match provided value
        """
        count = 0
        for index in range(self.size()):
            if self._da[index] == value:
                # increase count if occurence of value is found
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the contents of the Bag
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Compares contents of one Bag to another Bag
        Returns True if same elements (in any order)
        Returns False if unequal
        """
        # if the two Bags are of different sizes
        if self.size() != second_bag.size():
            return False
        # if both Bags are empty
        if self.size() == 0 and second_bag.size() == 0:
            return True
        else:
            for index in range(self.size()):
                bag1_count = self.count(self._da[index])
                bag2_count = second_bag.count(self._da[index])
                if bag1_count == bag2_count:
                    continue
                else:
                    return False
        return True


    def __iter__(self):
        """
        Creates an iterator within the class
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Returns the next item in the Bag
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration
        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
