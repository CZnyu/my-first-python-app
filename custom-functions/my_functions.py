# custom-functions/my_functions.py

# TODO: define temperature conversion function here
def celsius_to_fahrenheit(celsius_temp):
    return(celsius_temp*9/5) + 32

# TODO: define gradebook function here
def numeric_to_letter_grade (a):
    if a >= 94:
        return "A"
    elif a >= 89:
        return "A-"
    elif a >= 84:
        return "B+"
    elif a >= 79:
        return "B"
    else:
        return "C"


if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    #print("--------------------")
    #c = float(input("Enter Temperature:"))
    #print("THE CELSIUS TEMP IS:", c, "DEGREES")
    #f = celsius_to_fahrenheit(c)
    #print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

   # print("--------------------")
    #score = 87.5
    #print("THE NUMERIC SCORE IS:", score)
    #grade = numeric_to_letter_grade(score)
    #print("THE LETTER-GRADE EQUIVALENT IS:", grade)


    print("--------------------")
    score = float(input("Enter Numeric Grade (from 0 to 100):"))
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)