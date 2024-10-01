def main():
    # Open file for appending data
    outputFile = open("Info.txt", "a")
    outputFile.write("\nPython is interpreted\n")
    outputFile.close() # Close the input file

main() # Call the main function
