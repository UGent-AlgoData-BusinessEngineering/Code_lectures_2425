from random import randint 

def main():
    # Open file for writing data
    outputFile = open("Numbers.txt", "w")
    for i in range(10):
        outputFile.write(str(randint(0, 9)) + " ")
    outputFile.close() # Close the file

    # Open file for reading data
    inputFile = open("Numbers.txt", "r")
    s = inputFile.read() # Read all data to s
    numbers = [float(x) for x in s.split()]
    for number in numbers:
        print(number, end = " ")
    inputFile.close() # Close the file
    
main() # Call the main function
