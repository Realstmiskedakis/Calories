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
def calories():
    try:

        # It's a function that calculates the daily calories of a person.
        print(">> Find out how many calories you should eat per day")
        print(">> Age: 15-18 / 18-30 / 30-60 / 60<\n")

        sex = input(">> Enter your Gender ( Sex ), Answer w/ Male or Female: ").lower()
        
        if sex not in ('male', 'female'):
            print("Invalid Input, Rerun the program.")
            quit()
            
        elif sex == 'male' or 'female':
            age = int(input(">> Tell me your age: "))
            weight = int(input(">> Tell me your weight (Kg - Kilograms): "))
            height = float(input(">> Tell me your height (cm - Centimeters): "))
            if sex == 'male':
                male_cal = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
                print(">> Your Daily Calories is: ", male_cal)

            elif sex == 'female':
                female_cal = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
                print(">> Your Daily Calories is: ", female_cal)

    except (TypeError, ValueError, IndexError):
        print("Invalid Input, Rerun the program.")
        quit()


calories()
