"""
@Author: STelios Miskedakis - @Realstmiskedakis / @AcidSHellGR
Language: Python 3.10.5
Version: "1.0V"
About this Program:
    Ideal weight means euphoria and above all health!
    The best way to achieve the ideal weight is daily exercise, and a complete and proper diet.
    Extreme diets that promise the loss of many kilos in a short period of time are of no use, because after the end of the diet,
    the kilos we lost are almost certain to be gained back, and even more so.
    Achieving the ideal weight is a goal that we must approach slowly, making exercise and proper nutrition a way of life, as much as possible.
    It's never too late to take care of your health!

    *find out how many calories you should eat per day*
"""

# The Calories Function
def get_calories(sex, age, weight, height):
    if sex == 'male':
        return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    elif sex == 'female':
        return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

sex = input("Enter ( Male / Female ): ").lower()
while sex not in ['male', 'female']:
    sex = input("Enter ( Male / Female ): ").lower()

age = int(input(">> Tell me your age: "))
weight = int(input(">> Tell me your weight (Kg - Kilograms): "))
height = float(input(">> Tell me your height (cm - Centimeters): "))
calories = get_calories(sex, age, weight, height)

print(f">>{sex}: {calories} calories")
