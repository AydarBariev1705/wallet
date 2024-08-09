from fastapi.encoders import jsonable_encoder


def encode_input(data) -> dict:
    data = jsonable_encoder(data)
    data = {key: value for key, value in data.items() if value is not None}
    return data
