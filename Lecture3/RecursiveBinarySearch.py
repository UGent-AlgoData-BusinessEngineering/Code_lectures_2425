def recursiveBinarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    return recursiveBinarySearchHelper(lst, key, low, high)

def recursiveBinarySearchHelper(lst, key, low, high):
    if low > high:  # The list has been exhausted without a match
        return -low - 1

    mid = (low + high) // 2
    if key < lst[mid]:
        return recursiveBinarySearchHelper(lst, key, low, mid - 1)
    elif key == lst[mid]:
        return mid
    else:
        return recursiveBinarySearchHelper(lst, key, mid + 1, high)

def main():
    lst = [3, 5, 6, 8, 9, 12, 34, 36]
    print(recursiveBinarySearch(lst, 3))
    print(recursiveBinarySearch(lst, 4))

main()
