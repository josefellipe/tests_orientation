from .moks.calculatos import NumbersIn, Result
from src.calculator.basic_operations import sum_numbers

def test_calculator1():
    result1 = sum_numbers(NumbersIn.firstIn[0], NumbersIn.firstIn[1])
    result2 = sum_numbers(NumbersIn.secondIn[0], NumbersIn.secondIn[1])
    result3 = sum_numbers(NumbersIn.thirdIn[0], NumbersIn.thirdIn[1])
    assert Result.firstResult == result1
    assert Result.secondResult == result2
    assert Result.thirdResult == result3
    