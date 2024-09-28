def convert_length(value, from_unit, to_unit):
    # Define conversion factors
    conversion_factors = {
        'meters': 1,
        'feet': 3.28084,
        'inches': 39.3701
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'kilograms': 1,
        'pounds': 2.20462
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid temperature conversion.")

def main():
    print("Unit Converter")
    print("1. Length (meters, feet, inches)")
    print("2. Weight (kilograms, pounds)")
    print("3. Temperature (Celsius, Fahrenheit)")

    choice = input("Choose a conversion type (1/2/3): ")

    if choice == '1':
        value = float(input("Enter value: "))
        from_unit = input("From unit (meters/feet/inches): ").lower()
        to_unit = input("To unit (meters/feet/inches): ").lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == '2':
        value = float(input("Enter value: "))
        from_unit = input("From unit (kilograms/pounds): ").lower()
        to_unit = input("To unit (kilograms/pounds): ").lower()
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

    elif choice == '3':
        value = float(input("Enter value: "))
        from_unit = input("From unit (Celsius/Fahrenheit): ").capitalize()
        to_unit = input("To unit (Celsius/Fahrenheit): ").capitalize()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

