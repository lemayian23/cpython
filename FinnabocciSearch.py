#Fibonacci Series is  a series of numbers that have two primitive numbers
#The successive numbers are the sum of preceding two numbers in series
#This is infinite constants series, therefore , the numbers in it are fixed.
#The main idea behind the Fibonacci series is also to eliminate the least possible places
#where the element could be found. In a way, it acts like a divide and conquer algorithm(logic behind binary search)
#The first few numbers include: 0,1,1,2,3,,5,8,13,21,34,55,89,144,233,377,610,987,1597,2484,4081,6565.

def fibonacci_search(arr,n,key):
    offset = -1
    Fm2 = 0
    Fm1 = 1
    Fm = Fm1 + Fm2
    while Fm < n:
        Fm2 = Fm1
        Fm1 = Fm
        Fm = Fm1 + Fm2
    while Fm > 1:
        i = min(offset+Fm2,n-1)
        if arr[i] < key:
            Fm = Fm1
            Fm1 = Fm2
            Fm2 = Fm1 - Fm2
            offset = i
        elif arr[i] > key:
            Fm = Fm2
            Fm1 = Fm1 - Fm2
            Fm2 = Fm - Fm1
        else:
            return i
    if (Fm1 ==1 and arr[offset + 1] == key):
        return offset + 1
    return -1
arr = [12, 14, 16, 17, 20, 24, 31, 43, 50, 62]
print("Array elements are: ")
for i in range(len(arr)):
    print(arr[i],end = " ")
n = len(arr)
key = 20
print("\n The element to be searched: ",key)
index = fibonacci_search(arr, n , key)
if (index >= 0):
    print("The elements is found at index : ", (index ))
else:
    print("\nUnsuccessful Search")