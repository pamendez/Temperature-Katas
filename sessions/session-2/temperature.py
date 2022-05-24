from temperature_scale import TemperatureScale
from __future__ import annotations

class Temperature():
    """
        Represents the class for the instatiation of temperatures.
    """

    Scale = None
    Value = None

    def __init__(self, value: float, scale: TemperatureScale):
        """
            Instantiates a new temperature.
        """

        self.Scale = scale
        self.Value = value
        pass

    def Add(self, other: Temperature) -> Temperature:
        """
            Adds the current temperature with another temperature.
        """
        
        primary_scale = self.Scale
        other = other.ConvertToTarget(primary_scale)
        result = round(self.Value, other.Value, 2)
        return Temperature(result, primary_scale)

    def Substract(self, other: Temperature) -> Temperature:
        """
            Substracts the current temperature with another temperature.
        """

        primary_scale = self.Scale
        other = other.ConvertToTarget(primary_scale)
        result = round(self.Value - other.Value, 2)
        return Temperature(result, primary_scale)

    def MultiplyBy(self, other: Temperature) -> Temperature:
        """
            Multiplies the current temperature with another temperature.
        """

        primary_scale = self.Scale
        other = other.ConvertToTarget(primary_scale)
        result = round(self.Value * other.Value, 2)
        return Temperature(result, primary_scale)

    def DivideBy(self, other: Temperature) -> Temperature:
        """
            Divides the current temperature with another temperature.
        """

        primary_scale = self.Scale
        other = other.ConvertToTarget(primary_scale)
        result = round(self.Value / other.Value, 2)
        return Temperature(result, primary_scale)
        

    def ToFarenheit(self) -> Temperature:
        """
            Converts the current temperature to the farenheit scale.
        """

        result = None
        scale = TemperatureScale.Farenheit
        if (self.Scale.name == TemperatureScale.Celcius.name):
            result = round((self.Value * 1.8) + 32, 2)
            pass
        
        elif (self.Scale.name == TemperatureScale.Kelvin.name):
            result = round((self.Value * 1.8) - 459.67, 2)
            pass

        return Temperature(result, scale)

    def ToCelcius(self) -> Temperature:
        """
            Converts the current temperature to the celcius scale.
        """

        result = None
        scale = TemperatureScale.Celcius
        if (self.Scale.name == TemperatureScale.Kelvin.name):
            result = round(self.value - 273.15, 2)
            pass

        elif (self.Scale.name == TemperatureScale.Farenheit.name):
            result = round((self.Value - 32) / 1.8, 2)
            pass

        return Temperature(result, scale)

    def ToKelvin(self) -> Temperature:
        """
            Converts the current temperature to the kelvin scale.
        """

        result = None
        scale = TemperatureScale.Kelvin
        if (self.Scale.name == TemperatureScale.Celcius.name):
            result = round(self.Value + 273.15, 2)
            pass

        elif (self.Scale.name == TemperatureScale.Farenheit.name):
            result = round(((self.Value - 32) / 1.8) + 273.15, 2)
            pass

        return Temperature(result, scale)

    def ToString(self) -> str:
        """
            Converts the current temperature to a string representation.
        """

        scale_char = self.Scale.name.capitalize()[0]
        str_equivalent = f"{self.Value}{scale_char}"
        return str_equivalent        

    def ConvertToTarget(self, target_scale: TemperatureScale) -> Temperature:
        """
            Given a scale, converts the current temperature to the specified scale.
            This is used as the conversion wrapper.
        """

        if (self.Scale.name == target_scale.name):
            return self

        conversion = None
        if (target_scale.name == TemperatureScale.Kelvin.name):
            conversion = self.ToKelvin()
            pass

        elif (target_scale.name == TemperatureScale.Farenheit.name):
            conversion = self.ToFarenheit()
            pass

        elif (target_scale.name == TemperatureScale.Celcius.name):
            conversion = self.ToCelcius()
            pass

        else:
            raise Exception("Invalid temperature scale.") # Exception

        return conversion