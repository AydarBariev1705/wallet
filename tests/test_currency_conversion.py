import pytest
from app.currency_conversion import get_conversion_rate, apply_commission


@pytest.mark.asyncio
async def test_conversion_rate():
    rate = await get_conversion_rate("USD", "EUR")
    assert rate > 0


def test_apply_commission():
    assert apply_commission(100) == 97.0
