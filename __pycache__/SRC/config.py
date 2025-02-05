from pydantic import BaseSettings


class Settings(BaseSettings):
    path: int
    database_username:str
    database_password:str
    database_port: str
    database_name: str
    secret_key:str
    algorithm:str
    access_token_expire_minutes: str

    class Config:
        env_file = ".env"


settings = Settings()