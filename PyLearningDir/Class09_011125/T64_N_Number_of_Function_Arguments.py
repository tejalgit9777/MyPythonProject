# N Number of function arguments

def n_number_args(*args):
    print(args)

n_number_args(1, 2, 3,"test",3.40,'Shine',True)


def min_max_number_find(*numbers):
    print("Minimum Number is: ",min(numbers))
    print("Minimum Number is: ",max(numbers))

min_max_number_find(34,567,11,3,22)
