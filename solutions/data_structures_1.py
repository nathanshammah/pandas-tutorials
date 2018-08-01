fibonacci_numbers = [1, 1]
[fibonacci_numbers.append(sum(fibonacci_numbers[-2:])) for i in range(8)]
fibonacci_numbers = pandas.Series(fibonacci_numbers)

(fibonacci_numbers ** 2)[-4:].sum()
