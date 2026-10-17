from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health():
    r=client.get('/health'); assert r.status_code==200 and r.json()['status']=='ok'
def test_task_flow():
    r=client.post('/api/v1/tasks',json={'title':'Fix bug','issue':'Login returns 500'}); assert r.status_code==201
    tid=r.json()['id']; r=client.post(f'/api/v1/tasks/{tid}/transition/exploring'); assert r.json()['status']=='exploring'
    r=client.get(f'/api/v1/tasks/{tid}/events'); assert len(r.json())>=2
