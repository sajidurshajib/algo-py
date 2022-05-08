from typing import List


list_array = [2, 4, 1, 3, 9]


def merge(array: List):
    return


def merge_sort(array: List, l: int, r: int):
    if l < r:
        m = l+(r-l)//2
        merge_sort(array=array, l=l, r=m)
        merge_sort(array=array, l=m+1, r=r)


if __name__ == "__main__":
    merge_sort(array=list_array, l=0, r=len(list_array)-1)
