from settings import settings
from random import randint
from pydantic import BaseModel


class Data(BaseModel):
    temp: float
    temp_reg: float
    hum: float
    hum_reg: float
    leak: bool
    dust: bool
    gas: bool


class RoomMonitoring:
    def __init__(self, file_name: str):
        self.__file_name: str = file_name
        self.__data: Data = None

    def update(self):
        with open(self.__file_name) as file:
            self.__data = Data.model_validate_json(file.read())

    def get_temp_b(self):
        return self.__data.temp_reg

    def get_humidity_b(self):
        return self.__data.hum_reg

    def get_temp(self):
        temp = self.__data.temp
        temp += randint(0, 3)
        return temp

    def get_humidity(self):
        hum = self.__data.hum
        hum += randint(0, 3)
        return hum

    def get_leak(self):
        leak = self.__data.leak
        return leak

    def get_dust(self):
        dust = self.__data.dust
        return dust

    def get_gas(self):
        gas = self.__data.gas
        return gas