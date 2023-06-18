import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    Returns the min and max value of an array
    """
    min = arr[0]
    max = arr[0]
    for index in range(arr.length()):
        if arr[index] <= min:       # if compared val is less than or equal to min val
            min = arr[index]
        elif arr[index] >= max:     # if compared val is greater than or equal to max val
            max = arr[index]
    return (min, max)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Returns numbers in an array as "fizz", "buzz", or "fizzbuzz"
    if a multiple of 3, 5, or both respectively
    """
    fizzbuzz_arr = StaticArray(arr.length())
    for index in range(arr.length()):
        if arr[index] % 3 == 0 and arr[index] % 5 == 0:   # if val is divisible by 3 and 5
            fizzbuzz_arr.set(index, "fizzbuzz")
        elif arr[index] % 3 == 0:               # if val is divisible by 3
            fizzbuzz_arr.set(index, "fizz")
        elif arr[index] % 5 == 0:               # if val is divisible by 5
            fizzbuzz_arr.set(index, "buzz")
        else:
            fizzbuzz_arr.set(index, arr[index])
    return fizzbuzz_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Changes a static array in reversed order
    """
    back_count = 1
    for index in range(arr.length()):
        if back_count > arr.length() / 2:          # if median of array is reached, end
            break
        new_back = arr[index]
        new_front = arr[(arr.length() - back_count)]
        arr.set((index), new_front)
        arr.set((arr.length() - back_count), new_back)
        back_count += 1


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Returns a Static Array with rotation based on steps
    (negative to the L, positive to the R)
    """
    rotated_arr = StaticArray(arr.length())
    if steps == 0:                          # if steps are 0, return original array
        for index in range(arr.length()):
            rotated_arr.set(index, arr[index])
        return rotated_arr
    simplified_move = abs(steps) % arr.length()   # removes full rotations from step count
    if steps > 0:                               # if step count is positive (move R)
        for index in range(arr.length()):
            new_pos = index + simplified_move
            if new_pos > (arr.length() - 1):       # if val reaches past end of array
                carry_over_steps = new_pos - arr.length()
                rotated_arr.set(carry_over_steps, arr[index])
            else:
                rotated_arr.set(new_pos, arr[index])
        return rotated_arr
    if steps < 0:                               # if step count is negative (move L)
        for index in range(arr.length()):
            new_pos = index - simplified_move
            if new_pos < 0:                  # if val reaches past beginning of array
                carry_over_steps = arr.length() - abs(new_pos)
                rotated_arr.set(carry_over_steps, arr[index])
            else:
                rotated_arr.set(new_pos, arr[index])
        return rotated_arr



# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Returns a StaticArray containing all consecutive integers when given a start and end
    """
    if end >= start:        # for ascending arrays
        array_size = abs(end - start + 1)
    if end < start:         # for descending arrays
        array_size = abs(start - end + 1)
    range_array = StaticArray(array_size)
    if end >= start:        # descending array
        index = 0
        for value in range(start, end + 1):
            range_array.set(index, value)
            index += 1
    if end < start:         # ascending array
        index = 0
        for value in range(start, end - 1, -1):
            range_array.set(index, value)
            index += 1
    return range_array



# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Returns 1 if array is sorted in ascending order, -1 if descending, 0 if other
    """
    consecutive_count = 0
    for index in range(arr.length()):
        if index == arr.length() - 1:       # when end of array is reached, find return value
            if consecutive_count == arr.length() - 1:       # ascending order
                return 1
            if consecutive_count == -(arr.length() - 1):    # descending order
                return -1
            else:                                    # neither ascending or descending order
                return 0
        if arr[index+1] > arr[index]:
            consecutive_count += 1
        if arr[index+1] < arr[index]:
            consecutive_count -= 1
        if arr[index+1] == arr[index]:
            continue


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    Returns a tuple containing the most frequent value and the value's frequency count
    """
    curr_most_freq_val = arr[0]
    curr_most_freq_val_count = 1
    compared_val = arr[0]
    compared_val_count = 1
    for index in range(arr.length() - 1):
        if arr[index] == arr[index + 1]:    # val count increased if next val is the same
            compared_val_count += 1
        else:
            if compared_val_count <= curr_most_freq_val_count:  # resets compared_val variables
                compared_val = arr[index + 1]
                compared_val_count = 1
            else:             # updates most freq val variables and resets compared val variables
                curr_most_freq_val = compared_val
                curr_most_freq_val_count = compared_val_count
                compared_val = arr[index + 1]
                compared_val_count = 1
    if compared_val_count > curr_most_freq_val_count:
            curr_most_freq_val_count = compared_val_count
            curr_most_freq_val = compared_val
            return (curr_most_freq_val, curr_most_freq_val_count)
    else:
        return (curr_most_freq_val, curr_most_freq_val_count)



# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Returns a new StaticArray with all duplicates removed
    """
    new_array_size = arr.length()
    if arr.length() == 1:       # if given array has length of 1, return original array
        arr_no_dup = StaticArray(1)
        arr_no_dup.set(0, arr[0])
        return arr_no_dup
    for index in range(arr.length()):   # finds new array size without duplicates
        if index == arr.length() - 1:
            continue
        if arr[index] == arr[index + 1]:
            new_array_size -= 1
        else:
            continue
    arr_no_dup = StaticArray(new_array_size)
    no_dup_index = 0
    for index in range(arr.length()):
        if no_dup_index == new_array_size - 1:      # if end of array is reached
            arr_no_dup[no_dup_index] = arr[index]
            return arr_no_dup
        if arr[index] == arr[index + 1]:   # if duplicate is found, do not enter in new array
            continue
        if arr[index] != arr[index + 1]:
            arr_no_dup[no_dup_index] = arr[index]
            no_dup_index += 1


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray and returns a new StaticArray in non-ascending order
    """
    min = arr[0]
    max = arr[0]
    for index in range(arr.length()):       # finds min and max of array
        if arr[index] <= min:
            min = arr[index]
        elif arr[index] >= max:
            max = arr[index]
        else:
            continue
    range_count_arr = abs(max - min + 1)    # range of count array
    count_arr = StaticArray(range_count_arr)
    if arr.length() == 1:
        count_arr = StaticArray(1)
        count_arr.set(0, arr[0])
    # for count_arr: sets val as index and frequency as val
    for index in range(count_arr.length()):     # sets all None values to 0
        count_arr.set(index, 0)
    for index in range(arr.length()):
        count_index = arr[index] - min
        curr_freq = count_arr[count_index]
        count_arr.set(count_index, curr_freq + 1)
    # for final sort
    final_sort = StaticArray(arr.length())
    curr_index = 0
    for index in range(max - min, -1, -1):  # uses info from count array for final sort array
        final_val = index + min
        val_freq = count_arr[index]
        for val in range(val_freq):
            final_sort.set(curr_index, final_val)
            curr_index += 1
    return final_sort


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Returns a StaticArray of the squares of values
    """
    sorted_sq_arr = StaticArray(arr.length())
    left_index = 0
    right_index = arr.length() - 1
    sorted_index = 0
    if arr[0] >= 0:     # if all values are 0 or positive, return in same order
        for index in range(arr.length()):
            sorted_sq_arr.set(index, arr[index]**2)
        return sorted_sq_arr
    if arr[arr.length() - 1] <= 0:   # if all values are 0 or negative, return in opposite order
        for index in range(arr.length()):
            sorted_sq_arr.set(arr.length() - 1 - index, arr[index]**2)
        return sorted_sq_arr
    else:
        for index in range(arr.length()):
            if sorted_index == arr.length():    # if end of array is reached
                return sorted_sq_arr
            if abs(arr[left_index]) >= abs(arr[right_index]):
                sorted_sq_arr.set(arr.length() - 1 - sorted_index, arr[left_index]**2)
                left_index += 1
                sorted_index += 1
            else:
                sorted_sq_arr.set(arr.length() - 1 - sorted_index, arr[right_index]**2)
                right_index -= 1
                sorted_index += 1
        return sorted_sq_arr


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")


    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)



    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')

