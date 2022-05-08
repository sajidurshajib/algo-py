from typing import List


list_array = [2, 4, 1, 3, 9]


def insertion(array: List):
    size = len(array)

    for step in range(1, size):
        key = array[step]
        j = step - 1

        # go back and set value
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

    print(array)


if __name__ == "__main__":
    insertion(array=list_array)
