from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.health import router as health_router
from app.api.tasks import router as task_router
from app.core.config import get_settings
settings=get_settings()
app=FastAPI(title=settings.app_name,version='0.1.0',description='Autonomous Software Engineer platform')
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_origin_list,allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.include_router(health_router)
app.include_router(task_router,prefix=settings.api_prefix)
@app.get('/')
async def root(): return {'name':settings.app_name,'status':'running','phase':'1-foundation'}
