from fastapi import FastAPI

app = FastAPI(title="Hazard Alert Bot")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "hazard-alert-bot",
        "version": "1.0.0"
    }