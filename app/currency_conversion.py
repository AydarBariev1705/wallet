import aiohttp

from app.config import CONVERSION_API_URL


async def get_conversion_rate(base_currency: str, target_currency: str) -> float:
    async with aiohttp.ClientSession() as session:
        async with session.get(CONVERSION_API_URL) as response:
            data = await response.json()
            rates = data['rates']
            if base_currency == 'USD':
                return rates[target_currency]
            elif base_currency == 'EUR' and target_currency == 'USD':
                return 1 / rates['USD']
            else:
                raise ValueError("Unsupported currency conversion")


def apply_commission(amount: float) -> float:
    return amount * 0.97  # 3%
