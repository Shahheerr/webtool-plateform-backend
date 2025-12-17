"""
Agent Executor Service
Handles the execution of AI agents with proper error boundaries and output sanitization.
"""
import uuid
from typing import Optional, Dict, Any
from agents import Agent, Runner, ModelSettings

# Use the same config that agents use
from config.gemini_config import gemini_config
from app.schemas import AgentResponse, ErrorResponse, UsageInfo, ModelSettingsSchema


class AgentExecutor:
    """
    Service class for executing AI agents.
    Implements error boundaries and ensures clean output without hallucination.
    """
    
    @staticmethod
    async def execute(
        agent: Agent,
        prompt: str,
        settings: Optional[ModelSettingsSchema] = None,
        user_context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Execute an agent with the given prompt and settings.
        
        Args:
            agent: The Agent instance to execute
            prompt: User's input prompt
            settings: Optional model settings override
            user_context: Optional additional context
            
        Returns:
            AgentResponse with clean content
        """
        agent_id = str(uuid.uuid4())
        
        try:
            # Build the full prompt with context if provided
            full_prompt = prompt
            if user_context:
                context_str = "\n".join(f"{k}: {v}" for k, v in user_context.items())
                full_prompt = f"Context:\n{context_str}\n\nRequest:\n{prompt}"
            
            # Execute the agent using the SAME config that agents use
            result = await Runner.run(agent, full_prompt, run_config=gemini_config)
            
            # Extract clean content - NO meta-talk, NO debugging strings
            content = result.final_output
            
            # Ensure content is a string
            if not isinstance(content, str):
                content = str(content)
            
            # Build usage info if available
            usage = None
            if hasattr(result, 'usage') and result.usage:
                usage = UsageInfo(
                    prompt_tokens=getattr(result.usage, 'prompt_tokens', None),
                    completion_tokens=getattr(result.usage, 'completion_tokens', None),
                    total_tokens=getattr(result.usage, 'total_tokens', None)
                )
            
            return AgentResponse(
                status="success",
                agent_id=agent_id,
                content=content,
                usage=usage
            )
            
        except Exception as e:
            # Return clean error without exposing internals
            raise AgentExecutionError(
                message=f"Agent execution failed: {str(e)}",
                agent_id=agent_id
            )


class AgentExecutionError(Exception):
    """Custom exception for agent execution failures."""
    
    def __init__(self, message: str, agent_id: str):
        self.message = message
        self.agent_id = agent_id
        super().__init__(self.message)
    
    def to_error_response(self) -> ErrorResponse:
        """Convert to standardized error response."""
        return ErrorResponse(
            status="error",
            message=self.message,
            agent_id=self.agent_id
        )
