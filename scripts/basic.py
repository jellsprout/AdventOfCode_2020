def find_sum_components(numbers, expected_sum, total_entries=2):
    numbers = sorted(numbers)
    indices = list(range(total_entries))
    trial_numbers = list(numbers[i] for i in indices)
    trial_sum = sum(trial_numbers)
    while trial_sum != expected_sum:
        if trial_sum < expected_sum:
            indices[-1] += 1
        else:
            for j in range(total_entries):
                if indices[-1 - j] - indices[-2 - j] != 1:
                    new_largest_indices = list(range(indices[-2-j]+1, indices[-2-j]+3+j))
                    indices[-2-j:] = new_largest_indices
                    break
        trial_numbers = list(numbers[i] for i in indices)
        trial_sum = sum(trial_numbers)
    return tuple(trial_numbers)


def get_product(list_of_numbers):
    product = 1
    for x in list_of_numbers:
        product *= x
    return product
