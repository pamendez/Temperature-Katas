import pytest
from temperature import Temperature
from temperaturescale import TemperatureScale

def test_stringify_temperature():
    """
        Represents the first test case:
        Evaluates the ToString() method.
    """

    temp = Temperature(10, TemperatureScale.Celcius)
    expected = "10C"
    actual = temp.ToString()
    assert(actual == expected, "Invalid string conversion.")

def test_convert_farenheit_to_celcius():
    """
        Represents the second test case:
        Converts a temperature from farenheit to celcius.
    """

    temp = Temperature(1, TemperatureScale.Farenheit)
    expected = -17.22
    actual = temp.ToFarenheit().Value
    assert(actual == expected, f"Invalid conversion. Expected {expected}C, and result is {actual}C.")

def test_sum_two_equal_scale_temperatures():
    """
        Represents the third test case:
        Sums two celcius temperatures.
    """

    temp1 = Temperature(2, TemperatureScale.Celcius)
    temp2 = Temperature(10, TemperatureScale.Celcius)
    expected = 12
    actual = temp1.Sum(temp2)
    assert(actual == expected, f"Invalid sum. Expected {expected}C, and result is {actual}C.")

def test_substract_two_equal_scale_temperatures():
    """
        Represents the fourth test case:
        Substract two farenheit temperatures.
    """
    
    temp1 = Temperature(19, TemperatureScale.Farenheit)
    temp2 = Temperature(21, TemperatureScale.Farenheit)
    expected = -2
    actual = temp1.Substract(temp2)
    assert(actual == expected, f"Invalid substraction. Expected {expected}F, and result is {actual}F.")

def test_mutliply_two_equal_scale_temperatures():
    """
        Represents the fifth test case:
        Multiplies two kelvin temperatures
    """

    temp1 = Temperature(3, TemperatureScale.Kelvin)
    temp2 = Temperature(9, TemperatureScale.Kelvin)
    expected = 27
    actual = temp1.MultiplyBy(temp2)
    assert(actual == expected, f"Invalid multiplication. Expected {expected}K, and result is {actual}K.")

def test_divide_two_equal_scale_temperatures():
    """
        Represents the sixth test case:
        Divides two celcius temperatures.
    """

    temp1 = Temperature(13, TemperatureScale.Celcius)
    temp2 = Temperature(2, TemperatureScale.Celcius)
    expected = 6.5
    actual = temp1.DivideBy(temp2)
    assert(actual == expected, f"Invalid division. Expected {expected}C, and result is {actual}C.")

def test_convert_celcius_to_kelvin():
    """
        Represents the seventh test case:
        Converts a temperature from celcius to kelvin.
    """

    temp = Temperature(2, TemperatureScale.Celcius)
    expected = 274.15
    actual = temp.ToKelvin().Value
    assert(actual == expected, f"Invalid conversion. Expected {expected}K, and result is {actual}K")