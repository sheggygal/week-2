import datetime

def get_age(year, month, day):
    current_date = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return age

def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)

    if gender.lower() == 'm':
        retirement_age = 67
    elif gender.lower() == 'f':
        if year > 1947 or (year == 1947 and month >= 4):
            retirement_age = 62
        else:
            retirement_age = 63  # Retirement age for women born before April 1947
    else:
        return "Invalid gender"

    return age >= retirement_age

def main():
    gender = input("Enter your gender (m/f): ")
    date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")

    if can_retire(gender, date_of_birth):
        print("Congratulations! You can retire.")
    else:
        print("Sorry, you can't retire yet.")

if __name__ == "__main__":
    main()