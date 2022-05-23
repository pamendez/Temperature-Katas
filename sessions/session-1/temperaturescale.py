from enum import Enum

class TemperatureScale(Enum):
    """
        Represents the temperature scales, these being:
            - Celcius (C)
            - Farenheit (F)
            - Kelvin (K)
    """

    Celcius = 1,
    Farenheit = 2,
    Kelvin = 3