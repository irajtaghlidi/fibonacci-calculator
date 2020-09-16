import fibonacci
import argparse



def main():
    # define arguments
    parser = argparse.ArgumentParser(description='Fibinacci calculator.', prog='docker run --rm [IMAGE NAME]')
    parser.add_argument('--calc', type=int, default=10, help='how many fibonacci numbers should be printed out in the sequence')
    parser.add_argument('--check', type=int, help='identify whether a number is part of the fibonacci sequence or not')
    parser.add_argument('--verbose', '-v', action='count')
    args = parser.parse_args()

    verbose_level = 0
    if args.verbose is not None:
        verbose_level = args.verbose

    
    if args.check is not None:
        user_input = args.check
        fibonacci_result = fibonacci.check_number(user_input)
        print_fibonacci_result(fibonacci_result, verbose_level)
    
    elif args.calc is not None:
        user_input = int(args.calc)
        # calculate Fibonacci sequense
        sequence = fibonacci.sequence_calc(user_input)
        # reverese sequence and print it
        sequence.reverse()
        print_out(sequence, verbose_level)




def print_out(data_array, verbose_level = 0, glue = "\n"):
    """ Print List with variable message and Glue/seprator. """
    if verbose_level > 0:
        index = len(data_array)
        for number in data_array:
            print("#{0}: {1}".format(index, number))
            index -= 1
    else:
        output = glue.join(map(str, data_array))
        print(output)



def print_fibonacci_result(result, verbose_level):
    if result[0] == True:
        if verbose_level > 0:
            print("True: This number is #{0} in Fibonacci sequent".format(result[1]))
        else:
            # print("1:{0}".format(result[1]))
            print("1")
    else:
        if verbose_level > 0:
            print("False: Unfortunately this number is NOT in Fibonacci sequent")
        else:
            print("0")



if __name__ == "__main__":
    main()
