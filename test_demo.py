#
# Test the factorial() function.
#
import demo


def test_fact_1():
    assert demo.factorial(1) == 1


def test_fact_2():
    assert demo.factorial(2) == 2


def test_fact_3():
    assert demo.factorial(3) == 6


def test_fact_10():
    assert demo.factorial(10) == 3628800


def test_fact_20():
    assert demo.factorial(20) == 2432902008176640000


def test_fact_30():
    assert demo.factorial(30) == 265252859812191058636308480000000


def test_fact_40():
    assert demo.factorial(40) == \
        815915283247897734345611269596115894272000000000


def test_fact_50():
    assert demo.factorial(50) == \
        30414093201713378043612608166064768844377641568960512000000000000
