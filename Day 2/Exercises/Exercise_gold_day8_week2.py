import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws_count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throws_count += 1
        if dice1 == dice2:
            return throws_count

def main():
    throws_results = []
    total_throws = 0

    for _ in range(100):
        throws_count = throw_until_doubles()
        total_throws += throws_count
        throws_results.append(throws_count)

    total_throws_total = sum(throws_results)
    average_throws = total_throws_total / 100

    print("Total throws:", total_throws_total)
    print("Average throws to reach doubles:", round(average_throws, 2))

main()


