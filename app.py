# Body Mass Index Calculator
# To calculate body mass index we require user height and weight

height = float(input("Height :"))
weight = float(input("Weight :"))

# formula :-
BMI = weight/ height **2

# logic :-
if  BMI < 18.5:
    health= "underweight"
elif BMI < 24.9:
    health= "Normal"
elif BMI < 29.0:
    health= "Over Weight"
elif BMI < 34.0:
    health= "Obese"
else:
    health= "Extreme Obese"

# output :-
print(f"your bmi is {BMI :.2f}\nyou are {health}")