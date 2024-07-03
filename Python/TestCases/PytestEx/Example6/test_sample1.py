import pytest

class TestClass():
    def setup_class(self):
        print("setup class called once")
        
    def teardown_class(self):
        print("teardown class called once")
        
    def setup_method(self):
        print("setup method called before every test case")
        
    def teardown_method(self):
        print("teardown method called after every test case")
        
    def test_one(self):
        print("one")
        assert True
        
    def test_two(self):
        print("two")
        assert False