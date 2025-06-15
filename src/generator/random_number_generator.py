"""Random number generator class.
It is used for generating random numbers based on hourly weather forecasting data.
"""

import json

import requests


class TrueRandomGenerator:
    CONST_CITY_COORDINATE = (42.5255, -71.7642)
    CONST_A = 8191
    CONST_C = 524287
    CONST_M = 6700417
    CONST_MIN_VAL = 0
    CONST_MAX_VAL = 6700417

    def __init__(self, coordinate=None):
        if coordinate:
            self._seed_coordinate = coordinate
        else:
            self._seed_coordinate = self.CONST_CITY_COORDINATE
        self.seed = 0

    def _get_forecast_url(self, coordinate) -> str:
        """Create dto backend instance.

        Args:
            coordinate: The coordinate of the city for which the weather forecast is drawn from.
        """
        try:
            url = f"https://api.weather.gov/points/{coordinate[0]},{coordinate[1]}"
            response = requests.get(url)
            response.raise_for_status()
            parsed_context = json.loads(response.content)
            return parsed_context["properties"]["forecastHourly"]
        except requests.exceptions.HTTPError as err:
            print(err.response.text)

    def _get_random_seed(self):
        """Create and store the random seed."""
        try:
            forecast_url = self._get_forecast_url(self._seed_coordinate)
            response = requests.get(forecast_url)
            response.raise_for_status()

            parsed_context = json.loads(response.content)
            all_forecasts = parsed_context["properties"]["periods"]
            temp_list = [forecast["temperature"] for forecast in all_forecasts]
            self.seed = sum(temp_list) // len(temp_list)
            return
        except requests.exceptions.HTTPError as err:
            print(err.response.text)

    def random(self):
        """Generate a random number between 0 and 1"""
        if self.seed == 0:
            self._get_random_seed()
        random_number = (self.CONST_A * self.seed + self.CONST_C) % self.CONST_M
        self.seed = random_number
        return random_number / self.CONST_MAX_VAL
