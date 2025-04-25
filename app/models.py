### app/models.py
from sqlmodel import SQLModel, Field, Session, create_engine, select
import os

DB_PATH = os.path.join("db", "time_manager.db")
engine = create_engine(f"sqlite:///{DB_PATH}")

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    duration: int  # total time in days
    days_passed: int

SQLModel.metadata.create_all(engine)

def create_task(name: str, duration: int, days_passed: int):
    with Session(engine) as session:
        task = Task(name=name, duration=duration, days_passed=days_passed)
        session.add(task)
        session.commit()

def get_all_tasks():
    with Session(engine) as session:
        return session.exec(select(Task)).all()