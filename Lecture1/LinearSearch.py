# The function for finding a key in the list 
def linearSearch(lst, key):
    for i in range(len(lst)): 
        if key == lst[i]:
            return i
  
    return -1

def main():
    lst = [4, 5, 1, 2, 9, -3]
    print(linearSearch(lst, 2))
    
main()