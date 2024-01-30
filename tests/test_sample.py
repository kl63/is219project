"""
This module contains unit tests for the functions in the app module.
"""

from app import add, sub

def test_add():
    """
    Test the add function.

    This function asserts that the add function returns the expected sum.
    """
    assert add(2, 2) == 4

def test_subtract():
    """
    Test the subtract function.

    This function asserts that the subtract function returns the expected difference.
    """
    assert sub(2, 2) == 0
