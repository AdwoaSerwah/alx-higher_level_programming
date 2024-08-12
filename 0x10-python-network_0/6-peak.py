#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    A peak element is one that is not smaller than its neighbors.
    If the list is empty, the function returns None.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: A peak element in the list or None if the list is empty.
    """
    if not list_of_integers:
        return None

    def binary_search_peak(low, high):
        if low == high:
            return list_of_integers[low]
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return binary_search_peak(mid + 1, high)
        else:
            return binary_search_peak(low, mid)

    return binary_search_peak(0, len(list_of_integers) - 1)
