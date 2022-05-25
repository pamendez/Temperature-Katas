from temperature import Temperature
from temperature_scales import TemperatureScale
import pytest

def test_case_conversion_1():
    """
        Represents the test case #01: 
        It converts a temperature to a given scale (Celcius to Farenheit).
    """

    temp1 = Temperature(11, TemperatureScale.Celcius)
    new_temp = temp1.ConvertToScale(TemperatureScale.Farenheit)
    expected = (51.8, "Farenheit")
    actual = (new_temp.Value, new_temp.Scale.name)
    assert actual == expected, "Conversion is invalid."

def test_case_sum_temps_equal_scales():
    """
        Represents the test case #02:
        Sums two temperatures with equal scales (Celcius and Celcius).
    """

    temp1 = Temperature(19, TemperatureScale.Celcius)
    temp2 = Temperature(21, TemperatureScale.Celcius)
    expected = (40, "Celcius")
    result = temp1.Add(temp2)
    actual = (result.Value, result.Scale.name)
    assert actual == expected, "Sum of temperatures is invalid."    

def test_case_sub_temps_equal_scales():
    """
        Represents tbe test case #03:
        Substracts two temperatures with equal scales (Kelvin and Kelvin).
    """

    temp1 = Temperature(40, TemperatureScale.Kelvin)
    temp2 = Temperature(18, TemperatureScale.Kelvin)
    expected = (22, "Kelvin")
    result = temp1.Substract(temp2)
    actual = (result.Value, result.Scale.name)
    assert actual == expected, "Substraction is invalid"
    pass

def test_case_mutliply_temps_equal_scales():
    """
        Represents the test case #04:
        Multiplies two temperatures with equal scales (Farenheit and Farenheit).
    """

    temp1 = Temperature(8, TemperatureScale.Farenheit)
    temp2 = Temperature(3, TemperatureScale.Farenheit)
    expected = (24, "Farenheit")
    result = temp1.MultiplyBy(temp2)
    actual = (result.Value, result.Scale.name)
    assert actual == expected, "Multiplication is invalid."

def test_case_divide_temps_equal_scales():
    """
        Represents the test case #05:
        Divides two temperatures with equal scales (Celcius and Celcius).
    """

    temp1 = Temperature(9, TemperatureScale.Celcius)
    temp2 = Temperature(4, TemperatureScale.Celcius)
    expected = (2.25, "Celcius")
    result = temp1.DivideBy(temp2)
    actual =  (result.Value, result.Scale.name)
    assert actual == expected, "Division is invalid."

def test_case_sum_temps_different_scales():
    """
        Represents the test case #06:
        Sums two temperatures with different scales (Celcius and Kelvin).
    """

    temp1 = Temperature(4, TemperatureScale.Celcius)
    temp2 = Temperature(0, TemperatureScale.Kelvin)
    expected = (-269.15, "Celcius")
    result = temp1.Add(temp2)
    actual = (result.Value, result.Scale.name)
    assert actual == expected, "Sum is invalid."

def test_case_sub_temps_different_scales():
    """
        Represents the test case 07:
        Subtracts two temperatures with different scales (Farenheit and Kelvin).
    """

    temp1 = Temperature(7, TemperatureScale.Farenheit)
    temp2 = Temperature(10, TemperatureScale.Kelvin)
    expected = (448.67, "Farenheit")
    result = temp1.Substract(temp2)
    actual = (result.Value, result.Scale.name)
    assert actual == expected, "Substraction is invalid."

def test_case_multiply_temps_different_scales():
    """
        Represents the test case #08:
        Multiplies two temperatures with different scales (Farenheit and Celcius).
    """

    temp1 = Temperature(0, TemperatureScale.Farenheit)
    temp2 = Temperature(11, TemperatureScale.Celcius)
    expected = (0, "Farenheit")
    result = temp1.MultiplyBy(temp2)
    actual = (result.Value, result.Scale.name)
    assert actual == expected, "Multiplication is invalid."

def test_case_divide_temps_different_scales():
    """
        Represents the test case #09:
        Divides two temperatures with different scales (Kelvin and Celcius).
    """

    temp1 = Temperature(100, TemperatureScale.Kelvin)
    temp2 = Temperature(-200, TemperatureScale.Celcius)
    expected = (1.37, "Kelvin")
    result = temp1.DivideBy(temp2)
    actual = (result.Value, result.Scale.name)
    assert actual == expected, "Division is invalid."

def test_case_conversion_2():
    """
        Represents the test case #10: 
        It converts a temperature to a given scale (Farenheit to Celcius).
    """


    temp = Temperature(17, TemperatureScale.Farenheit)
    new_temp = temp.ConvertToScale(TemperatureScale.Celcius)
    expected = (-8.33, "Celcius")
    actual = (new_temp.Value, new_temp.Scale.name)
    assert actual == expected, "Conversion is invalid."

def test_case_conversion_3():
    """
        Represents the test case #11:
        It converts a temperature to a given scale (Celcius to Kelvin).
    """


    temp = Temperature(8, TemperatureScale.Celcius)
    new_temp = temp.ConvertToScale(TemperatureScale.Kelvin)
    expected = (281.15, "Kelvin")
    actual = (new_temp.Value, new_temp.Scale.name)
    assert actual == expected, "Conversion is invalid."

def test_case_conversion_4():
    """
        Represents the test case #12: 
        It converts a temperature to a given scale (Kelvin to Celcius).
    """

    temp = Temperature(64, TemperatureScale.Kelvin)
    new_temp = temp.ConvertToScale(TemperatureScale.Celcius)
    expected = (-209.15, "Celcius")
    actual = (new_temp.Value, new_temp.Scale.name)
    assert actual == expected, "Conversion is invalid."

def test_case_conversion_5():
    """
        Represents the test case #13: 
        It converts a temperature to a given scale (Kelvin to Farenheit).
    """

    temp = Temperature(0, TemperatureScale.Kelvin)
    new_temp = temp.ConvertToScale(TemperatureScale.Farenheit)
    expected = (-459.67, "Farenheit")
    actual = (new_temp.Value, new_temp.Scale.name)
    assert actual == expected, "Conversion is invalid."

def test_case_conversion_6():
    """
        Represents the test case #14: 
        It converts a temperature to a given scale (Farenheit to Kelvin).
    """

    temp = Temperature(73, TemperatureScale.Farenheit)
    new_temp = temp.ConvertToScale(TemperatureScale.Kelvin)
    expected = (295.93, "Kelvin")
    actual = (new_temp.Value, new_temp.Scale.name)
    assert actual == expected, "Conversion is invalid."

def test_case_conmmutative_property_add():
    """
        Represents the test case #15:
        Validates the conmmutative property of addition of temperatures.
    """

    temp1 = Temperature(7, TemperatureScale.Celcius)
    temp2 = Temperature(10, TemperatureScale.Celcius)
    expected = (7 + 10 == 10 + 7) # Celcius
    actual = (temp1.Add(temp2).Value == temp2.Add(temp1).Value)
    assert actual == expected, "Conmmutative property is not true."

def test_case_conmmutative_property_multiplication():
    """
        Represents the test case #16:
        Validates the conmmutative property of multiplication of temperatures.
    """

    temp1 = Temperature(4, TemperatureScale.Celcius)
    temp2 = Temperature(5, TemperatureScale.Celcius)
    expected = (4 * 5 == 5 * 4) # Celcius
    actual = (temp1.MultiplyBy(temp2).Value == temp2.MultiplyBy(temp1).Value)
    assert actual == expected, "Conmmutative property is not true."

def test_case_conversion_failure_exception():
    """
        Represents the test case #17:
        Verifies whether the conversion function returns exception when invalid value is inserted.
    """

    temp = Temperature(10, TemperatureScale.Celcius)
    with pytest.raises(Exception) as ex:
        new_temp = temp.ConvertToScale(None)
        pass