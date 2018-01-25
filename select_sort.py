# -*- coding: utf-8 -*-


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def select_sort(arr):
    result = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        result.append(arr.pop(smallest_index))
    return result

if __name__ == '__main__':
    arr = [1, 5, 3, 7, 9]
    print select_sort(arr)