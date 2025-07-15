from fastmcp import Client
import weather_server  # Ensure it has a running MCP server and registered tools
import asyncio

async def main():
    async with Client(weather_server.mcp) as mcp_client:
        tools = await mcp_client.list_tools()
        print(tools)

if __name__ == "__main__":
    asyncio.run(main())