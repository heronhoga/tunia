import os

import asyncpg
from dotenv import load_dotenv

# initialize env
_ = load_dotenv()

db_name = os.getenv("DATABASE_NAME")
db_host = os.getenv("DATABASE_HOST")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_port = os.getenv("DATABASE_PORT")

pool = None

async def connect_db():
    global pool
    pool = await asyncpg.create_pool(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )

async def get_db():
    if pool is None:
        raise RuntimeError("Database pool has not been initialized")
        
    async with pool.acquire() as conn:
        yield conn
        


