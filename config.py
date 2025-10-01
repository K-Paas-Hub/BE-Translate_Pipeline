import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # 서버 설정
    port: int = 8000
    host: str = "0.0.0.0"
    
    # 환경 설정
    environment: str = "development"
    debug: bool = True
    
    # API 키 설정
    translate_api_key: Optional[str] = None
    google_translate_api_key: Optional[str] = None
    
    # 데이터베이스 설정
    database_url: Optional[str] = None
    postgres_url: Optional[str] = None
    
    # 로깅 설정
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# 전역 설정 인스턴스
settings = Settings()
