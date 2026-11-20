from mcp.server.fastmcp import FastMCP
from Tools.weather import get_weather
from typing import Dict, Any


mcp=FastMCP("weather_bot")


@mcp.tool()
async def check_weather(location: str) -> Dict[str, Any]:
    """
    Asynchronously checks the weather for a given location.

    Args:
        location (str): The location for which to check the weather.
    """
    return get_weather(location)
    
   