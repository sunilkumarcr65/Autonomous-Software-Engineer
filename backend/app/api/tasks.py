from uuid import UUID
from fastapi import APIRouter,HTTPException
from app.models.task import Task,TaskCreate,TaskEvent,TaskStatus
from app.services.task_service import TaskService
router=APIRouter(prefix='/tasks',tags=['tasks']); service=TaskService()
@router.post('',response_model=Task,status_code=201)
async def create_task(payload:TaskCreate): return service.create(payload)
@router.get('',response_model=list[Task])
async def list_tasks(): return service.list()
@router.get('/{task_id}',response_model=Task)
async def get_task(task_id:UUID):
    t=service.get(task_id)
    if not t: raise HTTPException(404,'Task not found')
    return t
@router.post('/{task_id}/transition/{status}',response_model=Task)
async def transition_task(task_id:UUID,status:TaskStatus):
    t=service.transition(task_id,status,f'Transitioned to {status.value}')
    if not t: raise HTTPException(404,'Task not found')
    return t
@router.get('/{task_id}/events',response_model=list[TaskEvent])
async def task_events(task_id:UUID):
    if not service.get(task_id): raise HTTPException(404,'Task not found')
    return service.events(task_id)
