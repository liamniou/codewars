from collections import defaultdict


def order_weight(string):
    weight_dict = defaultdict(list)
    for number in string.split():
        list_of_number_digits = list(number)
        sum_of_digits = 0
        for value in list_of_number_digits:
            sum_of_digits += int(value)
        weight_dict[sum_of_digits].append(number)
    return ' '.join([' '.join(sorted(value)) for key, value in sorted(weight_dict.items())])


def order_weight_best_practice(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
