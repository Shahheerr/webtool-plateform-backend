"""
API v1 Router
Combines all agent routers into a single API v1 router.
"""
from fastapi import APIRouter

from .agents import agents_router

router = APIRouter(prefix="/api/v1")

# Include all agent endpoints
router.include_router(agents_router, prefix="/agents", tags=["Agents"])
