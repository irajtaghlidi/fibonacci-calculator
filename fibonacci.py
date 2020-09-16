def fibonacci_element(n, computed = {0: 0, 1: 1}):
    """ calculate N'th Fibonacci number. """
    if n not in computed:
        computed[n] = fibonacci_element(n-1, computed) + fibonacci_element(n-2, computed)
    return computed[n]



def sequence_calc(nterms = 1):
    """ Calculate Fibonacci sequence from start """
    sequence = []
    for i in range(nterms):
        next_fibonacci_value = fibonacci_element(i)
        sequence.append(next_fibonacci_value)
    return sequence



def check_number(input_int):
    """
    Identify whether a number is part of the fibonacci sequence or not.
    we calculate fibinacci from 0 to equil or first number bigger than input number.
    If we pass the input number, then we just return False.
    """
    sequence_index = 1
    fibonacci_number = 0
    while fibonacci_number <= input_int:
        if fibonacci_number == input_int:
            return [True, sequence_index]

        sequence_index += 1
        fibonacci_number = fibonacci_element(sequence_index)

    return [False, False]
        