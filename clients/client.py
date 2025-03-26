from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",
    args=["server.py"],
    env=None,
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()

            # List awailable resources
            resouces = await session.list_resources()

            # List available tools
            tools = await session.list_tools()
            print("Available tools:", tools)
            # Call a tool
            result = await session.call_tool(
                name="calculate_bmi", arguments={"weight_kg": 52, "height_m": 1.65}
            )
            print("BMI Result:", result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())