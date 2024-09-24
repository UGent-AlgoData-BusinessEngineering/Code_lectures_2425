# The function for sorting elements in ascending order (Simplified Version)
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin = min(lst[i : ])
        currentMinIndex = i + lst[i: ].index(currentMin)
        
        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin
            
def main():
    lst = [-2, 4.5, 5, 1, 2, -3.3]
    selectionSort(lst)
    print(lst)

main()