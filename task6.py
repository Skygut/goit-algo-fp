def greedy_algorithm(items, budget):
    items_calorie_ratio = {
        item: items[item]["calories"] / items[item]["cost"] for item in items
    }
    sorted_items = sorted(
        items_calorie_ratio.keys(), key=lambda x: items_calorie_ratio[x], reverse=True
    )

    selected_items = {}
    total_cost = 0
    total_calories = 0

    for item in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items[item] = items[item]
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost = items[item_names[i - 1]]["cost"]
            calories = items[item_names[i - 1]]["calories"]

            if cost <= w:
                dp[i][w] = max(calories + dp[i - 1][w - cost], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = {}
    total_calories = dp[n][budget]
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = item_names[i - 1]
            selected_items[item] = items[item]
            w -= items[item]["cost"]

    return selected_items, total_calories


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    budget = 100

    greedy_solution = greedy_algorithm(items, budget)
    dynamic_solution = dynamic_programming(items, budget)

    print("Greedy Algorithm Solution:", greedy_solution)
    print("Dynamic Programming Solution:", dynamic_solution)


if __name__ == "__main__":
    main()
