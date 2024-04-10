import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def count_pairs_with_sum(numbers, target):
    count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1

    return count


pairs_count = count_pairs_with_sum(list_of_numbers, target_number)

print("Number of pairs summing to target number:", pairs_count)