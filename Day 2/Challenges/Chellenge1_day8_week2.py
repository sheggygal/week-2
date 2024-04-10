def decode_matrix(matrix_str):
    matrix = [list(row) for row in matrix_str.split('\n')]

    columns = [''.join(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0]))]

    for i in range(len(columns)):
        alpha_started = False
        for j in range(len(columns[i])):
            if columns[i][j].isalpha():
                if alpha_started:
                    alpha_started = False
                else:
                    alpha_started = True
            elif alpha_started:
                columns[i] = columns[i][:j] + ' ' + columns[i][j+1:]

    secret_message = ''.join([char for col in columns for char in col if char.isalpha()])

    return secret_message


matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

print("Secret Message:", decode_matrix(matrix_str))