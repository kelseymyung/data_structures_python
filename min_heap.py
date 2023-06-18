# PLEASE NOTE: Skeleton code and test cases were provided by Oregon State University's Data Structures (CS 261) course.

from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new element to heap while maintaining integrity
        """
        # identifies if heap needs to be resized before add
        if self._heap.length() == self._heap.get_capacity:
            self._heap.resize()
        # appends new value to end of heap
        self._heap.append(node)
        new_index = self._heap.length() - 1
        new_value = self._heap.get_at_index(new_index)
        parent_index = (new_index - 1) // 2
        # if parent is less than 0, value will be the new root
        if parent_index < 0:
            parent_index = 0
            parent_value = self._heap.get_at_index(parent_index)
        else:
            parent_value = self._heap.get_at_index(parent_index)
        while parent_value >= new_value and new_index > 0:
            # swap parent and new
            self._heap.set_at_index(new_index, parent_value)
            self._heap.set_at_index(parent_index, new_value)
            # update variables
            new_index = parent_index
            parent_index = (new_index - 1) // 2
            if parent_index < 0:
                parent_index = 0
            parent_value = self._heap.get_at_index(parent_index)


    def is_empty(self) -> bool:
        """
        Returns True if heap is empty
        Returns False if heap is not empty
        """
        if self._heap.length() == 0:
            return True
        else:
            return False


    def get_min(self) -> object:
        """
        Returns the min or root of the heap
        """
        if self.is_empty() == True:
            raise MinHeapException
        min_object = self._heap.get_at_index(0)
        return min_object


    def remove_min(self) -> object:
        """
        Removes minimum value of heap and maintains heap integrity
        """
        # if heap is empty, raise exception
        if self._heap.is_empty() == True:
            raise MinHeapException
        else:
            min_object = self._heap.get_at_index(0)
            # if heap only has one value, empty heap
            if self._heap.length() == 1:
                new_heap = DynamicArray()
                self._heap = new_heap
                return min_object
            else:
                # replaces min value with last value in array
                last_index = self._heap.length() - 1
                last_value = self._heap.get_at_index(last_index)
                self._heap.set_at_index(0, last_value)
                # removes last value in array
                self._heap.remove_at_index(last_index)
                new_length = self._heap.length()
                curr_index = 0
                curr_val = self._heap.get_at_index(0)
                # calculate children indices and values
                child_1_index = (2 * curr_index) + 1
                child_2_index = child_1_index + 1
                if child_1_index < new_length:
                    child_1_val = self._heap.get_at_index(child_1_index)
                else:
                    child_1_val = None
                if child_2_index < new_length:
                    child_2_val = self._heap.get_at_index(child_2_index)
                else:
                    child_2_val = None
                # percolates new min value down heap until integrity is reached
                while child_1_index < new_length or child_2_index < new_length:
                    if child_2_val == None or child_1_val <= child_2_val:
                        if child_1_val < curr_val:
                            self._heap.set_at_index(curr_index, child_1_val)
                            self._heap.set_at_index(child_1_index, curr_val)
                            curr_index = child_1_index
                            child_1_index = (curr_index * 2) + 1
                            child_2_index = child_1_index + 1
                            if child_1_index < new_length:
                                child_1_val = self._heap.get_at_index(child_1_index)
                            else:
                                child_1_val = None
                            if child_2_index < new_length:
                                child_2_val = self._heap.get_at_index(child_2_index)
                            else:
                                child_2_val = None
                        else:
                            return min_object
                    else:
                        if child_1_val == None or child_2_val < curr_val:
                            self._heap.set_at_index(curr_index, child_2_val)
                            self._heap.set_at_index(child_2_index, curr_val)
                            curr_index = child_2_index
                            child_1_index = (curr_index * 2) + 1
                            child_2_index = child_1_index + 1
                            if child_1_index < new_length:
                                child_1_val = self._heap.get_at_index(child_1_index)
                            else:
                                child_1_val = None
                            if child_2_index < new_length:
                                child_2_val = self._heap.get_at_index(child_2_index)
                            else:
                                child_2_val = None
                        else:
                            return min_object
                return min_object


    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a heap from an unsorted array
        Time complexity: O(n)
        """
        new_da = DynamicArray()
        new_da.merge(da)
        last_index = new_da.length() - 1
        curr_index = (last_index - 1)//2
        # if curr_index < self._heap.length():
        while curr_index > -1:
            curr_val = new_da.get_at_index(curr_index)
            # calculate children indices and values
            child_1_index = (2 * curr_index) + 1
            child_2_index = child_1_index + 1
            if child_1_index <= last_index:
                child_1_val = new_da.get_at_index(child_1_index)
            else:
                child_1_val = None
            if child_2_index <= last_index:
                child_2_val = new_da.get_at_index(child_2_index)
            else:
                child_2_val = None
            next_index = curr_index - 1
            # percolates new min value down heap until integrity is reached
            while child_1_index <= last_index or child_2_index <= last_index:
                if child_2_val == None or child_1_val <= child_2_val:
                    if child_1_val < curr_val:
                        new_da.set_at_index(curr_index, child_1_val)
                        new_da.set_at_index(child_1_index, curr_val)
                        curr_index = child_1_index
                        child_1_index = (curr_index * 2) + 1
                        child_2_index = child_1_index + 1
                        if child_1_index <= last_index:
                            child_1_val = new_da.get_at_index(child_1_index)
                        else:
                            child_1_val = None
                        if child_2_index <= last_index:
                            child_2_val = new_da.get_at_index(child_2_index)
                        else:
                            child_2_val = None
                    else:
                        break
                else:
                    if child_1_val == None or child_2_val < curr_val:
                        new_da.set_at_index(curr_index, child_2_val)
                        new_da.set_at_index(child_2_index, curr_val)
                        curr_index = child_2_index
                        child_1_index = (curr_index * 2) + 1
                        child_2_index = child_1_index + 1
                        if child_1_index <= last_index:
                            child_1_val = new_da.get_at_index(child_1_index)
                        else:
                            child_1_val = None
                        if child_2_index <= last_index:
                            child_2_val = new_da.get_at_index(child_2_index)
                        else:
                            child_2_val = None
                    else:
                        break
            curr_index = next_index
        self._heap = new_da


    def size(self) -> int:
        """
        Returns size of heap
        """
        heap_size = self._heap.length()
        return heap_size


    def clear(self) -> None:
        """
        Clears heap completely, begins with empty heap
        """
        new_heap = DynamicArray()
        self._heap = new_heap


def heapsort(da: DynamicArray) -> None:
    """
    Receives a DynamicArray and sorts it into non-ascending order
    """
    # to build heap
    last_index = da.length() - 1
    curr_index = (last_index - 1) // 2
    # if curr_index < self._heap.length():
    while curr_index > -1:
        curr_val = da.get_at_index(curr_index)
        # calculate children indices and values
        child_1_index = (2 * curr_index) + 1
        child_2_index = child_1_index + 1
        if child_1_index <= last_index:
            child_1_val = da.get_at_index(child_1_index)
        else:
            child_1_val = None
        if child_2_index <= last_index:
            child_2_val = da.get_at_index(child_2_index)
        else:
            child_2_val = None
        next_index = curr_index - 1
        # percolates new min value down heap until integrity is reached
        while child_1_index <= last_index or child_2_index <= last_index:
            if child_2_val == None or child_1_val <= child_2_val:
                if child_1_val < curr_val:
                    da.set_at_index(curr_index, child_1_val)
                    da.set_at_index(child_1_index, curr_val)
                    curr_index = child_1_index
                    child_1_index = (curr_index * 2) + 1
                    child_2_index = child_1_index + 1
                    if child_1_index <= last_index:
                        child_1_val = da.get_at_index(child_1_index)
                    else:
                        child_1_val = None
                    if child_2_index <= last_index:
                        child_2_val = da.get_at_index(child_2_index)
                    else:
                        child_2_val = None
                else:
                    break
            else:
                if child_1_val == None or child_2_val < curr_val:
                    da.set_at_index(curr_index, child_2_val)
                    da.set_at_index(child_2_index, curr_val)
                    curr_index = child_2_index
                    child_1_index = (curr_index * 2) + 1
                    child_2_index = child_1_index + 1
                    if child_1_index <= last_index:
                        child_1_val = da.get_at_index(child_1_index)
                    else:
                        child_1_val = None
                    if child_2_index <= last_index:
                        child_2_val = da.get_at_index(child_2_index)
                    else:
                        child_2_val = None
                else:
                    break
        curr_index = next_index
    # to sort built heap
    sorted_index = da.length() - 1
    while sorted_index > -1:
        min_val = da.get_at_index(0)
        sort_val = da.get_at_index(sorted_index)
        da.set_at_index(sorted_index, min_val)
        da.set_at_index(0, sort_val)
        sorted_index -= 1
        curr_index = 0
        # calculate children indices and values
        child_1_index = (2 * curr_index) + 1
        child_2_index = child_1_index + 1
        if child_1_index <= sorted_index:
            child_1_val = da.get_at_index(child_1_index)
        else:
            child_1_val = None
        if child_2_index <= sorted_index:
            child_2_val = da.get_at_index(child_2_index)
        else:
            child_2_val = None
        # percolates new min value down heap until integrity is reached
        while child_1_index <= sorted_index or child_2_index <= sorted_index:
            if child_2_val == None or child_1_val <= child_2_val:
                if child_1_val < sort_val:
                    da.set_at_index(curr_index, child_1_val)
                    da.set_at_index(child_1_index, sort_val)
                    curr_index = child_1_index
                    child_1_index = (curr_index * 2) + 1
                    child_2_index = child_1_index + 1
                    if child_1_index <= sorted_index:
                        child_1_val = da.get_at_index(child_1_index)
                    else:
                        child_1_val = None
                    if child_2_index <= sorted_index:
                        child_2_val = da.get_at_index(child_2_index)
                    else:
                        child_2_val = None
                else:
                    break
            else:
                if child_1_val == None or child_2_val < sort_val:
                    da.set_at_index(curr_index, child_2_val)
                    da.set_at_index(child_2_index, sort_val)
                    curr_index = child_2_index
                    child_1_index = (curr_index * 2) + 1
                    child_2_index = child_1_index + 1
                    if child_1_index <= sorted_index:
                        child_1_val = da.get_at_index(child_1_index)
                    else:
                        child_1_val = None
                    if child_2_index <= sorted_index:
                        child_2_val = da.get_at_index(child_2_index)
                    else:
                        child_2_val = None
                else:
                    break




# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent_index: int) -> None:
    """
    Percolates parent node down in heap to preserve heap integrity
    """
    last_index = da.length() - 1
    parent_val = da.get_at_index(parent_index)
    # calculate children indices and values
    child_1_index = (2 * parent_index) + 1
    child_2_index = child_1_index + 1
    if child_1_index <= last_index:
        child_1_val = da.get_at_index(child_1_index)
    else:
        child_1_val = None
    if child_2_index <= last_index:
        child_2_val = da.get_at_index(child_2_index)
    else:
        child_2_val = None
    next_index = parent_index - 1
    # percolates new min value down heap until integrity is reached
    while child_1_index <= last_index or child_2_index <= last_index:
        if child_2_val == None or child_1_val <= child_2_val:
            if child_1_val < parent_val:
                da.set_at_index(curr_index, child_1_val)
                da.set_at_index(child_1_index, parent_val)
                curr_index = child_1_index
                child_1_index = (curr_index * 2) + 1
                child_2_index = child_1_index + 1
                if child_1_index <= last_index:
                    child_1_val = da.get_at_index(child_1_index)
                else:
                    child_1_val = None
                if child_2_index <= last_index:
                    child_2_val = da.get_at_index(child_2_index)
                else:
                    child_2_val = None
            else:
                break
        else:
            if child_1_val == None or child_2_val < parent_val:
                da.set_at_index(curr_index, child_2_val)
                da.set_at_index(child_2_index, parent_val)
                curr_index = child_2_index
                child_1_index = (curr_index * 2) + 1
                child_2_index = child_1_index + 1
                if child_1_index <= last_index:
                    child_1_val = da.get_at_index(child_1_index)
                else:
                    child_1_val = None
                if child_2_index <= last_index:
                    child_2_val = da.get_at_index(child_2_index)
                else:
                    child_2_val = None
            else:
                break






# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
