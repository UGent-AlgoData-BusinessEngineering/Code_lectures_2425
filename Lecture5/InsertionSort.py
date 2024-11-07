# The function for sorting elements in ascending order
def insertionSort(lst):
    for i in range(1, len(lst)):
        # insert lst[i] into a sorted sublist lst[0..i-1] so that
        #   lst[0..i] is sorted.
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1
  
        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement

def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    insertionSort(list)
    for v in list:
        print(v, end = " ")

main()
