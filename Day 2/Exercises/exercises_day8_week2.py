# Ex1
def display_message():
    print("Lucy is learning Data analytics")

display_message()

# Ex2
def favorite_book(title):
    print (f"One of my favorite books is {title}")

title = "Critique of Pure Reason"
favorite_book(title)

# Ex3
def describe_city(city, country="Israel"):
    print(f"{city} is in {country}." )

city = "Yekaterinburg"
describe_city(city, "Ural Republic")

city = "Holon"
describe_city(city)

# Ex 4
import random

def secret_compare(num1, num2):
    if num1 < 1 or num1 > 100:
        print(input("Error, your number isn't accepted"))

    elif num1>num2:
        print(f"Fail: {num1} > {num2}")

    elif num2>num1:
        print(f"Fail: {num2} > {num1}")

    else:
        print(f"Success! Numbers are equal. You've guessed {num1}")

    return(num1, num2)

num1 = int(input("Enter a number between 1 and 100: "))
num2 = random.randint(1, 100)

guessed_num1, secret_num = secret_compare(num1, num2)

# Ex 5

def make_shirt(size= 'large', text= 'I love Python' ):
    print(f"The size of the shirt is {size} and the text is {text}")

size = 'medium'
text = "HEYHEYHEY"
make_shirt(size, text)

make_shirt()

make_shirt(size='medium')

make_shirt(size='small', text='Hello, World!')

make_shirt(text='Hello, Python!', size='extra large')

# Ex 6

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] += " the Great"

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

print("Original list of magicians:")
show_magicians(magician_names)

make_great(magician_names)

# Call the show_magicians() function again to display the modified list
print("\nModified list of magicians:")
show_magicians(magician_names)