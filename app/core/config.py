# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str  # add this line for Render to pick up
    
    class Config:
        env_file = ".env"

settings = Settings() 
