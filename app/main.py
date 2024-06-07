from fastapi import FastAPI

app = FastAPI()

@app.get("/healthy")
async def health_check():
    return "healthy", 200

