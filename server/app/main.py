from fastapi import FastAPI
from app.api.v1 import auth, user
from app.db.session import engine
from app.db.base import Base
from sqlalchemy.ext.asyncio import AsyncEngine

app = FastAPI(title="Knowly")

app.include_router(auth.router)
app.include_router(user.router)

@app.on_event("startup")
async def on_startup():
    # create tables if not using alembic (helpful in dev). For production prefer Alembic migrations.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
