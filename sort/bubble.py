from typing import List

list_array = [2, 4, 1, 3, 9]


def bubble_sort(array: List):
    size = len(array)

    step = 0
    while step < size - 1:
        i = 0
        while i < size - step - 1:
            # swap
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            i += 1
        step += 1

    print(array)


if __name__ == "__main__":
    bubble_sort(array=list_array)
