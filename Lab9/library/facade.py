from library.logger import Logger


class LabFacade:
    """Реалізація патерну Facade"""

    def __init__(self):
        self.logger = Logger()

    @Logger().log_function_call
    def execute_lab1(self):
        """Виконати Lab 1"""
        from lab1.main_LAB1 import run as run_lab1
        run_lab1()

    @Logger().log_function_call
    def execute_lab2(self):
        """Виконати Lab 2"""
        from lab2.main_LAB2 import calculator
        calculator()

    @Logger().log_function_call
    def execute_lab3(self):
        """Виконати Lab 3"""
        from lab3.main_LAB3 import start_console_interface
        start_console_interface()

    @Logger().log_function_call
    def execute_lab4(self):
        """Виконати Lab 4"""
        from lab4.main_LAB4 import run as run_lab4
        run_lab4()

    @Logger().log_function_call
    def execute_lab5(self):
        """Виконати Lab 5"""
        from lab5.main_LAB5 import main
        main()

    @Logger().log_function_call
    def execute_lab6(self):
        """Виконати Lab 6"""
        import unittest
        from lab6.test_calculator_LAB6 import TestCalculator
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
        runner = unittest.TextTestRunner()
        runner.run(suite)

    @Logger().log_function_call
    def execute_lab7(self):
        """Виконати Lab 7"""
        from lab7.main_LAB7 import run as run_lab7
        run_lab7()

    @Logger().log_function_call
    def execute_lab8(self):
        """Виконати Lab 8"""
        from lab8.main_LAB8 import run as run_lab8
        run_lab8()