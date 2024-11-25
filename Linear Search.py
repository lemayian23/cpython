def linear_search(a, n, key):
    count = 0
    for i in range( n):
        if a[i] == key:
            print("The element found at position ", (i +1))
            count += 1
    if count == 0:
        print("The element not present in the array")

a = [11,14,56,72,32,84.10]
n = len(a)
key = 32
linear_search(a, n, key)
key = 3
linear_search(a, n, key)