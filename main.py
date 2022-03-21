from fastapi import FastAPI

import src
from src.models import book_models
from src.routes.book_routes import router
from src.database.db import engine

src.models.book_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix="/book", tags=["book"])

