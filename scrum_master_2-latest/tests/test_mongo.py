from app.db import db
import asyncio

async def test():
    # 1. Insert a document
    result = await db.mongo_test.insert_one({
        "source": "test_mongo.py",
        "status": "working",
        "checked": True
    })

    # 2. Read it back
    doc = await db.mongo_test.find_one({"_id": result.inserted_id})

    print("✅ Inserted ID:", result.inserted_id)
    print("✅ Read document:", doc)

asyncio.run(test())
