def temperature():
  print("Convert Fahrenheit to Celsius.")
  Fahrenheit_degree = float(input("Enter the temperature in Fahrenheit. "))
  Celsius_degree = (Fahrenheit_degree - 32) * 5.0/9.0
  print(f'The temperature in Celsius is {Celsius_degree}')

if __name__ == "__main__":
  temperature()