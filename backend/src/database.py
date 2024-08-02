from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    "sqlite+aiosqlite:///users.db"
    )
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass


class UsersOrm(Model):
    """Users models"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key = True)
    login: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)