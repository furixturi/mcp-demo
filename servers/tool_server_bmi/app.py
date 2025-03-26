import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Minimal MCP Server", host="0.0.0.0", port=3000)


@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m**2)


# @mcp.tool()
# async def fetch_weather(city: str) -> str:
#     """Fetch current weather for a city"""
#     async with httpx.AsyncClient() as client:
#         response = await client.get(f"https://api.weather.com/{city}")
#         return response.text


if __name__ == "__main__":
    # Start the server
    mcp.run(transport="stdio")
    # mcp.run(transport="sse")
