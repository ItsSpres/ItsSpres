import requests

# Replace with your server's IP or hostname
SERVER_IP = "play.myminecraftserver.com"

def fetch_server_status():
    url = f"https://api.mcsrvstat.us/2/pms.blockhero.net"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def update_readme(status):
    # Read the current README.md content
    with open("README.md", "r") as readme:
        lines = readme.readlines()
    
    # Identify the section markers
    start_marker = "<!-- MC_SERVER_STATUS_START -->"
    end_marker = "<!-- MC_SERVER_STATUS_END -->"

    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        if end_marker in line:
            end_index = i
    
    if start_index is None or end_index is None:
        print("Section markers not found in README.md")
        return

    # Generate the new status content
    if status and status.get("online"):
        new_content = [
            f"✅ **Server is online!**\n",
            f"**IP Address**: `pms.blockhero.net`\n",
            f"**Players Online**: {status['players']['online']}/{status['players']['max']}\n"
        ]
    else:
        new_content = ["❌ **Server is offline.**\n"]

    # Replace the section between the markers
    updated_lines = (
        lines[: start_index + 1]
        + new_content
        + lines[end_index:]
    )

    # Write the updated content back to README.md
    with open("README.md", "w") as readme:
        readme.writelines(updated_lines)

def main():
    status = fetch_server_status()
    update_readme(status)

if __name__ == "__main__":
    main()
