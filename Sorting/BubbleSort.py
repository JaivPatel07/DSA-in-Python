def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:     # no swap → stop early
            break

if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2]
    bubble_sort(arr)
    print(arr)
