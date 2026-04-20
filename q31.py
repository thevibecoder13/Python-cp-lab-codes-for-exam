def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit:", fahrenheit)