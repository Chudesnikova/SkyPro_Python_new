import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive_test(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative_test(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("       Hello", "Hello"),
    ("   python HW", "python HW"),
])
def test_trim_positive_test(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("12345   ", "12345   "),
    ("", ""),
    ("Python", "Python"),
])
def test_trim_negative_test(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Skypro", "S", True),
    ("Hello, user1!", "1", True),
    ("Python HW", "W", True),
])
def test_contains_positive_test(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Python HW", "1", False)
])
def test_contains_negative_test(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Skypro", "o", "Skypr"),
    ("Hello, user1!", "1", "Hello, user!"),
    ("Python HW", "P", "ython HW"),
])
def test_delete_symbol_positive_test(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Python HW", "Q", "Python HW")
], [])
def test_delete_symbol_negative_test(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected







