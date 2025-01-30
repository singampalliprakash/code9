#Bubble sort checks the first number and adjacent number if first number is largest and then
#  the maximum element goes end position and same way second largest element goes to second last by ysing swap.
arr = [5, 2, 9, 1, 5, 6]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array:", arr)