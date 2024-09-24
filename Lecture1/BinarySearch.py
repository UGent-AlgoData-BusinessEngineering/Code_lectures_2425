# Use binary search to find the key in the list
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1 # Last index in lst
      
    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
      
    return -low - 1 # Now high < low, key not found

def main():
    lst = [-3, 1, 2, 4, 9, 23]
    print(binarySearch(lst, 2))
    
main()