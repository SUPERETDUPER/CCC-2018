# IMPORT THE SCRIPT
import sys, io
import unittest
import abc

sys.path.insert(0, "./CCC/2017/")

import s3_nailed_it


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

        self.assertEqual("\n".join(self.get_expected_output()) + "\n", sys.stdout.getvalue())

        sys.stdout.close()

        sys.stdout = self.stdout_


class NailedItAbstractTest(AbstractTest, abc.ABC):

    def overrideInput(self, input_function):
        s3_nailed_it.input = input_function

    def runMethod(self):
        s3_nailed_it.main()


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


class TestCaseOne(NailedItAbstractTest):

    def get_input_data(self):
        return ["5", "1 10 100 1000 2000"]

    def get_expected_output(self):
        return ["1 10"]


class TestCaseTwo(NailedItAbstractTest):

    def get_input_data(self):
        return [
            "4",
            "1 2 3 4"
        ]

    def get_expected_output(self):
        return ["2 1"]


class InputReader:
    def __init__(self, input_data):
        self.input = input_data
        self.inputRow = 0

    def get_input(self):
        row_ = self.input[self.inputRow]
        self.inputRow += 1
        return row_


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([AbstractTestTester(), TestCaseOne(), TestCaseTwo()])

    runner = unittest.TextTestRunner()
    runner.run(suite)
