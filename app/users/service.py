from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.users.models import User

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def find_one(self, username: str) -> User:
        """Find a user by username in the database"""
        stmt = select(User).where(User.username == username)
        user = self.db.execute(stmt).scalar_one_or_none()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {username} not found"
            )
        return user

    async def create(self, username: str, password: str) -> User:
        """Create a new user"""
        user = User(username=username, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
