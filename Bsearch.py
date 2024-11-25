# Binary search algorithm works on principle of divide and conquer
#it has a runtime complexity of O(log n)
# Data should be sorted first
#It looks for a particular key value by comparing the middle most item of the collection.
# If a match occurs, the index of the item is returned
""""
PSEUDOCODE FOR BINARYSEARCH:
   A ← sorted array
   n ← size of array
   x ← value to be searched

   Set lowerBound = 1
   Set upperBound = n

   while x not found
      if upperBound < lowerBound
         EXIT: x does not exist.

      set midPoint = lowerBound + ( upperBound - lowerBound ) / 2

      if A[midPoint] < x
         set lowerBound = midPoint + 1

      if A[midPoint] > x
         set upperBound = midPoint - 1

      if A[midPoint] = x
         EXIT: x found at location midPoint
   end while
end procedure
"""
def binary_Search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        if arr[mid] == key:
            return mid  # Key found at index mid
        elif arr[mid] < key:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Key not found

# Input array
a = [16, 12, 14, 14, 22, 39, 5, 192]
a.sort()  # Sort the array
print("Sorted array:", a)

# Define parameters
n = len(a)
low = 0
high = n - 1


# Search for keys
keys = [14, 54, 192]  # Keys to search
for key in keys:
    result = binary_Search(a, low, high, key)
    if result != -1:
        print(f"Key {key} found at index {result}")
    else:
        print(f"Key {key} not found in the array")
