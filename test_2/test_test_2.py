from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100

def test_convert_for_exceptions():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("4/3")

    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"