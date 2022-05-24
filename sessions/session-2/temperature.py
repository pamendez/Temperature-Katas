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

        # TODO: Check for scales.
        pass

    def Substract(self, other: Temperature) -> Temperature:
        """
            Substracts the current temperature with another temperature.
        """

        # TODO: Check for scales.
        pass

    def MultiplyBy(self, other: Temperature) -> Temperature:
        """
            Multiplies the current temperature with another temperature.
        """

        # TODO: Check for scales.
        pass

    def DivideBy(self, other: Temperature) -> Temperature:
        """
            Divides the current temperature with another temperature.
        """

        # TODO: Check for scales.
        pass

    def ToFarenheit(self) -> Temperature:
        """
            Converts the current temperature to the farenheit scale.
        """

        # TODO: Search for formula.
        pass

    def ToCelcius(self) -> Temperature:
        """
            Converts the current temperature to the celcius scale.
        """

        # TODO: Search for formula.
        pass

    def ToKelvin() -> Temperature:
        """
            Converts the current temperature to the kelvin scale.
        """

        # TODO: Search for formula.
        pass

    def ToString() -> str:
        """
            Converts the current temperature to a string representation.
        """

        # TODO: Implement this method.
        pass

    def ConvertToTarget() -> Temperature:
        """
            Given a scale, converts the current temperature to the specified scale.
            This is used as the conversion wrapper.
        """

        # TODO: Implement this method.
        pass