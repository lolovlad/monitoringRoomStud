from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str
    server_port: int

    time_sleep: int

    login: str
    password: str


settings = Settings(_env_file="settings.env", _env_file_encoding="utf-8")