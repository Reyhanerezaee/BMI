height = int(input("Enter your height in centimeters: "))
height /= 100

weight = int(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

print(bmi)
