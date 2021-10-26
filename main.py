from temperature import temperatureConversion


print("In the next message, enter what you wish to convert.")
temp = input("Send the temperature value. Send the unit WITH A SPACE. \nExample: 25 C \n: ")
temp = temp.split()
temperatureConversion(temp[0], temp[1])

if __name__  != "__main__":
    print(("run this file dont import"))