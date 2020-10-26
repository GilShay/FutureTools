import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
        print(TypeError)
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)

print("First")
test_capital_case()
test_raises_exception_on_non_string_arguments()
print("Last")