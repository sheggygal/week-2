def box_printer(*strings):
    max_length = max(len(s) for s in strings)
    width = max_length + 4

    print('*' * width)


    for s in strings:
        print('* {:<{}} *'.format(s, max_length))

    print('*' * width)

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Ex 2
#This code implements the Insertion Sort algorithm.
# The purpose of the code is to sort a list of numbers (alist) in ascending order using the Insertion Sort algorithm.
# How it works:

# 1. The function insertion_sort takes a list alist as input.
# 2. The function iterates over each element in the list starting from the second element (index 1) to the end of the list.
# 3. For each element, it saves the current value (currentvalue) and its index (position).
# 4. It then enters a while loop that continues as long as position is greater than 0 and the element to the left of the current position is greater than currentvalue.
# 5. Inside the while loop, it shifts elements to the right to make space for the currentvalue.
# 6. Once the correct position for currentvalue is found (where all elements to its left are less than or equal to it), it assigns currentvalue to the list at that position.
# 7. After iterating through all elements, the list alist will be sorted in ascending order.
# 8. The sorted list is then printed.

