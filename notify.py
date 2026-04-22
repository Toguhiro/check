import json, urllib.request
from mcp.server.fastmcp import FastMCP

PC_NAME = "PC-B"
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1496449676432506991/7x9n5tklK82HOT-4zQR0FOPJIYlj1LPY95t1y7fo8yQ6ONutPCLlkk1CQvUZI8IVAhhx"

mcp = FastMCP("discord-notify")

@mcp.tool()
def notify_discord(message: str) -> str:
    payload = json.dumps({"embeds": [{"title": f"[{PC_NAME}] Claude通知", "description": message, "color": 5763719}]}).encode("utf-8")
    req = urllib.request.Request(WEBHOOK_URL, data=payload, headers={"Content-Type": "application/json", "User-Agent": "DiscordBot (https://example.com, 1.0)"})
    with urllib.request.urlopen(req) as r:
        return f"送信完了 (HTTP {r.status})"

if __name__ == "__main__":
    mcp.run(transport="stdio")
