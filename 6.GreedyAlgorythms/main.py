def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    num_items = len(item_names)

    # Initialize a table to store the maximum calories and total cost for each subproblem
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]
    total_cost_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    # Fill the table using dynamic programming approach
    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            current_item = items[item_names[i - 1]]

            if current_item["cost"] <= j:
                without_current = dp_table[i - 1][j]
                with_current = (
                    dp_table[i - 1][j - current_item["cost"]] + current_item["calories"]
                )

                if with_current > without_current:
                    dp_table[i][j] = with_current
                    total_cost_table[i][j] = (
                        total_cost_table[i - 1][j - current_item["cost"]]
                        + current_item["cost"]
                    )
                else:
                    dp_table[i][j] = without_current
                    total_cost_table[i][j] = total_cost_table[i - 1][j]
            else:
                dp_table[i][j] = dp_table[i - 1][j]
                total_cost_table[i][j] = total_cost_table[i - 1][j]

    # Reconstruct the selected items
    selected_items = []
    remaining_budget = budget
    for i in range(num_items, 0, -1):
        if dp_table[i][remaining_budget] != dp_table[i - 1][remaining_budget]:
            selected_items.append(item_names[i - 1])
            remaining_budget -= items[item_names[i - 1]]["cost"]

    return (
        selected_items,
        dp_table[num_items][budget],
        total_cost_table[num_items][budget],
    )


# Example usage:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 80

greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

print("Greedy Algorithm:")
print("Selected Items:", greedy_result[0])
print("Total Cost:", greedy_result[1])
print("Total Calories:", greedy_result[2])

print("\nDynamic Programming:")
print("Selected Items:", dynamic_result[0])
print("Total Cost:", dynamic_result[2])
print("Total Calories:", dynamic_result[1])
