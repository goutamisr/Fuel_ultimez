def calculate_pizza_slices(people):
    large_slices = 8
    medium_slices = 6
    regular_slices = 4
    small_slices = 1

    # Calculate the number of each type of pizza needed
    large_pizzas = people // large_slices
    people %= large_slices

    medium_pizzas = people // medium_slices
    people %= medium_slices

    regular_pizzas = people // regular_slices
    people %= regular_slices

    small_pizzas = people // small_slices

    return large_pizzas, medium_pizzas, regular_pizzas, small_pizzas


# Test cases
print(calculate_pizza_slices(10))  # Output: (12, 0, 1, 0)
print(calculate_pizza_slices(19))  # Output: (2, 0, 0, 3)
print(calculate_pizza_slices(70))