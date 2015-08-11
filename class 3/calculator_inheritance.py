"""
You'll need to build a better version of your calculator using OOP and inheritance:
A calculator can be built with different operations. An Operation is an abstract class for which you'll define
subclasses.

Example:

calc1 = Calculator(operations={
    'add': AddOperation,
    'subtract': SubtractOperation})

calc2 = Calculator(operations={
    'add': AddOperation})

The calculator has 1 generic method `calculate` that will receive the arguments
and the operation to perform. For example:

calc1.calculate(2, 1, 5, 'add')  # Should return 2 + 1 + 5 = 8
calc2.calculate(1, 5, 'add')  # Should return 1 + 5 = 6

*IMPORTANT: The number of arguments should be variable*

The Calculator will check if it has that computation present and
invoke the operation. Operations are initialized with the arguments to compute:

op = AddOperation(2, 1, 5)

Once you have an operation object created you should be able to invoke the `operate`
method PRESENT IN EVERY OPERATION.

op.operate()  # Should return 8

*Important notes:*
* The only method that you must implement for every operation (descendant from Operation)  is the `operate` method.
* If the operation is not supported by the calculator (for exampleinvoking `multiply` on calc1)
   the calculator should raise a custom exception (built by you) named `OperationInvalidException`.

This is a unittest class that might be useful for development:


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(operations={
            'add': AddOperation})
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(operations={
            'add': AddOperation})
        with self.assertRaises(OperationInvalidException):
            res = calc.calculate(1, 5, 13, 2, 'INVALID')


class AddOperationTestCase(unittest.TestCase):
    def test_add_operation_with_multiple_arguments(self):
        op = AddOperation(5, 1, 8, 3, 2)
        self.assertEqual(op.operate(), 19)

    def test_add_operation_with_1_arguments(self):
        op = AddOperation(5)
        self.assertEqual(op.operate(), 5)


if __name__ == '__main__':
    unittest.main()

"""

class Operation(object):
    def __init__(self, *args, **kwrgs):  # 1,2,3,4
        self.numbers = args
        
    def operate(self):
        raise NotImplementedError()

class AddOperation(Operation):
    # The only method present in this class
    def operate(self):
        return sum(self.numbers) 


class SubtractOperation(Operation):
    def operate(self):
        return reduce(lambda x,y: x-y, self.numbers)


class Calculator(object):
    def __init__(self, operations):
        self.operations = operations
        #{
        #    'add': AddOperation,
        #    'subtract': SubtractOperation,
        #    'martin': MartinOperation
        #}
        
        # tuple -> *args = ((1,2,3),)
        # args -> *args = (1,2,3)
        # *args always converts every argument to a tuple, even if it is already one
        # if you pass a list, you'd get ([1,2,3],)
        
    def calculate(self, *args):
        
        if len(args) < 3:
            raise ValueError("We need at least 3 arguments")
        elif not isinstance(args[-1], str):
            raise ValueError("Last argument needs to be a string")

        numbers = args[:-1]
        op = args[-1]
        
        if op in self.operations:
            operation_class = self.operations[op]
            op_instance= operation_class(*numbers)
            return op_instance.operate()
        else:
            raise ValueError("Operation not suported: {}".format(op))
        


# testing add
add = AddOperation(2, 1, 5)
assert add.operate() == 8, "AddOperation OK"

# testing subtract
subtract = SubtractOperation(10, 1, 2)
assert subtract.operate() == 7, "SubtractOperation OK"


# testing the calculator
operations = {
    'add': AddOperation,
    'subtract': SubtractOperation,
   # #'martin': MartinOperation
}

calculator = Calculator(operations=operations)
assert calculator.calculate(2, 1, 5, 'add')  == 8, "Calculate operation functions"
assert calculator.calculate(10, 5, 'subtract')  == 5, "Calculate operation functions"
#assert calculator.calculate('add')  # Exception
#assert calculator.calculate()  # Exception
assert calculator.calculate(10, 5, 'foobar')  # Exception



print("Finished")