def celsius_fahrenheit(celsius):
    cel_fah = (1.8) * celsius + 32
    return cel_fah


def celsius_kelvin(celsius):
    cel_kel = celsius + 273.15
    return cel_kel


def fahrenheit_celsius(fahrenheit):
    fah_cel = (fahrenheit-32) * 1.8
    return fah_cel


def fahrenheit_kelvin(fahrenheit):
    fah_kel = (fahrenheit-32)*1.8+273.15
    return fah_kel


def kelvin_celsius(kelvin):
    kel_cel = kelvin-273.15
    return kel_cel


def kelvin_fahrenheit(kelvin):
    kel_fah = (kelvin-273.15)*1.8+273.15
    return kel_fah


def temp_convert(value, temp_unit):
    if temp_unit == 'C':
        f = celsius_fahrenheit(value)
        k = celsius_kelvin(value)
        print(f"{value}°C is converted to {f:.2f}°F and {k:.2f}°K")
    elif temp_unit == 'F':
        c = fahrenheit_celsius(value)
        k = fahrenheit_kelvin(value)
        print(f"{value}°F is converted to {c:.2f}°C and {k:.2f}°K")
    elif temp_unit == 'K':
        c = kelvin_celsius(value)
        f = kelvin_fahrenheit(value)
        print(f"{value}°K is converted to {c:.2f}°C and {f:.2f}°F")
    else:
        print("Invalid unit of measurement")

if __name__ == "__main__":
    value = float(input("Enter the temperature value:"))
    temp_unit = input("Enter the unit(C,F,K):").upper()
    temp_convert(value, temp_unit)
