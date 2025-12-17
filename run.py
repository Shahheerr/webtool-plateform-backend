"""
Run Script for Web Tool Platform Backend
Launch the FastAPI application with uvicorn.
"""
import uvicorn

if __name__ == "__main__":
    # Import settings here to ensure .env is loaded
    from app.core import settings
    
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
