from datetime import datetime,timezone
from enum import Enum
from uuid import UUID,uuid4
from pydantic import BaseModel,Field
class TaskStatus(str,Enum):
    CREATED='created'; EXPLORING='exploring'; PLANNING='planning'; CODING='coding'; TESTING='testing'; REVIEWING='reviewing'; PR_READY='pr_ready'; FAILED='failed'; BLOCKED='blocked'; CANCELLED='cancelled'
class TaskCreate(BaseModel):
    title:str=Field(min_length=1,max_length=200); issue:str=Field(min_length=1); repository_url:str|None=None
class Task(BaseModel):
    id:UUID=Field(default_factory=uuid4); title:str; issue:str; repository_url:str|None=None; status:TaskStatus=TaskStatus.CREATED
    created_at:datetime=Field(default_factory=lambda:datetime.now(timezone.utc)); updated_at:datetime=Field(default_factory=lambda:datetime.now(timezone.utc))
class TaskEvent(BaseModel):
    task_id:UUID; event_type:str; message:str; timestamp:datetime=Field(default_factory=lambda:datetime.now(timezone.utc))
