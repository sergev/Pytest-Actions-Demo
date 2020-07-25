#
# Test the factorial() function.
#
from demo import *
import pytest

def test_fact_1():
    assert factorial(1) == 1

def test_fact_2():
    assert factorial(2) == 2

def test_fact_3():
    assert factorial(3) == 6

def test_fact_10():
    assert factorial(10) == 3628800

def test_fact_20():
    assert factorial(20) == 2432902008176640000

def test_fact_30():
    assert factorial(30) == 265252859812191058636308480000000

def test_fact_40():
    assert factorial(40) == 815915283247897734345611269596115894272000000000

def test_fact_50():
    assert factorial(50) == 30414093201713378043612608166064768844377641568960512000000000000
