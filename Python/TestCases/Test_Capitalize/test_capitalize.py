import pytest
def capital_case(x):
    return x.upper()

def test_capital_case():
    assert capital_case('hello') == 'HELLO'
   