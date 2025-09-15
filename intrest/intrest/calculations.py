def simple_interest(principal, rate, time=1):
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time=1, n=1):
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    return amount - principal
