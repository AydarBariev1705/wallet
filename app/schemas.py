from typing import Optional

from pydantic import BaseModel


class UserUpdate(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    user_id: Optional[str]
    name: Optional[str]
    email: Optional[str]


class WalletUpdate(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    wallet_id: Optional
    user_id: Optional[str]
    currency: Optional[str]
    balance: Optional[float]


class TransactionUpdate(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    transaction_id: Optional[str]
    wallet_id: Optional[str]
    type: Optional[str]
    amount: Optional[float]
    currency: Optional[str]
