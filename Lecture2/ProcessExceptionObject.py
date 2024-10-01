try:
    number = float(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as ex:
    print("Exception:", ex)


