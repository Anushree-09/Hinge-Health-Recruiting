from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.tasks import models as task_models
from app.users import models as user_models

from app.auth.router import router as auth_router
from app.tasks.router import router as tasks_router
from fastapi.responses import HTMLResponse


# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
async def root():
    return HTMLResponse(content="<h1>Hello World</h1>", status_code=200)
