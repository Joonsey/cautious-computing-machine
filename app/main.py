from fastapi import FastAPI

from app.routes import apis

app = FastAPI()
app.include_router(apis)

@app.get("/healthy")
async def health_check():
    return "healthy", 200
