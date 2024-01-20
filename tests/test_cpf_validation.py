from src.validations.cpf_validation import validate_cpf
from .moks.cpfs import CPFIn, Result

def test_validate_cpf():
    result1 = validate_cpf(CPFIn.firstIn)
    result2 = validate_cpf(CPFIn.secondIn)
    result3 = validate_cpf(CPFIn.thirdIn)
    result4 = validate_cpf(CPFIn.fourthIn)
    assert result1 == Result.firstResult
    assert result2 == Result.secondResult
    assert result3 == Result.thirdResult
    assert result4 == Result.fourthResult