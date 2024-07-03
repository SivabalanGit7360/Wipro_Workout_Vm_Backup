import pytest

@pytest.mark.set1
def test_file_method1():
    x = 5
    y = 6
    assert x+1 == y , "test failed"
    assert x == y , "test failed"
    
@pytest.mark.set2
def test_file_check1():
    x = 5
    y = 6
    assert x+1 == y , "test failed" 
    