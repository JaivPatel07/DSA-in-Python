def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):        # start from second element
        key = arr[i]             # element to be inserted
        j = i - 1

        # shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place key at correct position
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]
    insertion_sort(arr)
    print(arr)
