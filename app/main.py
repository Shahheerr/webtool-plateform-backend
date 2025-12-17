"""
App Main Module - FastAPI Application Factory
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.router import router as api_v1_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    application = FastAPI(
        title="Web Tool Platform API",
        description="AI-powered tools and content generation platform",
        version="2.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # CORS Configuration
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    application.include_router(api_v1_router)
    
    @application.get("/health")
    async def health():
        return {"status": "healthy"}
    
    return application


# Create app instance
app = create_app()