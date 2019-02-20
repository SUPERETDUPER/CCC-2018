# IMPORT THE SCRIPT
import sys, io
import unittest
import abc


class AbstractTest(unittest.TestCase, abc.ABC):

    @abc.abstractmethod
    def get_input_data(self):
        pass

    @abc.abstractmethod
    def get_expected_output(self):
        pass

    @abc.abstractmethod
    def overrideInput(self, input_function):
        pass

    @abc.abstractmethod
    def runMethod(self):
        pass

    def runTest(self):
        self.stdout_ = sys.stdout
        sys.stdout = io.StringIO()

        self.overrideInput(InputReader(self.get_input_data()).get_input)

        self.runMethod()

        output = self.get_expected_output()
        real_output = sys.stdout.getvalue()
        if output != -1:
            self.assertEqual("\n".join(output) + "\n", real_output)

        sys.stdout.close()

        sys.stdout = self.stdout_

        if output == -1:
            print(real_output)


class AbstractTestTester(AbstractTest):

    def get_input_data(self):
        return ["Hello1", "Hello2"]

    def get_expected_output(self):
        return ["Output1", "Output2"]

    def overrideInput(self, input_function):
        self.input_function = input_function

    def runMethod(self):
        self.assertEqual(self.input_function(), "Hello1")
        self.assertEqual(self.input_function(), "Hello2")
        print("Output1")
        print("Output2")


class InputReader:
    def __init__(self, input_data):
        self.input = input_data
        self.inputRow = 0

    def get_input(self):
        row_ = self.input[self.inputRow]
        self.inputRow += 1
        return row_
