def calculate_expression(x):
    x_str = str(x)

    term1 = int(x_str)
    term2 = int(x_str * 2)
    term3 = int(x_str * 3)
    term4 = int(x_str * 4)

    result = term1 + term2 + term3 + term4

    return result

print(calculate_expression(3))