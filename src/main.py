'''
This script will allow users to run a simple
calculator app with supplied arguments on the 
command line.
'''

__author__ = "Drowsy Dev + Scooterking38"
__version__ = 2.0

from argparse import ArgumentParser

def operate(num1: float, operator: str, num2: float) -> float:
    eval(f'result = {num1}{operator}{num2}')
    return result

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
