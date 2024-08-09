from beanie import init_beanie
from app.config import MONGO_URL
from app.models import User, Wallet, Transaction
from motor.motor_asyncio import AsyncIOMotorClient


async def init_db():
    client = AsyncIOMotorClient(
        MONGO_URL,
    )
    database = client['wallet']

    await init_beanie(
        database,
        document_models=[
            User,
            Wallet,
            Transaction,
        ],
    )
