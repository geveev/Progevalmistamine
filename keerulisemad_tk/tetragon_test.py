"""Test for tetragon_builder"""
import pytest

from tetragon_builder import tetragon_builder


@pytest.mark.parametrize("height, length, expected", [
    (4, 3, "***\n* *\n* *\n***"),
    (7, 2, "**\n**\n**\n**\n**\n**\n**"),
    (5, 5, "*****\n*   *\n*   *\n*   *\n*****"),
])
def test_tetragon_works(height, length, expected):
    assert tetragon_builder(height, length) == expected


def test_single_asteriks():
    height = 1
    length = 1
    result = tetragon_builder(height, length)
    assert result == "*"


def test_single_line():
    height = 1
    length = 2
    result = tetragon_builder(height, length)
    assert result == "**"


def test_small_cube():
    height = 2
    length = 2
    result = tetragon_builder(height, length)
    assert result == "**\n**"
