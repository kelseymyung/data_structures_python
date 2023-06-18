# PLEASE NOTE: Skeleton code and test cases, were provided by Oregon State University's Data Structures (CS 261) course.

from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            # print(index, value, self._size, self._capacity)
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the storage for a dynamic array
        Exits if new_capacity is less than current capacity or a negative value
        """
        if new_capacity >= self.length() and new_capacity > 0:
            # new capacity must be a positive integer and not smaller than current size
            new_data = StaticArray(new_capacity)
            self._capacity = new_capacity
            for index in range(self.length()): # copying pre-existing elements over to new array
                new_data.set(index, self.get_at_index(index))
            self._data = new_data


    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array
        If internal capacity is full, doubles capacity
        """
        if self._size < self._capacity: # if size is less than capacity
            self._size = self._size + 1
            self.set_at_index(self._size-1, value)
        elif self._size == self._capacity: # if size is at capacity
            self.resize(2 * self._capacity) # increase capacity
            self._size = self._size + 1
            self.set_at_index(self._size-1, value)


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at an index
        Exception if invalid index
        If capacity is reached, array is resized
        """
        if index < 0 or index >= self._size + 1: # valid indices are [0, N] inclusive
            raise DynamicArrayException
        if self._size == self._capacity:
            # resize array if at capacity
            self.resize(2 * self._capacity)
        if index == self._capacity - 1:
            # if given index is at the end of the array
            self.append(value)
        else:
            # insert new value and then move all other values over by 1 index
            curr_placeholder = value
            next_placeholder = self._data[index]
            self._size += 1
            for index in range(index, self._size):
                if index == self._size - 1:
                    self._data[index] = curr_placeholder
                else:
                    self._data[index] = curr_placeholder
                    curr_placeholder = next_placeholder
                    next_placeholder = self._data[index + 1]



    def remove_at_index(self, index: int) -> None:
        """
        Removes a value at a specific index
        Exception if invalid index
        If size before removal is less than 1/4 of capacity,
        array is resized to double the num of elements
        """
        if index < 0 or index >= self._size: # valid indicies are [0, N-1] inclusive
            raise DynamicArrayException
        elif self._size < (self._capacity / 4) and self._capacity > 10:
            # decreases capacity under certain circumstances
            # size is less than 1/4 capacity and capacity is greater than 10
            if (self._size * 2) > 10:
                self.resize(self._size * 2)
            elif (self._size * 2) < 10:
                # new capacity will not be less than 10
                self.resize(10)
        self._size -= 1
        for index in range(index, self._size + 1):
            if index == self._size:
                self._data[index] = None
            else:
                self._data[index] = self._data[index + 1]




    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new DynamicArray that contains requested number of elements
        beginning at the requested index
        """
        if start_index >= self._size or start_index + size > self._size \
                or start_index < 0 or size < 0:
            # valid indices are [0, N-1] inclusive
            raise DynamicArrayException
        if size == 1:
            new_da = DynamicArray()
            new_da.append(self._data[start_index])
            return new_da
        if size == 0:
            new_da = DynamicArray()
            return new_da
        else:
            new_da = DynamicArray()
            new_data = StaticArray(self._size - start_index + size + 1)
            for index in range(start_index, start_index + size):
                new_da.append(self._data[index])
            return new_da


    def merge(self, second_da: "DynamicArray") -> None:
        """
        Merges two DynamicArrays in same order of input array
        """
        for index in range(0, second_da._size):
            # adds second DynamicArray to first DynamicArray
            self.append(second_da[index])


    def map(self, map_func) -> "DynamicArray":
        """
        Creates a new DynamicArray where
        each value is passed through a function
        """
        new_da = DynamicArray()
        for index in range(self._size):
            # adds new values to new DynamicArray
            new_da.append(map_func(self._data[index]))
        return new_da



    def filter(self, filter_func) -> "DynamicArray":
        """
        Creates a new DynamicArray populated only with elements
        from original Array that return True through filter_func
        """
        new_da = DynamicArray()
        for index in range(self._size):
            # adds only the values to new DynamicArray that return True
            if filter_func(self._data[index]) == True:
                new_da.append(self._data[index])
        return new_da



    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies the reduce_func to tall elements of the array
        Returns the resulting value
        If initializer is None, begins at first index
        """
        if initializer == None:
            # if initializer is None, initializer is first value in array
            current_x = self._data[0]
        elif self._size == 0:
            # if array is empty, return initializer value
            return initializer
        else:
            # sets initializer as first current x value
            current_x = reduce_func(initializer, self._data[0])
        for index in range(0, self._size):
            if index == self._size - 1:
                # if final index
                return current_x
            else:
                # updates current x for next index
                current_x = reduce_func(current_x, self._data[index + 1])



def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Returns a tuple that contains the most frequent values of the given array
    and the frequency count
    """
    mode_da = DynamicArray()
    curr_most_freq_val_count = 1
    compared_val_count = 1
    for index in range(0, arr.length()):
        # for final value of array
        if index == arr.length() - 1:
            # if final value has same frequency as the most frequent values
            if compared_val_count == curr_most_freq_val_count:
                mode_da.append(arr[index])
                return (mode_da, curr_most_freq_val_count)
            # if final value has the new highest frequency
            elif compared_val_count > curr_most_freq_val_count:
                mode_da = DynamicArray()
                mode_da.append(arr[index])
                curr_most_freq_val_count = compared_val_count
                return (mode_da, curr_most_freq_val_count)
            # if final value is less frequent than current frequency
            elif compared_val_count < curr_most_freq_val_count:
                return (mode_da, curr_most_freq_val_count)
        # if next value is the same as current value
        elif arr[index] == arr[index + 1]:
            compared_val_count += 1
        # if next value is different as current value, evaluate frequency
        elif arr[index] != arr[index + 1]:
            # less frequent than current frequency
            if compared_val_count < curr_most_freq_val_count:
                compared_val_count = 1
            # same frequency as current frequency, adds to current DynamicArray
            if compared_val_count == curr_most_freq_val_count:
                if mode_da.get_capacity() == mode_da.length():
                    mode_da.resize(mode_da.get_capacity() * 2)
                mode_da.append(arr[index])
                compared_val_count = 1
            # higher frequency than current frequency, updates DynamicArray and current frequency
            if compared_val_count > curr_most_freq_val_count:
                mode_da = DynamicArray()
                mode_da.append(arr[index])
                curr_most_freq_val_count = compared_val_count
                compared_val_count = 1
    return (mode_da, curr_most_freq_val_count)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")



    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
