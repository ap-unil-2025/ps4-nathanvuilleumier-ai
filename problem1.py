"""
Problem 1: List Operations and Comprehensions
Practice working with Python lists - creating, modifying, filtering, and transforming them.
"""


def create_number_list(start, end):
    """
    Create a list of numbers from start to end (inclusive).

    Args:
        start (int): Starting number
        end (int): Ending number

    Returns:
        list: List of numbers from start to end

    Example:
        >>> create_number_list(1, 5)
        [1, 2, 3, 4, 5]
    """
    # TODO: Implement this function
    nums=[]
    for n in range(start, end+1):
        nums.append(n)
    return nums
    
    # Hint: Use range() and convert to list
    


def filter_even_numbers(numbers):

    l2=[]
    for i in numbers:
        if i%2==0:
            l2.append(i)
    return(l2)

    """
    Return a new list containing only the even numbers.

    Args:
        numbers (list): List of integers

    Returns:
        list: List of even numbers only

    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    # TODO: Implement this function
    # You can use a loop or list comprehension
    


def square_numbers(numbers):
    """
    Return a new list with each number squared.

    Args:
        numbers (list): List of numbers

    Returns:
        list: List where each element is squared

    Example:
        >>> square_numbers([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    # TODO: Implement this function
    # Hint: Try a list comprehension!
    l=[]
    for i in numbers:
        i=i*i
        l.append(i)
    return (l)



def find_max_min(numbers):
    """
    Find the maximum and minimum values in a list.

    Args:
        numbers (list): List of numbers

    Returns:
        tuple: (max_value, min_value)

    Example:
        >>> find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
        (9, 1)
    """
    # TODO: Implement this function
    # You can use max() and min() built-in functions
    

    return (max(numbers),min(numbers))


def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving order.
    """
    result = []
    for item in items:
        if item not in result:   # keep first occurrence only
            result.append(item)
    return result




def merge_lists(list1, list2):
    """
    Merge two lists, alternating elements from each.
    If one list is longer, append remaining elements.
    """
    result = []
    i = j = 0
    n1, n2 = len(list1), len(list2)

    # Alternate while both have elements left
    while i < n1 and j < n2:
        result.append(list1[i]); i += 1
        result.append(list2[j]); j += 1

    # Append leftovers
    if i < n1:
        result.extend(list1[i:])
    if j < n2:
        result.extend(list2[j:])

    return result

    
def list_statistics(numbers):
    """
    Calculate statistics for a list of numbers.
    Returns: dict with keys 'sum', 'average', 'count', 'max', 'min'
    """
    if not numbers:
        raise ValueError("numbers must be a non-empty list")

    total = sum(numbers)
    count = len(numbers)
    avg = total / count

    return {
        'sum': total,
        'average': avg,
        'count': count,
        'max': max(numbers),
        'min': min(numbers)
    }


    # TODO: Implement this function
    # Calculate and return a dictionary with the statistics
    pass


def chunk_list(items, chunk_size):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    chunks = []
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i:i + chunk_size])
    return chunks

    
    # TODO: Implement this function
    # Hint: Use list slicing in a loop
    pass


# Test cases
if __name__ == "__main__":
    print("Testing List Operations...")
    print("-" * 50)

    # Test create_number_list
    print("Test 1: create_number_list(1, 5)")
    result = create_number_list(1, 5)
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test filter_even_numbers
    print("Test 2: filter_even_numbers([1, 2, 3, 4, 5, 6])")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"Result: {result}")
    assert result == [2, 4, 6], "Failed!"
    print("✓ Passed\n")

    # Test square_numbers
    print("Test 3: square_numbers([1, 2, 3, 4])")
    result = square_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    assert result == [1, 4, 9, 16], "Failed!"
    print("✓ Passed\n")

    # Test find_max_min
    print("Test 4: find_max_min([3, 1, 4, 1, 5, 9, 2, 6])")
    result = find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Result: {result}")
    assert result == (9, 1), "Failed!"
    print("✓ Passed\n")

    # Test remove_duplicates
    print("Test 5: remove_duplicates([1, 2, 2, 3, 4, 3, 5])")
    result = remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test merge_lists
    print("Test 6: merge_lists([1, 3, 5], [2, 4, 6])")
    result = merge_lists([1, 3, 5], [2, 4, 6])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5, 6], "Failed!"
    print("✓ Passed\n")

    # Test list_statistics
    print("Test 7: list_statistics([1, 2, 3, 4, 5])")
    result = list_statistics([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    expected = {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    assert result == expected, "Failed!"
    print("✓ Passed\n")

    # Test chunk_list
    print("Test 8: chunk_list([1, 2, 3, 4, 5, 6, 7], 3)")
    result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"Result: {result}")
    assert result == [[1, 2, 3], [4, 5, 6], [7]], "Failed!"
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work!")
