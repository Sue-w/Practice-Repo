def sum_func(arg):
    total = 0
    for val in arg:
        total += val
    return total


if __name__ == '__main__':
    print(sum_func(list(range(5))))