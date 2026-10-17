from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name:str='Autonomous Software Engineer'; environment:str='development'; log_level:str='INFO'; api_prefix:str='/api/v1'
    database_url:str='postgresql+asyncpg://ase:ase@localhost:5432/ase'; redis_url:str='redis://localhost:6379/0'
    secret_key:str='development-secret'; cors_origins:str='http://localhost:5173'; max_agent_steps:int=50; default_command_timeout_seconds:int=120
    model_config=SettingsConfigDict(env_file='.env',extra='ignore')
    @property
    def cors_origin_list(self): return [x.strip() for x in self.cors_origins.split(',') if x.strip()]
@lru_cache
def get_settings(): return Settings()
