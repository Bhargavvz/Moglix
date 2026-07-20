import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from solution import longest_valid_parentheses


def test_example_1():
    assert longest_valid_parentheses("(()") == 2


def test_example_2():
    assert longest_valid_parentheses(")()())") == 4


def test_example_3_empty_string():
    assert longest_valid_parentheses("") == 0


def test_no_parentheses_match():
    assert longest_valid_parentheses(")))(((") == 0


def test_all_valid():
    assert longest_valid_parentheses("()()()") == 6


def test_nested_valid():
    assert longest_valid_parentheses("(((())))") == 8


def test_single_open():
    assert longest_valid_parentheses("(") == 0


def test_single_close():
    assert longest_valid_parentheses(")") == 0


def test_mixed_with_trailing_invalid():
    assert longest_valid_parentheses("()(()") == 2


def test_large_valid_block_after_invalid_prefix():
    assert longest_valid_parentheses(")(()())") == 6