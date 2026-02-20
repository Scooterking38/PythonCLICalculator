'''
This script will allow users to run a simple
calculator app with supplied arguments on the 
command line.
'''

__author__ = "Drowsy Dev"
__version__ = 1.0

from argparse import ArgumentParser

def operate(num1: float, operator: str, num2: float) -> float:
    '''Adds two floats together and return the sum.

       :param num1: float, The first number to add
       :param num2: float, The second number to add

       :return sum: float, The sum of the supplied arguments

       Example Usage:
       ```
        sum = add(1.0, 2.0)
        print(sum) # 3.0
       ```
    '''
    eval(f'result = {num1}{operator}{num2}')
    return result

def subtract(num1: float, num2: float) -> float:
    '''Subtract two floats and return the difference.

       :param num1: float, The number to subtract from
       :param num2: float, The number to subtract

       :return difference: float, The difference of the supplied arguments

       Example Usage:
       ```
        difference = subtract(5.0, 3.0)
        print(difference) # 2.0
       ```
    '''
    difference = num1 - num2
    return difference

def multiply(num1: float, num2: float) -> float:
    '''Multiplies two floats together and return the product.

       :param num1: float, The first number to multiply
       :param num2: float, The second number to multiply

       :return product: float, The product of the supplied arguments

       Example Usage:
       ```
        product = multiply(3.0, 2.0)
        print(product) # 6.0
       ```
    '''
    product = num1 * num2
    return product

def divide(num1: float, num2: float) -> (float | str):
    '''Divides two floats and return the quotient.

       :param num1: float, The number to divide from
       :param num2: float, The number to divide by

       :return quotient: float, The quotient of the supplied arguments

       Example Usage:
       ```
        quotient = divide(6.0, 2.0)
        print(quotient) # 3.0
       ```
    '''
    if num2 == 0:
        print("Error: Divide by zero error")
        return "inf"
    quotient = num1 / num2
    return quotient

parser = ArgumentParser()
parser.add_argument("operation", type=str, 
                    choices=["add", "subtract", "multiply", "divide"], 
                    help="The operation to run on the given arguments.")
parser.add_argument("num_one", type=float, help="The first number.")
parser.add_argument("num_two", type=float, help="The second number.")

args = parser.parse_args()
operation = args.operation
num_one = args.num_one
num_two = args.num_two

result = None
ops = ['+','-','*','/']
choicelist = ['add','subtract','multiply','divide']
result = operate(num_one,ops[choicelist.index(operation)],num_two)


print(f"Result: {result}")
