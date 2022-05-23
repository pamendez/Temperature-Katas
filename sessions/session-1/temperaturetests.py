from temperature import Temperature
from temperaturescale import TemperatureScale

def test_stringify_temperature():
    """
        Represents the first test case:
        Evaluates the ToString() method.
    """

    temp = Temperature(10, TemperatureScale.Celcius)
    expected = "10C" # Celcius
    actual = temp.ToString()
    assert actual == expected, "Invalid string conversion."

def test_convert_farenheit_to_celcius():
    """
        Represents the second test case:
        Converts a temperature from farenheit to celcius.
    """

    temp = Temperature(1, TemperatureScale.Farenheit)
    expected = -17.22 # Farenheit
    actual = temp.ToCelcius().Value
    assert actual == expected, f"Invalid conversion. Expected {expected}C, and result is {actual}C."

def test_sum_two_equal_scale_temperatures():
    """
        Represents the third test case:
        Sums two celcius temperatures.
    """

    temp1 = Temperature(2, TemperatureScale.Celcius)
    temp2 = Temperature(10, TemperatureScale.Celcius)
    expected = 12 # Celcius
    actual = temp1.Sum(temp2).Value
    assert actual == expected, f"Invalid sum. Expected {expected}C, and result is {actual}C."

def test_substract_two_equal_scale_temperatures():
    """
        Represents the fourth test case:
        Substract two farenheit temperatures.
    """
    
    temp1 = Temperature(19, TemperatureScale.Farenheit)
    temp2 = Temperature(21, TemperatureScale.Farenheit)
    expected = -2 # Farenheit
    actual = temp1.Substract(temp2).Value
    assert actual == expected, f"Invalid substraction. Expected {expected}F, and result is {actual}F." 

def test_mutliply_two_equal_scale_temperatures():
    """
        Represents the fifth test case:
        Multiplies two kelvin temperatures
    """

    temp1 = Temperature(3, TemperatureScale.Kelvin)
    temp2 = Temperature(9, TemperatureScale.Kelvin)
    expected = 27 # Kelvin
    actual = temp1.MultiplyBy(temp2).Value
    assert actual == expected, f"Invalid multiplication. Expected {expected}K, and result is {actual}K." 

def test_divide_two_equal_scale_temperatures():
    """
        Represents the sixth test case:
        Divides two celcius temperatures.
    """

    temp1 = Temperature(13, TemperatureScale.Celcius)
    temp2 = Temperature(2, TemperatureScale.Celcius)
    expected = 6.5 # Celcius
    actual = temp1.DivideBy(temp2).Value
    assert actual == expected, f"Invalid division. Expected {expected}C, and result is {actual}C." 

def test_convert_celcius_to_kelvin():
    """
        Represents the seventh test case:
        Converts a temperature from celcius to kelvin.
    """

    temp = Temperature(2, TemperatureScale.Celcius)
    expected = 275.15 # Kelvin
    actual = temp.ToKelvin().Value
    assert actual == expected, f"Invalid conversion. Expected {expected}K, and result is {actual}K"

def test_sum_two_different_scale_temperatures():
    """
        Represents the eigthth test case:
        Sums two temperatures: one is celcius and other is farenheit.
    """ 

    temp1 = Temperature(1, TemperatureScale.Celcius)
    temp2 = Temperature(9, TemperatureScale.Farenheit)
    expected = -11.78 # Celcius
    actual = temp1.Sum(temp2).Value
    assert actual == expected, f"Invalid sum. Expected {expected}C, and result is {actual}C." 

def test_substraction_two_different_scale_temperatures():
    """
        Represents the ninth test case:
        Substracts two temperatures: one is kelvin and other is celcius.
    """

    temp1 = Temperature(2, TemperatureScale.Kelvin)
    temp2 = Temperature(2, TemperatureScale.Celcius)
    expected = -273.15 # Kelvin
    actual = temp1.Substract(temp2).Value
    assert actual == expected, f"Invalid substraction. Expected {expected}K, and result is {actual}K."

def test_multiplication_two_different_scale_temperatures():
    """
        Represents the tenth test case:
        Multiplies two temperatures: one is kelvin and other is celcius.
    """

    temp1 = Temperature(2, TemperatureScale.Kelvin)
    temp2 = Temperature(-2, TemperatureScale.Celcius)
    expected = 542.3 # Kelvin
    actual = temp1.MultiplyBy(temp2).Value
    assert actual == expected, f"Invalid multiplication. Expected {expected}K, and result is {actual}K."

def test_division_two_different_scale_temperatures():
    """
        Represents the eleventh test case:
        Divides two temperatures: one is farenheit and other is celcius.
    """

    temp1 = Temperature(6, TemperatureScale.Farenheit)
    temp2 = Temperature(10, TemperatureScale.Celcius)
    expected = 0.12 # Farenheit
    actual = temp1.DivideBy(temp2).Value
    assert actual == expected, f"Invalid division. Expected {expected}F, and result is {actual}F."

def test_convert_farenheit_to_kelvin():
    """
        Represents the twelveth test case:
        Converts a farenheit temperature to kelvin.
    """

    temp = Temperature(8, TemperatureScale.Farenheit)
    expected = 259.82
    actual = temp.ToKelvin().Value
    assert actual == expected, f"Invalid conversion. Expected {expected}K, and result is {actual}K."


def test_convert_kelvin_to_celcius():
    """
        Represents the thirteenth:
        Converts a kelvin to celcius.
    """

    temp = Temperature(64, TemperatureScale.Kelvin)
    expected = -209.15
    actual = temp.ToCelcius().Value
    assert actual == expected, f"Invalid conversion. Expected {expected}C, and result is {actual}C."

def test_convert_celcius_to_celcius():
    """
        Represenths the fourteenth and final test case:
        Converts a celcius to celcius.
    """

    temp = Temperature(-1, TemperatureScale.Celcius)
    expected = -1
    actual = temp.ToCelcius().Value
    assert actual == expected, f"Invalid conversion. Expected {expected}C, and result is {actual}C."