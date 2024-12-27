import requests

# Replace with your server's IP or hostname
SERVER_IP = "play.myminecraftserver.com"

def fetch_server_status():
    url = f"https://api.mcsrvstat.us/2/{SERVER_IP}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def update_readme(status):
    with open("README.md", "w") as readme:
        readme.write("# Minecraft Server Status\n\n")
        if status and status.get("online"):
            readme.write(f"✅ **Server is online!**\n\n")
            readme.write(f"**IP Address**: `{SERVER_IP}`\n\n")
            readme.write(f"**Players Online**: {status['players']['online']}/{status['players']['max']}\n")
        else:
            readme.write("❌ **Server is offline.**\n\n")

def main():
    status = fetch_server_status()
    update_readme(status)

if __name__ == "__main__":
    main()
