from datetime import datetime,timezone
from uuid import UUID
from app.models.task import Task,TaskCreate,TaskStatus,TaskEvent
class TaskService:
    def __init__(self): self._tasks={}; self._events={}
    def create(self,payload):
        t=Task(title=payload.title,issue=payload.issue,repository_url=payload.repository_url); self._tasks[t.id]=t; self._events[t.id]=[TaskEvent(task_id=t.id,event_type='task.created',message='Task created')]; return t
    def get(self,task_id): return self._tasks.get(task_id)
    def list(self): return list(self._tasks.values())
    def transition(self,task_id,status,message):
        t=self._tasks.get(task_id)
        if not t:return None
        t.status=status;t.updated_at=datetime.now(timezone.utc);self._events[task_id].append(TaskEvent(task_id=task_id,event_type=f'task.{status.value}',message=message));return t
    def events(self,task_id): return self._events.get(task_id,[])
