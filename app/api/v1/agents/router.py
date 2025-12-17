"""
Agents Router Module
Handles all agent and tool processing endpoints.
"""
from fastapi import APIRouter, HTTPException
from agents import Agent

from app.schemas import AgentRequest, AgentResponse
from app.services.agent_executor import AgentExecutor, AgentExecutionError
from .registry import get_agent_or_tool, get_all_slugs, get_all_agent_slugs, get_all_tool_slugs

router = APIRouter()


@router.get("/list")
async def list_all_tools():
    """List all available tools (agents + deterministic tools)."""
    return {
        "agents": get_all_agent_slugs(),
        "tools": get_all_tool_slugs(),
        "all": get_all_slugs()
    }


@router.get("/agents")
async def list_agents():
    """List all AI agent slugs."""
    return get_all_agent_slugs()


@router.get("/tools")
async def list_tools():
    """List all deterministic tool slugs."""
    return get_all_tool_slugs()


@router.post("/process/{slug}", response_model=AgentResponse)
async def process_tool(slug: str, request: AgentRequest):
    """
    Process a request using the specified agent or tool.
    
    Args:
        slug: The tool/agent identifier
        request: The input request containing prompt and optional settings
        
    Returns:
        AgentResponse with the result
    """
    handler = get_agent_or_tool(slug)
    
    if not handler:
        raise HTTPException(
            status_code=404, 
            detail=f"Tool '{slug}' not found. Use /api/v1/agents/list to see available tools."
        )
    
    try:
        # AI Agent execution
        if isinstance(handler, Agent):
            return await AgentExecutor.execute(
                agent=handler,
                prompt=request.prompt,
                settings=request.settings,
                user_context=request.user_context
            )
        
        # Deterministic tool execution
        elif callable(handler):
            result = handler(request.prompt)
            return AgentResponse(
                status="success",
                content=str(result)
            )
        
        raise HTTPException(status_code=500, detail="Invalid tool configuration")
        
    except AgentExecutionError as e:
        raise HTTPException(status_code=500, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution error: {str(e)}")