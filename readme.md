# Discord Data Dump

This Python script allows you to extract channel and message data from a Discord server using the `discord.py` library. It fetches the channel structure and messages from each text channel and saves the information in a JSON file.

## Prerequisites

- Python 3.6 or higher
- `discord.py` library (install using `pip install discord.py`)

## Getting Started

1. Clone or download this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Replace `YOUR_BOT_TOKEN` in the `config.json` file by your actual bot token.
4. Run the script using python `dump.py`.

The extracted channel and message data will be saved in `dump.json`.


## Example Files

**config.json**

This file stores your Discord bot token. Replace "YOUR_BOT_TOKEN" with your actual bot token.

```json
{
    "token": "YOUR_BOT_TOKEN"
}
```

**dump.json**

This file contains information about guilds, channels, and messages extracted from the server.

```json
[
    {
        "guild_name": "Example Guild 1",
        "guild_id": "123456789012345678",
        "channels": [
            {
                "channel_name": "general",
                "channel_id": "123456789012345678",
                "messages": [
                    {
                        "author": "User1",
                        "content": "Hello, everyone!",
                        "timestamp": "2023-08-20 12:34:56"
                    },
                    ...
                ]
            },
            ...
        ]
    },
    ...
]
```

## Notes

Be cautious when sharing your bot token or code containing sensitive information.
The script may take a while to run, especially for large servers or channels with many messages.
Consider potential rate limiting issues from the Discord API when fetching large amounts of data.
