import pytest
from multi_bracket_validation import multi_bracket_validation

# {}	TRUE
def test_one():
    assert multi_bracket_validation('{}')

# {}(){}	TRUE
def test_two():
    assert multi_bracket_validation('{}(){}')

# ()[[Extra Characters]]	TRUE
def test_three():
    assert multi_bracket_validation('()[[Extra Characters]]')

# (){}[[]]	TRUE
def test_four():
    assert multi_bracket_validation('(){}[[]]')

# {}{Code}[Fellows](())	TRUE
def test_five():
    assert multi_bracket_validation('{}{Code}[Fellows](())')

# [({}]	FALSE
def test_six():
    not multi_bracket_validation('[({}]')

# (](	FALSE
def test_seven():assert not multi_bracket_validation('(](')

# {(})	FALSE
def test_eight():
    assert not multi_bracket_validation('{(})')