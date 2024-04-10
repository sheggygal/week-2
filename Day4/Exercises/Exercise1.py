import random

def get_random_temp(season):
    if season.lower() == 'winter':
        return round(random.uniform(-10, 16), 1)
    elif season.lower() == 'spring':
        return round(random.uniform(0, 23), 1)
    elif season.lower() == 'summer':
        return round(random.uniform(16, 32), 1)
    elif season.lower() == 'autumn' or season.lower() == 'fall':
        return round(random.uniform(0, 16), 1)
    else:
        return "Invalid season"

def main():
    month = int(input("Enter the number of the month (1-12): "))
    if month in [12, 1, 2]:
        season = 'winter'
    elif month in [3, 4, 5]:
        season = 'spring'
    elif month in [6, 7, 8]:
        season = 'summer'
    elif month in [9, 10, 11]:
        season = 'autumn'
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
        return

    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 24:
        print("It's a comfortable temperature.")
    elif 24 <= temperature < 32:
        print("Getting warm! Stay hydrated.")
    elif 32 <= temperature <= 40:
        print("Hot day ahead! Drink plenty of water.")
    else:
        print("Temperature out of range.")


if __name__ == "__main__":
    main()