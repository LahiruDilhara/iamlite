from dataclasses import dataclass
from pathlib import Path
from app.log import logger
import os
from abc import ABC as abstract, abstractmethod

class Config:
    @abstractmethod
    def load(self)->None:
        pass

    @abstractmethod
    def validate(self)->None:
        pass

class DBConfig(Config):
    POSTGRES_DB_HOST:str
    POSTGRES_DB_PORT:int
    POSTGRES_DB_NAME:str
    POSTGRES_DB_USER:str
    POSTGRES_DB_PASSWORD:str

    def load(self)->None:
        self.POSTGRES_DB_HOST = os.getenv("POSTGRES_DB_HOST",None)
        postgressPortStr = os.getenv("POSTGRES_DB_PORT",None)
        try:
            self.POSTGRES_DB_PORT = int(postgressPortStr) if postgressPortStr is not None else None
        except ValueError:
            logger.error("POSTGRES_DB_PORT must be an integer.")
            self.POSTGRES_DB_PORT = None
        self.POSTGRES_DB_NAME =  os.getenv("POSTGRES_DB_NAME",None)
        self.POSTGRES_DB_USER = os.getenv("POSTGRES_DB_USER",None)
        self.POSTGRES_DB_PASSWORD = os.getenv("POSTGRES_DB_PASSWORD",None)

    def validate(self)->None:
        valide =  all([
            self.POSTGRES_DB_HOST is not None,
            self.POSTGRES_DB_PORT is not None,
            self.POSTGRES_DB_NAME is not None,
            self.POSTGRES_DB_USER is not None,
            self.POSTGRES_DB_PASSWORD is not None
        ])
        if not valide:
            logger.error("One or more database configuration values are missing or invalid.")
            raise Exception("One or more database configuration values are missing or invalid.")

class APPConfig(Config):
    APP_TITLE:str

    def load(self)->None:
        self.APP_TITLE = os.getenv("APP_TITLE",None)

    def validate(self)->None:
        if self.APP_TITLE is None:
            logger.error("APP_TITLE is missing in the configuration.")
            raise Exception("APP_TITLE is missing in the configuration.")

class Configuration:
    _instance = None
    _db_config: DBConfig = None
    _app_config: APPConfig = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._db_config is None:
            self._db_config = DBConfig()
            self._db_config.load()
            self._db_config.validate()

        if self._app_config is None:
            self._app_config = APPConfig()
            self._app_config.load()
            self._app_config.validate()
    
    def get_db_config(self)->DBConfig:
        return self._db_config

    def get_app_config(self)->APPConfig:
        return self._app_config