from mcp.server.mcpserver import MCPServer
from Tools.weather import get_weather


mcp=MCPServer("weather_bot")


@mcp.tool()
async def get_current_weather(location: str) -> str:
    """
    Asynchronously checks the weather for a given location.

    Args:
        location (str): The location for which to check the weather.
    """
    return get_weather(location)



if __name__ == "__main__":
    mcp.run(transport="stdio")
    
   