height = int(input("Enter your height in centimeters: "))
height /= 100

weight = int(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("Healthy")
elif bmi > 25 and bmi < 29.9:
    print("Overweight")
elif bmi > 30:
    print("Fat")
