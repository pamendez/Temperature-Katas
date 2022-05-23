from __future__ import annotations
from temperaturescale import TemperatureScale

class Temperature():
    """
        Represents the temperature class used in the API.
    """

    Value = None
    Scale = None

    def __init__(self, value: float, scale: TemperatureScale) -> None:
        """
            Constructs an instance of the Temperature API class.
        """

        self.Value = value
        self.Scale = scale
        pass

    def Sum(self, other: Temperature) -> Temperature:
        """
            Sums the current temperature with another temperature.
        """

        result = None
        if (self.AreScalesEqual == True):
            result = self.Value + other.Value
            pass

        else:
            other_copy = getattr(other, f"To{self.Scale.name}")()
            result = self.Value + other_copy.Value
        
        return Temperature(result, self.Scale)


    def Substract(self, other: Temperature) -> Temperature:
        """
            Substracts the current temperature with another temperature.
        """

        result = None
        if (self.AreScalesEqual == True):
            result = self.Value - other.Value
            pass

        else:
            other_copy = getattr(other, f"To{self.Scale.name}")()
            result = self.Value - other_copy.Value

        return Temperature(result, self.Scale)
    
    def MultiplyBy(self, other: Temperature) -> Temperature:
        """
            Multiplies the current temperature by another temperature.
        """

        result = None
        if (self.AreScalesEqual == True):
            result = self.Value * other.Value
            pass

        else:
            other_copy = getattr(other, f"To{self.Scale.name}")()
            result = self.Value * other_copy.Value

        return Temperature(result, self.Scale)
    
    def DivideBy(self, other: Temperature) -> Temperature:
        """
            Divides the current temperature with another temperature.
        """

        result = None
        if (self.AreScalesEqual == True):
            result = self.Value / other.Value
            pass

        else:
            other_copy = getattr(other, f"To{self.Scale.name}")()
            result = self.Value / other_copy.Value

        return Temperature(result, self.Scale)

    def ToFarenheit(self) -> Temperature:
        """
            Converts a current temperature to the Farenheit scale.
        """

        result = self.Value
        if (self.Scale.name == TemperatureScale.Celcius.name):
            result = round((self.Value * 9/5) + 32, 2)

        elif (self.Scale.name == TemperatureScale.Kelvin.name):
            result = round(self.Value * 1.8 - 459.67, 2)
        
        return Temperature(result, TemperatureScale.Farenheit)

    def ToCelcius(self) -> Temperature:
        """
            Converts a current temperature to the celcius scale.
        """

        result = self.Value
        if (self.Scale.name == TemperatureScale.Farenheit.name):
            result = round((self.Value - 32) * 5/9, 2)

        elif (self.Scale.name == TemperatureScale.Kelvin.name):
            result = round(self.Value - 273.15, 2)

        return Temperature(result, TemperatureScale.Celcius)

    def ToKelvin(self) -> Temperature:
        """
            Converts a current temperature to the kelvin scale.
        """

        result = self.Value
        if (self.Scale.name == TemperatureScale.Celcius.name):
            result = round(self.Value + 273.15, 2)

        elif (self.Scale.name == TemperatureScale.Farenheit.name):
            result = round((self.Value + 459.67) * 5/9, 2)
        
        return Temperature(result, TemperatureScale.Celcius)

    def ToString(self) -> str:
        """
            Converts the temperature into a readable string format. 
        """

        return f"{self.Value}{self.Scale.name[0]}"

    def AreScalesEqual(self, other: Temperature) -> bool:
        """
            Compares the scales of the current temperature and another temperature.
        """

        return self.Scale == other.Scale