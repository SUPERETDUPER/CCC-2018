from script_tester import AbstractTest
import abc

import s3_nailed_it

class NailedItAbstractTest(AbstractTest, abc.ABC):

    def overrideInput(self, input_function):
        s3_nailed_it.input = input_function

    def runMethod(self):
        s3_nailed_it.start_solving()


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

class TestCaseTwo(NailedItAbstractTest):

    def get_input_data(self):
        return [
            "4",
            "1 2 3 4"
        ]

    def get_expected_output(self):
        return ["2 1"]
