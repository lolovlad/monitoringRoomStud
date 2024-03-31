import clr
from pathlib import Path


class CPUTempWin:
    def __init__(self):
        self.__path_dll = Path('OpenHardwareMonitorLib.dll')
        self.__handle = None
        self.__initialize_open_hardware_monitor()

    def __initialize_open_hardware_monitor(self):
        file = str(self.__path_dll.absolute())
        clr.AddReference(file)

        from OpenHardwareMonitor import Hardware

        handle = Hardware.Computer()
        handle.MainboardEnabled = True
        handle.CPUEnabled = True
        handle.RAMEnabled = False
        handle.GPUEnabled = False
        handle.HDDEnabled = False
        handle.Open()
        self.__handle = handle

    def get_cpu_temp(self):
        for i in self.__handle.Hardware:
            i.Update()
            for sensor in i.Sensors:
                if str(sensor.SensorType) == 'Temperature':
                    return sensor.Value

    def get_cpu_load(self):
        load_sum = 0
        count = 0
        for i in self.__handle.Hardware:
            i.Update()
            for sensor in i.Sensors:
                if str(sensor.SensorType) == 'Load':
                    if sensor.Value > 0:
                        load_sum += sensor.Value
                        count += 1
        return round(load_sum / count, 2)