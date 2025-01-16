from pydantic_settings import BaseSettings  

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:123@localhost:5432/meetme" 
    SECRET_KEY: str = "mysecretkey"  
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


    class Config:
        env_file = ".env"  

settings = Settings()
