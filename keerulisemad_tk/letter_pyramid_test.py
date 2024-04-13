"""Test for tetragon_builder"""
import pytest

from letter_pyramid import letter_pyramid


@pytest.mark.parametrize("letters, expected", [
    ("tere õhtust", "   t\n"
                    "  e r\n"
                    " e õ h\n"
                    "t u s t"),
    ("Tere Hommikust", "    T\n"
                       "   e r\n"
                       "  e H o\n"
                       " m m i k\n"
                       "u s t"),
    ("head ööd alligaator <3", "     h\n"
                               "    e a\n"
                               "   d ö ö\n"
                               "  d a l l\n"
                               " i g a a t\n"
                               "o r < 3")

])
def test_tetragon_works(letters, expected):
    assert letter_pyramid(letters) == expected


def test_single_letter_string():
    letters = "a"
    result = letter_pyramid(letters)
    assert result == "a"


def test_single_with_spaces():
    letters = "  a     "
    result = letter_pyramid(letters)
    assert result == "a"


def test_also_numbers_work():
    letters = "14671"
    result = letter_pyramid(letters)
    assert result == ("  1\n"
                      " 4 6\n"
                      "7 1")


def test_symbols_also_work():
    letters = "&#¤/##)#/=)([{]}%"
    result = letter_pyramid(letters)
    assert result == ("     &\n"
                      "    # ¤\n"
                      "   / # #\n"
                      "  ) # / =\n"
                      " ) ( [ { ]\n"
                      "} %")
