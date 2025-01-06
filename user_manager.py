from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from fastapi import HTTPException, status

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None

class User(UserBase):
    id: int
    created_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True  # For Pydantic v2 (use orm_mode = True for Pydantic v1)

class UserManager:
    def __init__(self):
        # Initialize with some static users
        self.users: List[User] = [
            User(id=1, username="john_doe", email="john@example.com", 
                 created_at=datetime(2024, 1, 1)),
            User(id=2, username="jane_smith", email="jane@example.com",
                 created_at=datetime(2024, 1, 2)),
            User(id=3, username="bob_wilson", email="bob@example.com",
                 created_at=datetime(2024, 1, 3))
        ]
        self._next_id = len(self.users) + 1

    def create_user(self, user: UserCreate) -> User:
        """Create a new user and add it to the users list."""
        new_user = User(
            id=self._next_id,
            username=user.username,
            email=user.email,
            created_at=datetime.now()
        )
        self.users.append(new_user)
        self._next_id += 1
        return new_user

    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID."""
        user = next((user for user in self.users if user.id == user_id), None)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return user

    def get_all_users(self) -> List[User]:
        """Retrieve all users."""
        return self.users

    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        """Update a user's information."""
        user = self.get_user(user_id)
        user_data = user_update.model_dump(exclude_unset=True)
        
        for field, value in user_data.items():
            setattr(user, field, value)
        
        return user

    def delete_user(self, user_id: int) -> bool:
        """Delete a user by their ID."""
        user = self.get_user(user_id)
        self.users.remove(user)
        return True

    def deactivate_user(self, user_id: int) -> User:
        """Deactivate a user's account."""
        user = self.get_user(user_id)
        user.is_active = False
        return user 