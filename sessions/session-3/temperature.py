from __future__ import annotations
from temperature_scales import TemperatureScale

class Temperature():
    """
        Represents the temperature class to be instantiated
    """

    Value = None
    Scale = None
    
    def __init__(self, value: float, scale: TemperatureScale):
        """
            Creates a new instance of the class with a value and a scale.
        """

        self.Value = value
        self.Scale = scale
        pass

    def Add(self, other: Temperature) -> Temperature:
        """
            Adds an instance of temperature with another instance.
        """

        other = other.ConvertToScale(self.Scale)
        result = round(self.Value + other.Value, 2)
        return Temperature(result, self.Scale)

    def Substract(self, other: Temperature) -> Temperature:
        """        
            Substracts an instance of temperature with another instance.
        """

        other = other.ConvertToScale(self.Scale)
        result = round(self.Value - other.Value, 2)
        return Temperature(result, self.Scale)

    def MultiplyBy(self, other: Temperature) -> Temperature:
        """
            Mutliplies an instance of temperature with another instance.
        """


        other = other.ConvertToScale(self.Scale)
        result = round(self.Value * other.Value, 2)
        return Temperature(result, self.Scale)

    def DivideBy(self, other: Temperature) -> Temperature:
        """
            Divides an instance of temperature with another instance.
        """

        other = other.ConvertToScale(self.Scale)
        result = round(self.Value / other.Value, 2)
        return Temperature(result, self.Scale)
        
    def ToFarenheit(self) -> Temperature:
        """
            Converts the current instance to the Farenheit temperature scale.
        """

        result = None
        if (self.Scale.name == "Kelvin"):
            result = round((self.Value * 9/5) - 459.67, 2)
            pass
        
        elif (self.Scale.name == "Celcius"):
            result = round((self.Value * 9/5) + 32, 2)
            pass

        return Temperature(result, TemperatureScale.Farenheit)

    def ToCelcius(self) -> Temperature:
        """
            Converts the current instance to the Celcius temperature scale.
        """

        result = None
        if (self.Scale.name == "Kelvin"):
            result = round(self.Value - 273.15, 2)
            pass

        elif (self.Scale.name == "Farenheit"):
            result = round((self.Value - 32) * 5/9, 2)
            pass

        return Temperature(result, TemperatureScale.Celcius)

    def ToKelvin(self) -> Temperature:
        """
            Converts the current instance to the Kelvin temperature scale.
        """

        result = None
        if (self.Scale.name == "Celcius"):
            result = round(self.Value + 273.15, 2)
            pass

        elif (self.Scale.name == "Farenheit"):
            result = round((self.Value + 459.67) * 5/9, 2)
            pass

        return Temperature(result, TemperatureScale.Kelvin)

    def ConvertToScale(self, target: TemperatureScale) -> Temperature:
        """
            Converts the current instance to the specified temperature scale.
        """

        if (target.name == self.Scale.name):
            return self

        if (target.name == "Kelvin"):
            return self.ToKelvin()

        if (target.name == "Celcius"):
            return self.ToCelcius()

        if (target.name == "Farenheit"):
            return self.ToFarenheit()

        raise Exception("Invalid or empty temperature scale target.")