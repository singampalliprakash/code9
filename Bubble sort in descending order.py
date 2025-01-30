arr = [3, 1, 4, 1, 5, 9]
n = len(arr)

for i in range(n):

    for j in range(0, n-i-1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array in dezscending order:", arr)