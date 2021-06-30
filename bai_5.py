def convert_temperature(temperature, temperature_unit):
    if temperature_unit == "C":
        print("\nConvert to F...")
        value = (temperature * 1.8) + 32
    if temperature_unit == "F":
        print("\nConvert to C...")
        value = (temperature - 32) / 1.8

    return value


def print_output(old_temperature, new_temperature, temperature_unit):
    if temperature_unit == "C":
        print(old_temperature, "C =", new_temperature, "F")
    if temperature_unit == "F":
        print(old_temperature, "F =", new_temperature, "C")


def main():
    temperature = float(input("Enter temperature: "))
    temperature_unit = input("Enter C or F: ")

    output = convert_temperature(temperature, temperature_unit.upper())

    print_output(temperature, output, temperature_unit.upper())


main()
