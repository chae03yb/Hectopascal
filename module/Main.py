import nextcord
from nextcord.ext import commands

import os

intents = nextcord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.webhooks = True

bot = commands.Bot(
    command_prefix=".", 
    intents=intents, 
    default_guild_ids=[ 
        697820304805724281,
        871059109326229564
    ]
)

class Main(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("bot ready")

    @nextcord.slash_command(name="test")
    async def test_command(self, interaction: nextcord.Interaction) -> None:
        await interaction.response.send_message("slash command test")

def setup(client: commands.Bot) -> None:
    client.add_cog(Main(bot))

if __name__ == "__main__":
    with open("./data/token", "r") as token:
        for file in os.listdir("./module"):
            if not file.endswith(".py"):
                continue
            bot.load_extension(file[:-3])
            print(f"loaded module: {file[:-3]}")
        bot.run(token.read())
