from pydantic import BaseModel


class MongoDBCollections(BaseModel):
    db: str
    collections: str
