from typing import List


list_array = [2, 4, 1, 3, 9]


def selection(array: List):
    size = len(array)

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        # fix min correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

    print(array)


if __name__ == "__main__":
    selection(array=list_array)
