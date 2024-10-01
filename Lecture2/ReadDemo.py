def main():
    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("(1) Using read(): ")
    print(inputFile.read()) # Read all in the file
    inputFile.close() # Close the input file

    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("\n(2) Using read(number): ")
    s1 = inputFile.read(5)
    print(s1)
    s2 = inputFile.read(15) # Read 15 characters to s2
    print(repr(s2))
    inputFile.close() # Close the input file

    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("\n(3) Using readline(): ")
    line1 = inputFile.readline() # Read a line
    line2 = inputFile.readline()
    line3 = inputFile.readline()
    line4 = inputFile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    inputFile.close() # Close the input file

    # Open file for input
    inputFile = open("Presidents.txt", "r")
    print("\n(4) Using readlines(): ")
    print(inputFile.readlines())
    inputFile.close() # Close the input file

main() # Call the main function
