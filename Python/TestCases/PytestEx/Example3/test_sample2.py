import pytest

@pytest.mark.set2
def test_file1_method2():
    x = 10
    y = 14

    assert x+4 == y
   
@pytest.mark.set1 
def test_file1_check2():
    x = 7
    y = 9
    
    assert x+2 == y 