from fastapi import FastAPI, status
from user_manager import UserManager, User, UserCreate, UserUpdate

app = FastAPI(title="User Management API")
user_manager = UserManager()

@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return user_manager.create_user(user)

@app.get("/users/", response_model=list[User])
async def read_users():
    return user_manager.get_all_users()

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    return user_manager.get_user(user_id)

@app.patch("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate):
    return user_manager.update_user(user_id, user_update)

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    user_manager.delete_user(user_id)

@app.post("/users/{user_id}/deactivate", response_model=User)
async def deactivate_user(user_id: int):
    return user_manager.deactivate_user(user_id) 