from bank import value


def test_greet_with_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_greeting_starting_with_h():
    assert value("How are you doing") == 20
    assert value("how are you doing") == 20

def test_greeting_other_than_h_or_hello():
    assert value("what's happening?") == 100
