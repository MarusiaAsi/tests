import pytest
from main import Calculator


def setup() :
    print("basic setup into module")


def teardown() :
    print("basic teardown into module")


def setup_module(module) :
    print("module setup")


def teardown_module(module) :
    print("module teardown")


def setup_function(function) :
    print("function setup")


def teardown_function(function) :
    print("function teardown")


def test_numbers_3_4() :
    print
    "test 3*4"
    assert 3 * 4 == 12


def test_strings_a_3() :
    print
    "test a*3"
    assert 'a' * 3 == 'aaa'


class TestUM :
    def setup(self) :
        print("basic setup into class")

    def teardown(self) :
        print("basic teardown into class")

    def setup_class(Calculator) :
        print("class setup")

    def teardown_class(Calculator) :
        print("class teardown")

    def test_numbers_add(self) :
        print("test 5+5")
        a = Calculator()
        assert a.add(5, 5) == 10

    def test_numbers_multiply(self) :
        print("test 5*6")
        a = Calculator()
        assert a.multiply(5, 5) == 25

    def test_numbers_subtract(self) :
        print("test 5-4")
        a = Calculator()
        assert a.subtract(5, 5) == 0

    def test_numbers_divide(self) :
        print("test 5/5")
        a = Calculator()
        assert a.divide(5, 5) == 1
