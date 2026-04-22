import json, urllib.request
from mcp.server.fastmcp import FastMCP

PC_NAME = "PC-A"
WEBHOOK_URL = "https://discord.com/api/webhooks/ここにコピーしたURL"

mcp = FastMCP("discord-notify")

@mcp.tool()
def notify_discord(message: str) -> str:
    """タスク完了・エラー時にDiscordへ通知を送る"""
    payload = json.dumps({
        "embeds": [{
            "title": f"🔔 [{PC_NAME}] Claude通知",
            "description": message,
            "color": 5763719
        }]
    }).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as r:
        return f"送信完了 (HTTP {r.status})"

if __name__ == "__main__":
    mcp.run(transport="stdio")