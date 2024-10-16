import time

def getTime(n):
    startTime = time.time()
    k = 0
    for i in range(n):
        k = k + 5
    endTime = time.time()
    print("Execution time for n =", n, "is",
        endTime - startTime, "seconds")

def main():
    getTime(10000)
    getTime(100000)
    getTime(1000000)
    getTime(10000000)

main()