from sqlalchemy.orm import Session

class TasksService:
    def __init__(self, db: Session):
        self.db = db
