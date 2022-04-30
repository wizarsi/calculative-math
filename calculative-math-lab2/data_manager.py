import math
import sys
from calculating import solve_simple_iteration_method, solve_newton_method, solve_system_iteration_method, show_graph

INPUT_STREAM = sys.stdin
OUTPUT_STREAM = sys.stdout


class DataManager:
    equations = {1: "-1,38x^3-5,42x^2+2,57x+10,95", 2: "e^(3x)-2x", 3: "(3x^4)/5+3"}
    system_equations = {1: "x^2 - 5y + 10", 2: "3x^3 - 2y", 3: "(3x^2)/5 + 3y + 2"}
    equation_number = 0
    equation_number1 = 0
    equation_number2 = 0
    reading_type = 0
    calculating_type = 0
    approximation1 = 0
    approximation2 = 0
    a = 0
    b = 0
    accuracy = 0.0

    def __init__(self):
        self.choose_calculating_method()
        self.choose_reading_type()
        self.choose_equation()
        self.solve_equation()
        # вывести ответ в файл или в консоль

    def solve_equation(self):
        match self.calculating_type:
            case 1:
                solve_newton_method(self.get_equation(self.equation_number), self.a, self.b, self.accuracy)
            case 2:
                solve_simple_iteration_method(self.get_equation(self.equation_number), self.a, self.b, self.accuracy)
            case 3:
                solve_system_iteration_method(self.get_system_equation(self.equation_number1),
                                              self.get_system_equation(self.equation_number2), self.approximation1,
                                              self.approximation2, self.accuracy)

    def enter_accuracy(self):
        print("Enter accuracy:")
        str = INPUT_STREAM.readline().strip().split()
        while 1:
            if len(str) == 1:
                self.accuracy = float(str[0])
                break
            else:
                print("Accuracy should be only one value")

    def enter_borders(self):
        print("Enter borders, for example, 2 10:")
        borders = INPUT_STREAM.readline().strip().split()
        while 1:
            if len(borders) == 2:
                self.a = float(borders[0])
                self.b = float(borders[1])
                break
            else:
                print("Borders amount should be only two values")

    def enter_approximation(self):
        print("Enter approximation, it should be 2 values, for example, 1 1:")
        approximation = INPUT_STREAM.readline().strip().split()
        while 1:
            if len(approximation) == 2:
                self.approximation1, self.approximation2 = map(int, approximation)

                break
            else:
                print("Approximation amount should be only two values")

    def choose_calculating_method(self):
        print("Choose calculating method")
        print(f"1. Newton's method\n2. Simple iteration method\n3. Simple iteration method for equations system")
        while 1:
            str = INPUT_STREAM.readline().strip().split()
            if len(str) == 1:
                self.calculating_type = int(str[0])
                break
            else:
                print("No correct, please retry:")

    def read_from_console(self):
        if self.calculating_type == 3:
            self.enter_approximation()
        else:
            self.enter_borders()
        self.enter_accuracy()

    def get_data_file(self, file_name):
        try:
            with open(file_name) as file:
                return [list(map(float, row.split())) for row in file.readlines()]
        except FileNotFoundError:
            print("File not found")

    def read_from_file(self):
        print("Enter path to file:")
        file_name = INPUT_STREAM.readline().strip()
        file_data = self.get_data_file(file_name)
        if self.calculating_type == 3:
            if len(file_data[0]) == 2:
                self.approximation1 = int(file_data[0][0])
                self.approximation2 = int(file_data[0][1])
                print(f"approximation: {self.approximation1} and {self.approximation2}\n")
            else:
                print("approximation amount should be only two values")
                return
        else:
            if len(file_data[0]) == 2:
                self.a = int(file_data[0][0])
                self.b = int(file_data[0][1])
                print(f"a:{self.a} and b:{self.b}\n")
            else:
                print("Borders amount should be only two values")
                return
        if len(file_data[1]) == 1:
            self.accuracy = float(file_data[1][0])
        else:
            print("Accuracy should be only one value")
            return

    def choose_reading_type(self):
        print("Choose reading data type:\n1. write in console\n2. file")
        self.reading_type = INPUT_STREAM.readline().strip()

        match int(self.reading_type):
            case 1:
                self.read_from_console()
            case 2:
                self.read_from_file()

    def choose_equation(self):
        if (self.calculating_type == 3):
            print("Choose first equation")
            print(f"1. {self.system_equations[1]}\n2. {self.system_equations[2]}\n3. {self.system_equations[3]}")
            self.equation_number1 = int(INPUT_STREAM.readline().strip())

            print("Choose second equation")
            print(f"1. {self.system_equations[1]}\n2. {self.system_equations[2]}\n3. {self.system_equations[3]}")
            self.equation_number2 = int(INPUT_STREAM.readline().strip())
        else:
            print("Choose equation")
            print(f"1. {self.equations[1]}\n2. {self.equations[2]}\n3. {self.equations[3]}")
            self.equation_number = int(INPUT_STREAM.readline().strip())
            show_graph(self.get_equation( self.equation_number))

    def get_system_equation(self, equation_number):
        match equation_number:
            case 1:
                return lambda x, y: x ** 2 - 5 * y + 10
            case 2:
                return lambda x, y: 3 * x ** 3 - 2 * y
            case 3:
                return lambda x, y: (3 * x ** 2) / 5 + 3 * y + 2

    def get_equation(self, equation_number):
        match equation_number:
            case 1:
                return lambda x: -1.38 * x ** 3 - 5.42 * x ** 2 + 2.57 * x + 10.95
            case 2:
                return lambda x: math.e ** (3 * x) - 2 * x
            case 3:
                return lambda x: (3 * x ** 4) / 5 + 3

