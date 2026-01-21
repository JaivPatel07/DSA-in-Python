def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i# assume current is smallest

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j# update smallest index

        # swap smallest with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print(arr)
