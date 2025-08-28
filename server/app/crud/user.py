from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.core.security import get_password_hash, verify_password

async def get_user_by_username(db: AsyncSession, username: str):
    q = await db.execute(select(User).where(User.username == username))
    return q.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    q = await db.execute(select(User).where(User.email == email))
    return q.scalars().first()

async def create_user(db: AsyncSession, username: str, email: str, password: str):
    hashed = get_password_hash(password)
    user = User(username=username, email=email, hashed_password=hashed)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def authenticate_user(db: AsyncSession, username_or_email: str, password: str):
    # allow username or email for login
    if "@" in username_or_email:
        user = await get_user_by_email(db, username_or_email)
    else:
        user = await get_user_by_username(db, username_or_email)

    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
