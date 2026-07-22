marks = int(input("Enter marks: "))
if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >= 91:
    print("Grade: A+")
elif marks >= 81:
    print("Grade: A")
elif marks >= 71:
    print("Grade: B+")
elif marks >= 61:
    print("Grade: B")
elif marks >= 51:
    print("Grade: C+")
elif marks >= 35:
    print("Grade: C")
else:
    print("Fail")
