# Project description
A multi-currency wallet system
The system support USD and EUR wallets, CRUD operations, currency conversion, and transaction tracking.

## In project used:
* **Python** (3.12);
* **FastApi** (Asynchronous Web Framework);
* **MongoDB** (Database);
* **beanie** (ODM);
* **Pydantic** (Data verification);
* **Pytest** (Tests);


## Building and running the application
1. Rename .env.template file to .env
2. Fill out the .env file
3. Run command:
    ```
    uvicorn app.main:app --reload
    ```
   
## Documentation
    ```
    localhost:8000/docs/
    ```