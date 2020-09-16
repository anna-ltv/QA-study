import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculation_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculation_correctly(self):
        assert self.calc.subtraction(self, 15, 1) == 14

    def test_adding_calculation_correctly(self):
        assert self.calc.adding(self, 13, 15) == 28

    def test_multiply_calculation_correctly(self):
        assert self.calc.multiply(self, 15, 3) == 45