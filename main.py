"""
Web Tool Platform Backend - Main Entry Point
FastAPI application with unified agent/tool processing.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from app.core import settings
from app.api.v1.router import router as api_v1_router

# Initialize FastAPI app
app = FastAPI(
    title="Web Tool Platform API",
    description="AI-powered tools and content generation platform",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_v1_router)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint - API information."""
    return {
        "name": "Web Tool Platform API",
        "version": "2.0.0",
        "status": "running",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handle all unhandled exceptions."""
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal server error",
            "detail": str(exc) if settings.DEBUG else "An error occurred"
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
