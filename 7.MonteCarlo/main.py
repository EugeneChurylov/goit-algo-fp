import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    outcomes = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        outcomes[total] += 1

    probabilities = {key: value / num_rolls * 100 for key, value in outcomes.items()}
    return probabilities


def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for i in range(2, 13):
        print(f"{i}\t{probabilities[i]:.2f}% ({probabilities[i]/100:.2f})")


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.bar(sums, probabilities_values, color="blue", alpha=0.7)
    plt.xlabel("Сума")
    plt.ylabel("Імовірність (%)")
    plt.title("Ймовірності сум при киданні двох кубиків")
    plt.show()


if __name__ == "__main__":
    num_rolls = 1000000  # Задайте бажану кількість кидків

    probabilities = simulate_dice_rolls(num_rolls)

    print_probabilities(probabilities)
    plot_probabilities(probabilities)
