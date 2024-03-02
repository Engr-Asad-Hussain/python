from fastapi import FastAPI
from uuid import UUID

app = FastAPI()


# Other additional data types you can use:
# UUID, datetime, date, time, bytes etc
@app.get(path="/api/store/{store_id}")
async def specific_store(store_id: UUID):
    return {"message": "Following is the store", "storeId": store_id}


# Reference: https://fastapi.tiangolo.com/tutorial/extra-data-types/
