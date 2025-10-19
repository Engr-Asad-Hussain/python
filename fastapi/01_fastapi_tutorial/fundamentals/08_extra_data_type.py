from uuid import UUID

from fastapi import FastAPI

app = FastAPI()


# Other additional data types you can use:
# UUID, datetime, date, time, bytes etc
@app.get(path="/api/store/{store_id}")
async def specific_store(store_id: UUID):
    return {"message": "Following is the store", "storeId": store_id}


# Reference: https://fastapi.tiangolo.com/tutorial/extra-data-types/
