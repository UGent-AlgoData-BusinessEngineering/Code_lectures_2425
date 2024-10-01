def main():
    # Open file for output
    outputFile = open("Presidents.txt", "w")

    # Write data to the file
    outputFile.write("George Washington\n")
    outputFile.write("John Adams\n")
    outputFile.write("Thomas Jefferson") #Write Thomas Jefferson

    outputFile.close() # Close the output file

main() # Call the main function
