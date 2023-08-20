import discord
import json

# Load token from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    bot_token = config["token"]

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} - {client.user.id}")

    channel_data = []

    # Fetch all guilds (servers) the bot is a member of
    for guild in client.guilds:
        guild_info = {
            "guild_name": guild.name,
            "guild_id": guild.id,
            "channels": []
        }

        # Fetch all channels in the guild
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                channel_info = {
                    "channel_name": channel.name,
                    "channel_id": channel.id,
                    "messages": []
                }

                async for message in channel.history(limit=None):
                    message_info = {
                        "author": message.author.name,
                        "content": message.content,
                        "timestamp": str(message.created_at)
                    }
                    channel_info["messages"].append(message_info)

                guild_info["channels"].append(channel_info)

        channel_data.append(guild_info)

    with open("dump.json", "w") as dump_file:
        json.dump(channel_data, dump_file, indent=4)

    print("Channel data with messages saved to dump.json")
    await client.close()
    print("Client closed")
    exit(0)

client.run(bot_token)
