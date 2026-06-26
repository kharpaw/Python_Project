score = int(input("Enter the grades of students: "))

if score >= 101:
    print("Please enter the grade again")
    exit()

if score >= 90:
    grade = "A"
    
elif score >= 80:
    grade = "B"
    
elif score >= 70:
    grade = "c"
    
elif score >= 60:
    grade = "D"
    
else:
    grade = "Failed"
    

print("Grade: ", grade)    