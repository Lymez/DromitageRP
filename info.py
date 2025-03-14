import a2s

server_address = ("147.185.221.16", 16261)

try:
    server_info = a2s.info(server_address)
    print("Server Name:", server_info.server_name)
    print("Players:", f"{server_info.player_count}/{server_info.max_players}")
    print("Map:", server_info.map_name)
except Exception as e:
    print("Error retrieving server info:", e)