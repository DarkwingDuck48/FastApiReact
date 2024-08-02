
from sqlalchemy import select
from src.database import new_session
from src.schemas import UserCreate, UserLogin
from src.database import UsersOrm

class UserRepository:
    """User repository"""
    @classmethod
    async def add_user(cls, data: UserCreate):
        """Add user to DB"""
        async with new_session() as session:
            user_dump = data.model_dump()
            user = UsersOrm(**user_dump)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_users(cls):
        """Gets all users"""
        async with new_session() as session:
            query = select(UsersOrm)
            result = await session.execute(query)
            users = result.scalars().all()
            return users

    @classmethod
    async def login_user(cls, data: UserLogin) -> bool:
        """Login user by login and password"""
        async with new_session() as session:
            query = select(UsersOrm).where(UsersOrm.login == data.login).where(UsersOrm.password == data.password)
            result = await session.execute(query)
            user = result.scalars().first()
            return user is not None
