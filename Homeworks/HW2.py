from datetime import datetime

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year
age = current_year - birth_year

user_info = [first_name, last_name, age, birth_year]

print("\nUser Information:")
for info in user_info:
    print(info)

if age < 18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")
