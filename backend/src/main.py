from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import create_tables
from src.router import router as users_router

@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    await create_tables()
    yield

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://0.0.0.0:5173"
]


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)
app.include_router(users_router)
