from httpx import Client
from functools import partial


class ServerRepository:
    def __init__(self, host: str, port: int):
        self.__token = None
        self.__client = partial(Client,
                                base_url=f'http://{host}:{port}/v1')

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

    def get_all_type_point(self) -> list:
        with self.__client() as client:
            response = client.get("/point/type_point/all")
            return response.json()

    def post_point(self, value: str, id_type_point: int, default_value=""):
        point = {
            "value": value,
            "default_value": default_value,
            "id_type_point": id_type_point
        }
        with self.__client() as client:
            response = client.post("point/", json=point, headers={"Authorization": f"Bearer {self.__token}"})
            return response.json()

    def login_pc(self, login: str, password: str):
        user = {"grant_type": "",
                "username": login,
                "password": password,
                "scope": "",
                "client_id": "",
                "client_secret": ""}
        with self.__client() as client:
            response = client.post("/login/sign-in", headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }, data=user)
            return response.json()
