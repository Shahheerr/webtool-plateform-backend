"""
Test script for agent execution
"""
import asyncio
from app.api.v1.agents import get_agent
from app.services import AgentExecutor
from app.schemas import ModelSettingsSchema


async def test_story_generator():
    print("=" * 50)
    print("Testing Story Generator Agent")
    print("=" * 50)
    
    # Get the agent
    agent = get_agent("story-generator")
    if not agent:
        print("❌ Agent not found!")
        return False
    
    print(f"✅ Agent found: {agent.name}")
    
    # Execute with a simple prompt
    try:
        response = await AgentExecutor.execute(
            agent=agent,
            prompt="Write a very short 2-sentence story about a brave knight",
            settings=None,
            user_context=None
        )
        
        print(f"✅ Status: {response.status}")
        print(f"✅ Agent ID: {response.agent_id}")
        print(f"✅ Content:\n{response.content}")
        if response.usage:
            print(f"✅ Usage: {response.usage}")
        return True
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_hex_to_rgb():
    print("\n" + "=" * 50)
    print("Testing Hex to RGB Tool")
    print("=" * 50)
    
    from app.api.v1.agents import get_tool
    
    tool = get_tool("hex-to-rgb")
    if not tool:
        print("❌ Tool not found!")
        return False
    
    print("✅ Tool found")
    
    # Test cases
    test_cases = [
        ("#FF5733", "rgb(255, 87, 51)"),
        ("000000", "rgb(0, 0, 0)"),
        ("#FFF", "rgb(255, 255, 255)"),
    ]
    
    all_passed = True
    for hex_val, expected_prefix in test_cases:
        result = tool(hex_val)
        if "rgb" in result:
            print(f"✅ {hex_val} -> {result}")
        else:
            print(f"❌ {hex_val} -> {result}")
            all_passed = False
    
    return all_passed


async def test_list_tools():
    print("\n" + "=" * 50)
    print("Testing Tool Registry")
    print("=" * 50)
    
    from app.api.v1.agents import get_all_slugs, get_all_agent_slugs, get_all_tool_slugs
    
    agents = get_all_agent_slugs()
    tools = get_all_tool_slugs()
    all_tools = get_all_slugs()
    
    print(f"✅ Total AI Agents: {len(agents)}")
    print(f"✅ Total Deterministic Tools: {len(tools)}")
    print(f"✅ Total Available: {len(all_tools)}")
    
    print("\nAI Agents:")
    for slug in agents[:5]:
        print(f"  - {slug}")
    print(f"  ... and {len(agents) - 5} more")
    
    print("\nDeterministic Tools:")
    for slug in tools:
        print(f"  - {slug}")
    
    return True


async def run_all_tests():
    print("\n🚀 Starting Backend Tests\n")
    
    results = {
        "Tool Registry": await test_list_tools(),
        "Hex to RGB": await test_hex_to_rgb(),
        "Story Generator": await test_story_generator(),
    }
    
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    print("\n" + ("🎉 All tests passed!" if all_passed else "⚠️ Some tests failed!"))
    return all_passed


if __name__ == "__main__":
    asyncio.run(run_all_tests())
