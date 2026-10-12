# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        environments = {"dev", "test", "prod"}
        if value not in environments:
            raise ValueError("Wrong environment name")
        else:
            return value
