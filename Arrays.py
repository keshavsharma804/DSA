# # Iterate Python Program to print alternate elements
# def aler(arr):
#     res = []
#     for i in range(0, len(arr), 2):
#         res.append(arr[i])
#     return res

# arr = [10, 20, 30, 40, 50]
# res = aler(arr)
# print(" ".join(map(str, res)))



## Find Second Smallest and Second Largest
# def sort(arr):
#     sorted_arr = sorted(arr)
#     second_smallest = sorted_arr[1]
#     second_largest = sorted_arr[-2]
#     return second_smallest, second_largest

# arr = [15, 14, 5, 25, 44, 23]
# secnd_smallest, secnd_largest  = sort(arr)
# print("Second Smallest:", secnd_smallest)
# print("Second Largest:", secnd_largest)


##
# def sort(arr):
#     for i in range(len(arr) -1):
#         if arr[i] >  arr[i+1]:
#             return False
#     return True
# arr = [15,14, 25, 4]
# check = sort(arr)
# print(check)




# Left rotate the array by one
# def left_rotate(arr):
#     # Store the first element of the array
#     first_element = arr[0]
    
#     # Shift all elements one position to the left
#     for i in range(1, len(arr)):
#         arr[i - 1] = arr[i]
    
#     # Place the first element at the last position
#     arr[-1] = first_element

# arr = [4, 3, 5, 2, 1]
# left_rotate(arr)
# print("Array after left rotation by one:", arr)


##Two Sum
# def two(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             return [i, j]
#     return [-1. -1]

# arr = [2, 7, 11, 15]
# target = 9
# print(two(arr, target))


# sort the array without using inbuilt sort functions.
# def sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# array = [2,0,2,1,1,0]
# print("Array sorted by absolute values:", sort(array))


## Majority Element that occurs more than N/2 times
# def cnt(arr):
#     n = len(arr)
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[j] == arr[i]:
#                 count+= 1
#         if count > (n//2):
#             return arr[i]
#     return -1

# arr = [2, 2, 1, 1, 1, 2, 2]
# ans = cnt(arr)
# print("The majority element is:", ans)


# # Move Zeros to end (CG)
# def moveZeros(a):
#     pos = 0  
    
#     for i in range(len(a)):
#         if a[i] != 0:
#             a[pos], a[i] = a[i], a[pos]  
#             pos += 1
#     return a

# arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# ans = moveZeros(arr)
# print(*ans)  

   
# def peakElement(arr):
#     n = len(arr)
#     if n == 1:
#         return "true" 

#     if arr[0] > arr[1]:
#         return "true"
#     if arr[-1] > arr[-2]:
#         return "true"

#     for i in range(1, n - 1):
#         if arr[i-1] < arr[i] > arr[i+1]:
#             return "true"    
#     return "false"

# arr = [1, 2, 4, 5, 7, 8, 3]
# value = peakElement(arr)
# print(value)  


# def search(arr, x):
#     for i in range(0, len(arr)):
#         if x == arr[i]:
#             return i
#     return -1

# arr = [1, 2, 3, 4]
# x = 3
# value = search(arr, x)
# print(value)


# def largest(arr):
#     if not arr:
#         return None
#     largest_element = arr[0]

#     for i in range(len(arr)):
#         if arr[i] > largest_element:
#             largest_element = arr[i]
#     return largest_element
        
# arr = [1, 2, 3, 4, 5]
# value = largest(arr)
# print(value)


## Array Subset (CG)
# def subset(a, b):
#     return all(item in b for item in a)

# a = [11, 7, 1, 13, 21, 3, 7, 3]
# b = [11, 3, 7, 1, 7]
# value = subset(a,b)
# print(value)


## Reverse Group Array----------------------------------------------------Try Again---------------------
# def reverse_in_groups(arr, k):
#     n = len(arr)
#     for i in range(0, n, k):
#         left = i
#         right = min(i + k - 1, n - 1)
#         while left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#     return arr

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# result = reverse_in_groups(arr, k)
# print(result)  


# Max and Min
# def max_min(arr):

#     max_value = arr[0]
#     min_value = arr[0]
    
#     for i in range(1, len(arr)):  
#         if arr[i] > max_value:
#             max_value = arr[i]
#         if arr[i] < min_value:
#             min_value = arr[i]
    
#     return max_value, min_value

# arr = [3, 2, 1, 56, 10000, 167]
# max_value, min_value = max_min(arr)
# print(max_value,min_value)


# def rotate(arr):
#     last_element = arr[-1]
#     for i in range(len(arr) - 1, 0, -1):
#         arr[i] = arr[i-1]
#     arr[0] = last_element
#     return arr

# arr = [1, 2, 3, 4, 5]
# rot = rotate(arr)
# print(rot)


## Value equal to index value
# def valueEqualToIndex(arr):
#     result = []
#     for i in range(len(arr)):
#         if arr[i] == i+1:
#             result.append(arr[i])
#     return result

# arr = [15, 2, 45, 4 , 7]
# result = valueEqualToIndex(arr)
# print(result)