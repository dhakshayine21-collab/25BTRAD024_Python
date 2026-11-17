# Mini Project: Unit Converter

print("===== Unit Converter =====")
print("1. Centimeters to Meters")
print("2. Kilograms to Grams")
print("3. Celsius to Fahrenheit")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    cm = float(input("Enter length in centimeters: "))
    m = cm / 100
    print("Length in meters =", m)

elif choice == 2:
    kg = float(input("Enter weight in kilograms: "))
    g = kg * 1000
    print("Weight in grams =", g)

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit =", f)

else:
    print("Invalid choice!")