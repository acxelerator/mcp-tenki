from pydantic import BaseModel, Field


class Temperature(BaseModel):
    celsius: str | None
    fahrenheit: str | None


class TemperatureRange(BaseModel):
    min: Temperature
    max: Temperature


class WeatherDetail(BaseModel):
    weather: str
    wind: str
    wave: str


class WeatherImage(BaseModel):
    title: str
    url: str
    width: int
    height: int


class ChanceOfRain(BaseModel):
    T00_06: str
    T06_12: str
    T12_18: str
    T18_24: str


class WeatherForecast(BaseModel):
    date: str
    date_label: str = Field(alias="dateLabel")
    telop: str
    detail: WeatherDetail = Field(alias="detail")
    temperature: TemperatureRange
    chance_of_rain: ChanceOfRain = Field(alias="chanceOfRain")

    def format_forecast(self) -> str:
        return f"""
            Daet: {self.date}
            TemperatureMin: {self.temperature.min.celsius}度
            TemperatureMax: {self.temperature.max.celsius}度
            ChanceOfRain(00_06): {self.chance_of_rain.T00_06}
            ChanceOfRain(06_12): {self.chance_of_rain.T06_12}
            ChanceOfRain(12_18): {self.chance_of_rain.T12_18}
            ChanceOfRain(18_24): {self.chance_of_rain.T18_24}
            """
