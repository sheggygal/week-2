def compute_division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print(compute_division(5,0))