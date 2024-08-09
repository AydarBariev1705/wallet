from beanie import Document
from datetime import datetime


class User(Document):
    name: str
    email: str


class Wallet(Document):
    user_id: str
    currency: str
    balance: float


class Transaction(Document):
    wallet_id: str
    type: str  # 'deposit', 'withdrawal', 'conversion'
    amount: float
    currency: str
    timestamp: datetime
