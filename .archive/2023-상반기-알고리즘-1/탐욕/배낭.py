def knapsack(cargo):
    capacity = 15
    pack = []

    for price, weight in cargo:
        pack.append((price/weight, price, weight))

    pack.sort(reverse=True)

    total_value: float = 0

    for price, weight in pack:
        if capacity - weight >= 0:
            capacity -= weight
            total_value += price
        else:
            fraction = capacity / weight
            total_value += price * fraction
            break

    return total_value
