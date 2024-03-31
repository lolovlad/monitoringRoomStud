from RoomMonitoring import RoomMonitoring
from Classes.ServerRepository import ServerRepository
from settings import settings
from time import sleep


repository = ServerRepository(settings.server_host, settings.server_port)

s = RoomMonitoring("main.json")
type_point_list = repository.get_all_type_point()

key_type_point = {}

for type_point in type_point_list:
    key_type_point[type_point["name"]] = type_point["id"]


token = repository.login_pc(settings.login, settings.password)["access_token"]
repository.token = token


while True:
    s.update()

    temp = s.get_temp()
    hum = s.get_humidity()
    leak = s.get_leak()
    dust = s.get_dust()
    gas = s.get_gas()

    print(f"temperature: {temp}, normal {s.get_temp_b()}")
    print(f"humidity: {hum}, normal {s.get_humidity_b()}")
    print(f"leak: {leak}")
    print(f"dust: {dust}")
    print(f"gas: {gas}")

    repository.post_point(str(s.get_temp()), key_type_point["temperature"], str(s.get_temp_b()))
    repository.post_point(str(s.get_humidity()), key_type_point["humidity"], str(s.get_humidity_b()))
    repository.post_point(str(int(s.get_leak())), key_type_point["leak"])
    repository.post_point(str(int(s.get_dust())), key_type_point["dust"])
    repository.post_point(str(int(s.get_gas())), key_type_point["gas"])

    sleep(settings.time_sleep)
