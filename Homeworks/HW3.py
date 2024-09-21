def login():
    attempts = 3
    correct_name = "John"
    correct_surname = "Doe"
    
    while attempts > 0:
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        
        if name == correct_name and surname == correct_surname:
            print(f"Welcome, {name} {surname}!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect name or surname. You have {attempts} attempts left.")
    
    print("Please try again later.")
    return False

def choose_courses():
    courses = []
    for i in range(5):
        course = input(f"Enter course {i+1}: ")
        courses.append(course)
    
    print("\nAvailable courses: ", courses)
    chosen_courses = []
    
    while True:
        chosen_courses = input("\nEnter the courses you want to take (separate by commas): ").split(',')
        chosen_courses = [course.strip() for course in chosen_courses]  
        
        if len(chosen_courses) < 3:
            print("You failed in class. Minimum 3 courses required.")
            return False
        elif len(chosen_courses) > 5:
            print("Maximum 5 courses allowed.")
        else:
            print("Courses selected: ", chosen_courses)
            return chosen_courses

def calculate_grade():
    midterm = int(input("Enter midterm grade: "))
    final = int(input("Enter final grade: "))
    project = int(input("Enter project grade: "))
    
    grades = {"midterm": midterm, "final": final, "project": project}
    
    final_grade = (midterm * 0.30) + (final * 0.50) + (project * 0.20)
    print(f"\nFinal grade: {final_grade:.2f}")
    
    if final_grade >= 90:
        print("You received an AA.")
    elif 70 <= final_grade < 90:
        print("You received a BB.")
    elif 50 <= final_grade < 70:
        print("You received a CC.")
    elif 30 <= final_grade < 50:
        print("You received a DD.")
    else:
        print("You received an FF. You failed the course.")
    
    return final_grade

if login():
    chosen_courses = choose_courses()
    if chosen_courses:
        print("\nChoose one course to take an exam from.")
        chosen_course = input("Enter the course name: ")
        
        if chosen_course in chosen_courses:
            print(f"\nYou chose {chosen_course}.")
            final_grade = calculate_grade()
        else:
            print("Invalid course selection.")
