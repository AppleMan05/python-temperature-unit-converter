def temperatureConversion(input, unit):
    input = int(input)
    print(input)
    
    if unit == "C":
        kelvin = input + 273
        fahrenheit = (input*9/5)+32
        celcius = input
    elif unit == "K":
        kelvin = input
        celcius = input - 273
        fahrenheit = (input-273) * 9/5 + 32
    elif unit == "F":
        celcius = (input - 32)*5/9
        fahrenheit = input
        kelvin = celcius + 273
    print(f'Celcius = {celcius} \n Fahrenheit = {fahrenheit} \n Kelvin = {kelvin}')


if __name__ == "__main__":
    print("this isnt meant to be run.")