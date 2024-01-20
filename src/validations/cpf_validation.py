
def validate_cpf(cpf:str) -> bool:
    cpf_numbers = ''.join([num for num in cpf if num.isnumeric()])
    if len(cpf_numbers) == 11:
        return True
    return False