import random
import matplotlib.pyplot as plt

num_throws = 1000000

sum_counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

for _ in range(num_throws):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    sum_counts[dice_sum] += 1

probabilities = {sum_val: count / num_throws for sum_val, count in sum_counts.items()}

analytical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def main():
    sums = list(sum_counts.keys())
    simulated_probs = [probabilities[sum_val] for sum_val in sums]
    analytical_probs = [analytical_probabilities[sum_val] for sum_val in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(
        sums, simulated_probs, width=0.4, label="Monte Carlo Simulation", align="center"
    )
    plt.plot(
        sums,
        analytical_probs,
        color="red",
        marker="o",
        linestyle="-",
        label="Analytical Probability",
    )
    plt.xlabel("Sum of Dice")
    plt.ylabel("Probability")
    plt.title("Probability of Dice Sums: Simulation vs Analytical")
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()

    probabilities, analytical_probabilities


if __name__ == "__main__":
    main()
