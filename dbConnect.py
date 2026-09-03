from motor.motor_asyncio import AsyncIOMotorClient

# only for conpass
client = AsyncIOMotorClient("mongodb://localhost:27017")
# only for atlas
# client = AsyncIOMotorClient("mongodb+srv://admin:admin@cluster0.7pllq7y.mongodb.net/?appName=Cluster0")

db = client["gube"]
productCollection = db["products"]