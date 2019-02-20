import script_tester, unittest
import abc, sys, io
import s3
from random import randint


class S1AbstractTest(script_tester.AbstractTest, abc.ABC):

    def overrideInput(self, input_function):
        s3.input = input_function

    def runMethod(self):
        s3.main()


class TestCaseOne(S1AbstractTest):

    def get_input_data(self):
        return ["5 1 X", "5 1 X", "5 1 X"]

    def get_expected_output(self):
        return -1


class TestCaseTwo(S1AbstractTest):
    def get_input_data(self):
        return [
            "5 5 5",
            "1 1 1",
            "X X X"
        ]

    def get_expected_output(self):
        return -1


class TestCaseThree(S1AbstractTest):
    def get_input_data(self):
        return [
            "14 X 18",
            "X 12 X",
            "X X 2"
        ]

    def get_expected_output(self):
        return -1


class TestCaseFour(S1AbstractTest):
    def get_input_data(self):
        return [
            "14 X X",
            "X X 18",
            "X 16 X"
        ]

    def get_expected_output(self):
        return -1


class TestCaseFive(S1AbstractTest):
    def get_input_data(self):
        return [
            "X X X",
            "X X X",
            "X X X"
        ]

    def get_expected_output(self):
        return -1


class TestCaseFive(S1AbstractTest):
    def get_input_data(self):
        return [
            "16 X X",
            "X X X",
            "X -3 X"
        ]

    def get_expected_output(self):
        return -1


class TestCaseSix(S1AbstractTest):
    def get_input_data(self):
        return [
            "0 5 10",
            "10 X X",
            "20 -3 X"
        ]

    def get_expected_output(self):
        return -1


class TestCaseSeven(S1AbstractTest):
    def get_input_data(self):
        return [
            "16 X X",
            "X X X",
            "X -2 X"
        ]

    def get_expected_output(self):
        return -1

class TestCaseEight(S1AbstractTest):
    def get_input_data(self):
        return [
            "X X X",
            "X X 3",
            "X 6 X"
        ]

    def get_expected_output(self):
        return -1

class TestCaseNine(S1AbstractTest):
    def get_input_data(self):
        return [
            "X X -3",
            "X X X",
            "X X -1"
        ]

    def get_expected_output(self):
        return -1


def multipleTest():
    while True:
        inputData = [
            "X X X",
            "X X X",
            "X X X"
        ]

        for i in range(2):
            random1 = randint(0, 2)
            random2 = randint(0, 2)
            random3 = str(randint(-10, 10))
            if random1 == 0:
                newRow = random3 + " X X"
            elif random1 == 1:
                newRow = "X " + random3 + " X"
            else:
                newRow = "X X " + random3

            inputData[random2] = newRow

        print(inputData)

        s3.input = script_tester.InputReader(inputData).get_input

        stdout_ = sys.stdout
        sys.stdout = io.StringIO()

        s3.main()

        result = sys.stdout.getvalue().rstrip()

        sys.stdout.close()

        sys.stdout = stdout_

        if not resultIsValid(result):
            print("BAD")
            print(result.split("\n"))
            break
        else:
            print("GOOD")
            print(result.split("\n"))
            print()


def resultIsValid(result):
    grid = []
    rows = result.split("\n")
    for row in rows:
        grid.append(list(map(int, row.strip().split(" "))))

    for row in grid:
        if row[1] - row[0] != row[2] - row[1]:
            return False

    for columnIndex in range(3):
        if grid[1][columnIndex] - grid[0][columnIndex] != grid[2][columnIndex] - grid[1][columnIndex]:
            return False

    return True


if __name__ == '__main__':
    multipleTest()
    # suite = unittest.TestSuite()
    # suite.addTests([TestCaseOne(), TestCaseTwo(), TestCaseThree(), TestCaseFour])
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
