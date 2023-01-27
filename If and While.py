# Name: Tyler Williams
# Filename: If and While.py
# Purpose: Validate a student's enrollment in Honor Roll or Dean's List

last_name = str(input("Enter student's last name: "))

while last_name != 'ZZZ':
    first_name = str(input("Enter student's first name: "))
    gpa = float(input("Enter student GPA: "))

    if gpa > 3.5:
        print(first_name, last_name, "is on the Dean's List")
    elif gpa < 3.5 and gpa > 3.25:
        print(first_name, last_name, "is on the Honor Roll")
    else: 
        print(first_name, last_name, "is not on the Honor Roll or Dean's List")

    last_name = str(input("Enter student's last name: "))
    


    

    
