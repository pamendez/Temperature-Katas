from temperature import Temperature
from temperature_scale import TemperatureScale
import pytest

def test_convert_from_farenheit_to_celcius():
    """
        Test case 01: Convert a temperature from farenheit to celcius.
    """

    temp = Temperature(10, TemperatureScale.Farenheit)
    new_temp = temp.ToCelcius()
    expected = -12.22 # Celcius
    actual = new_temp.Value
    assert actual == expected, f"Invalid conversion. Expected value does not match actual value. {expected}C != {actual}C."

def test_sum_two_equal_scale_temps():
    """
        Test case 02: Sum two temperatures with same scales. 
        In this case, Celcius will be used as the scale.
    """

    temp1 = Temperature(12, TemperatureScale.Celcius)
    temp2 = Temperature(10, TemperatureScale.Celcius)
    expected = 22 # Celcius
    actual = temp1.Add(temp2).Value
    assert actual == expected, f"Sum does not match expected result. {expected}C != {actual}C."

def test_sub_two_equal_scale_temps():
    """
        Test case 03: Substract two temperatures with same scales.
        In this case, Farenheit will be used as the scale.
    """

    temp1 = Temperature(22, TemperatureScale.Farenheit)
    temp2 = Temperature(19, TemperatureScale.Farenheit)
    expected = 3 # Farenheit
    actual = temp1.Substract(temp2).Value
    assert actual == expected, f"Substraction does not match expected result. {expected}F != {actual}F."

def test_multiply_two_equal_scale_temps():
    """
        Test case 04: Multiply two temperatures with same scales.
        In this case, Kelvin will be used as the scale.
    """

    temp1 = Temperature(45, TemperatureScale.Kelvin)
    temp2 = Temperature(2, TemperatureScale.Kelvin)
    expected = 90 # Kelvin
    actual = temp1.MultiplyBy(temp2).Value
    assert actual == expected, f"Multiplication does not match expected result. {expected}K != {actual}K."

def test_divide_two_equal_scale_temps():
    """
        Test case 05: Divide two temperatures with same scales.
        In this case, Celcius will be used as the scale.
    """    

    temp1 = Temperature(15, TemperatureScale.Celcius)
    temp2 = Temperature(6, TemperatureScale.Celcius)
    expected = 2.5
    actual = temp1.DivideBy(temp2).Value
    assert actual == expected, f"Division does not match expected result. {expected}C != {actual}C."

def test_sum_two_different_scale_temps():
    """
        Test case 06: Sum two temperatures with different scales.
        In this case, a temperature with Celcius scale and another with Farenheit scale will be used.
    """

    temp1 = Temperature(10, TemperatureScale.Celcius)
    temp2 = Temperature(11, TemperatureScale.Farenheit)
    expected = -1.67 # Celcius
    actual = temp1.Add(temp2).Value
    assert actual == expected, f"Sum does not match expected value. {expected}C != {actual}C."

def test_sub_two_different_scale_temps():
    """
        Test case 07: Substract two temperatures with different scales.
        In this case, a temperature with Kelvin scale and another with Celcius scale will be used.
    """

    temp1 = Temperature(-1, TemperatureScale.Kelvin)
    temp2 = Temperature(1, TemperatureScale.Celcius)
    expected = -275.15 # Kelvin
    actual = temp1.Substract(temp2).Value
    assert actual == expected, f"Substraction does not match expected result. {expected}K != {actual}K"

def test_multiply_two_different_scale_temps():
    """
        Test case 08: Multiply two temperatures with different scales.
        In this case, a temperature with Farenheit scale and another with Celcius scale will be used. 
    """

    temp1 = Temperature(10, TemperatureScale.Farenheit)
    temp2 = Temperature(0, TemperatureScale.Celcius)
    expected = 320 # Farenheit
    actual = temp1.MultiplyBy(temp2).Value
    assert actual == expected, f"Multiplication does not match expected result. {expected}F != {actual}F."

def test_divide_two_different_scale_temps():
    """
        Test case 09: Divide two temperatures with different scales.
        In this case, a temperature with Kelvin scale and another with Farenheit scale will be used.
    """

    temp1 = Temperature(-100, TemperatureScale.Kelvin)
    temp2 = Temperature(-100, TemperatureScale.Farenheit)
    expected = -0.5 # Kelvin
    actual = temp1.DivideBy(temp2).Value
    assert actual == expected, f"Divisio does not match expected result. {expected}K != {actual}K."

def test_target_conversion_1():
    """
        Test case 10: Converts a temperature to a specified target.
        Converts a celcius temperature to a farenheit temperature.
    """

    temp = Temperature(10, TemperatureScale.Celcius)
    conv_temp = temp.ConvertToTarget(TemperatureScale.Farenheit)
    expected = (50, "Farenheit")
    actual = (conv_temp.Value, conv_temp.Scale.name)
    assert actual == expected, f"Invalid conversion. Expected conversion is {expected} and actual is {actual}."

def test_target_conversion_2():
    """
        Test case 11: Converts a temperature to a specified target.
        Convers a farenheit temperature to a kelvin temperature.
    """

    temp = Temperature(64, TemperatureScale.Farenheit)
    conv_temp = temp.ConvertToTarget(TemperatureScale.Kelvin)
    expected = (290.93, "Kelvin")
    actual = (conv_temp.Value, conv_temp.Scale.name)
    assert actual == expected, f"Invalid conversion. Expected conversion is {expected} and actual is {actual}."

def test_target_conversion_error():
    """
        Test case 12: Failure to convert a temperature to a specified target.
        An exception should be raised here.
    """

    with pytest.raises(Exception) as ex:
        temp = Temperature(0, TemperatureScale.Celcius)
        conv_temp = temp.ConvertToTarget(None)

def test_target_conversion_3():
    """
        Test case 13: Convert a temperature from farenheit to celcius.
        Convers a farenheit temperature to a celcius temperature.
        * Note: This test case reimplements test case 01.
    """

    temp = Temperature(16, TemperatureScale.Farenheit)
    conv_temp = temp.ConvertToTarget(TemperatureScale.Celcius)
    expected = (-8.89, "Celcius")
    actual = (conv_temp.Value, conv_temp.Scale.name)
    assert actual == expected, f"Invalid conversion. Expected conversion is {expected} and actual is {actual}."
