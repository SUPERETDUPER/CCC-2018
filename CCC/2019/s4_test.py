import script_tester
import s4


class S4AbstractTest(script_tester.AbstractTest):
    def overrideInput(self, input_function):
        s4.input = input_function

    def runMethod(self):
        s4.main()


class Test1(S4AbstractTest):
    def get_input_data(self):
        return [
            "10 2",
            "1 2 3 4 5 6 7 8 9 10"
        ]

    def get_expected_output(self):
        return ["30"]


class Test2(S4AbstractTest):
    def get_input_data(self):
        return [
            "10 6",
            "1 2 3 4 5 6 7 8 9 10"
        ]

    def get_expected_output(self):
        return ["16"]


class Test3(S4AbstractTest):
    def get_input_data(self):
        return [
            "10 9",
            "1 2 3 4 5 6 7 8 9 10"
        ]

    def get_expected_output(self):
        return ["19"]
