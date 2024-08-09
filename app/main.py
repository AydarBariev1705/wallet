from beanie import PydanticObjectId
from fastapi import FastAPI, HTTPException
from starlette import status
from typing import List

from app.database import init_db
from app.currency_conversion import get_conversion_rate, apply_commission
from app.models import User, Wallet, Transaction
from app.utils import encode_input
from app.schemas import UserUpdate, WalletUpdate, TransactionUpdate

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.post(
    "/users/",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
)
async def create_user(user: User):
    await user.insert()
    return user


@app.get(
    "/users/",
    response_model=List[User],
)
async def get_users():
    users = await User.find_all().to_list()
    return users


@app.get(
    "/users/{id}",
    response_model=User,
)
async def get_user(user_id: int):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user


@app.put(
    "/users/{user_id}",
    response_model=User,
)
async def update_user(user_id: int, user_data: UserUpdate):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    user_data = encode_input(user_data)
    update = await user.update({"$set": user_data})
    updated_user = await user.get(user_id)
    return updated_user


@app.delete(
    "/user/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(user_id: int):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    await user.delete()
    return {"message": "User deleted successfully"}


@app.post(
    "/wallets/",
    status_code=status.HTTP_201_CREATED,
    response_model=Wallet,
)
async def create_wallet(wallet: Wallet):
    await wallet.insert()
    return wallet


@app.get(
    "/wallets/",
    response_model=List[Wallet],
)
async def get_wallets():
    wallets = await Wallet.find_all().to_list()
    return wallets


@app.get(
    "/wallets/{wallet_id}",
    response_model=Wallet,
)
async def get_wallet(wallet_id: int):
    wallet = await Wallet.get(wallet_id)
    if wallet:
        return wallet
    raise HTTPException(
        status_code=404,
        detail=f"Wallet with id {wallet_id} not found",
    )


@app.put(
    "/wallets/{wallet_id}",
    response_model=Wallet,
)
async def update_wallet(wallet_id: int, wallet_data: WalletUpdate):
    wallet = await Wallet.get(wallet_id)
    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Wallet with id {wallet_id} not found",
        )
    wallet_data = encode_input(wallet_data)
    update = await wallet.update({"$set": wallet_data})
    updated_user = await wallet.get(wallet_id)
    return updated_user


@app.delete(
    "/wallet/{wallet_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_wallet(wallet_id: int):
    wallet = await Wallet.get(wallet_id)
    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Wallet with id {wallet_id} not found",
        )
    await wallet.delete()
    return {"message": "Wallet deleted successfully"}


@app.post(
    "/transactions/",
    status_code=status.HTTP_201_CREATED,
    response_model=Transaction,
)
async def create_transaction(transaction: Transaction):
    await transaction.insert()
    return transaction


@app.get(
    "/transactions/{wallet_id}",
    response_model=List[Transaction],
)
async def get_transactions(wallet_id: int):
    transactions = await Transaction.get(wallet_id)
    return transactions


@app.put(
    "/transactions/{transactions_id}",
    response_model=Transaction,
)
async def update_transaction(transactions_id: int, transaction_data: TransactionUpdate):
    transaction = await Transaction.get(transactions_id)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {transactions_id} not found",
        )
    transaction_data = encode_input(transaction_data)
    update = await transaction.update({"$set": transaction_data})
    updated_transaction = await transaction.get(transactions_id)
    return updated_transaction


@app.delete("/transactions/{transactions_id}",
            status_code=status.HTTP_204_NO_CONTENT,
            )
async def delete_transaction(transactions_id: int):
    transaction = await Transaction.get(transactions_id)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {transactions_id} not found",
        )
    await transaction.delete()
    return {"message": "Transaction deleted successfully"}


@app.post(
    "/convert/",
)
async def convert_currency(amount: float, from_currency: str, to_currency: str):
    rate = await get_conversion_rate(from_currency, to_currency)
    converted_amount = amount * rate
    fee_amount = apply_commission(converted_amount)
    return {"converted_amount": fee_amount}
