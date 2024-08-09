from beanie import Document
from datetime import datetime


class User(Document):
    user_id: int
    name: str
    email: str


class Wallet(Document):
    wallet_id: int
    user_id: int
    currency: str
    balance: float


class Transaction(Document):
    transaction_id: int
    wallet_id: int
    type: str  # 'deposit', 'withdrawal', 'conversion'
    amount: float
    currency: str
    timestamp: datetime
