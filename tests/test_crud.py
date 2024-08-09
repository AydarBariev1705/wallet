import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(
            app=app,
            base_url="http://127.0.0.1:8000"
    ) as client:
        response = await client.post(
            "/users/",
            json={
                "_id": "5eb7cf5a86d9755df3a6c993",
                "user_id": 999,
                "name": "test",
                "email": "test@test.com",
            },
        )
        assert response.status_code == 200
        assert response.json() == {
                "_id": "5eb7cf5a86d9755df3a6c993",
                "user_id": 999,
                "name": "test",
                "email": "test@test.com",
            }
