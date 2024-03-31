import psutil
from .CPUTempWin import CPUTempWin


class ServerMonitoring:
    def __init__(self):
        self.__cpu_temp = CPUTempWin()
        self.__disks = [i.device for i in psutil.disk_partitions()]

    def disk_size(self) -> tuple[int, int]:
        total_size = 0
        free_size = 0
        for i in self.__disks:
            used = psutil.disk_usage(i)
            total_size += used.total
            free_size += used.free

        return total_size, free_size

    def cpu_load(self) -> float:
        return self.__cpu_temp.get_cpu_load()

    def cpu_temp(self) -> float:
        return self.__cpu_temp.get_cpu_temp()
