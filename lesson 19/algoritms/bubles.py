def my_sort(arr):
    for i in range(1, len(arr)):
        for j in range (0, len(arr) -1):
            if arr[j] > arr[j +1]:
                arr[j],arr[j +1] = arr[j+1] , arr[j]
    return arr

print(my_sort([3,5,7,87,9,5,76,45,3]))