try:
    number = int(input("Enter a number: "))
    print ("The number enteren is", number)

except ValueError as ex:
    print("Exception: ", ex)