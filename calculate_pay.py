def calculate_pay(hours, wage):
    """
    Calculate weekly pay including overtime after 40 hours

    :param hours: number greater than 0
    :param wage: number greater than 0
    :precondition: two parameters that both must be greater than 0
    :postcondition: calculate weekly pay including double wage after 40 hours
    :return: weekly pay

    >>> calculate_pay(10, 10)
    100
    >>> calculate_pay(50, 10)
    600.0
    """
    if hours <= 0.0 or wage <= 0.0:
        total_pay = 0.0
    elif hours <= 40.0:
        total_pay = hours * wage
    else:
        overtime = hours - 40.0
        weekly_pay = (hours-overtime) * wage
        overtime_pay = (2 * overtime) * wage
        total_pay = weekly_pay + overtime_pay
    return total_pay


def main():
    """Execute the program."""
    print(calculate_pay(42, 20))


if __name__ == "__main__":
    main()
