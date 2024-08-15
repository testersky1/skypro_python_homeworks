import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize('word, result', [
     ("хугарден", "Хугарден") 
])
def test_capitalize_positive(word, result):
    res = utils.capitilize(word)
    assert res == result

@pytest.mark.parametrize('word, result', [
    ("123", "123"),
    ("", ""),
    ("abcdef", "Abcdef")
])
def test_capitalize_negative(word, result):
    res = utils.capitilize(word)
    assert res == result

@pytest.mark.parametrize('word, result', [
    ("        пробел", "пробел"),
    ("   leading", "leading")
])
def test_trim_positive(word, result):
    res = utils.trim(word)
    assert res == result

@pytest.mark.parametrize('word, result', [
    ("", ""),
    ("alreadyTrimmed", "alreadyTrimmed")
])
def test_trim_negative(word, result):
    res = utils.trim(word)
    assert res == result

@pytest.mark.parametrize("input, delimiter, result", [
    ("персик,яблоко,груша", ",", ["персик", "яблоко", "груша"]),
    ("one;two;three", ";", ["one", "two", "three"])
])
def test_to_list_positive(input, delimiter, result):
    res = utils.to_list(input, delimiter)
    assert res == result

@pytest.mark.parametrize("input, delimiter, result", [
    ("персик", ",", ["персик"]),
    ("onlyone", ";", ["onlyone"])
])
def test_to_list_negative(input, delimiter, result):
    res = utils.to_list(input, delimiter)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("Symbol", "y", True),
    ("Hello", "H", True),
    ("Test", "t", True)
])
def test_contains_positive(input, symbol, result):
    res = utils.contains(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("Symbol", "a", False),
    ("Hello", "z", False)
])  
def test_contains_negative(input, symbol, result):
    res = utils.contains(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("carp", "p", "car"),
    ("hello", "l", "heo")
])
def test_delete_symbol_positive(input, symbol, result):
    res = utils.delete_symbol(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("corner", "er", "corn"),
    ("hello", "z", "hello")
])
def test_delete_symbol_negative(input, symbol, result):
    res = utils.delete_symbol(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("Кристофоро", "К", True),
    ("apple", "a", True)
])
def test_starts_with_positive(input, symbol, result):
    res = utils.starts_with(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("кристофоро", "К", False),
    ("banana", "b", True)
])
def test_starts_with_negative(input, symbol, result):
    res = utils.starts_with(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("common", "n", True),
    ("hello", "o", True)
])
def test_ends_with_positive(input, symbol, result):
    res = utils.end_with(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, symbol, result", [
    ("commoN", "n", False),
    ("world", "d", True)
])
def test_ends_with_negative(input, symbol, result):
    res = utils.end_with(input, symbol)
    assert res == result

@pytest.mark.parametrize("input, result", [
    (" ", True)
])
def test_is_empty_positive(input, result):
    res = utils.is_empty(input)
    assert res == result

@pytest.mark.parametrize("input, result", [
    ("эта строка пустая",  False),
    (" ", True)
])
def test_is_empty_negative(input, result):
    res = utils.is_empty(input)
    assert res == result

@pytest.mark.parametrize("lst, joiner, result", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),  
    (["Sky", "Pro"], ", ", "Sky, Pro"),  
    (["Sky", "Pro"], "-", "Sky-Pro"),    
    ([], ", ", ""),                      
    ([1, 2, 3], "; ", "1; 2; 3"),        
    ([True, False], " or ", "True or False")  
])
def test_list_to_string_positive(lst, joiner, result):
    res = utils.list_to_string(lst, joiner)
    assert res == result

@pytest.mark.parametrize("lst, joiner", [
    ("not a list", ", "),  
    ([1, 2, 3], None)      
])
def test_list_to_string_negative(lst, joiner):
    with pytest.raises(Exception):
        utils.list_to_string(lst, joiner)