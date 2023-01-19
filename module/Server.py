import nextcord
from nextcord.ext import commands

from xml.etree import ElementTree

class Server(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client

    def _read_save_data(self, *, save_location: str) -> None:
        root = ElementTree.parse(f"{save_location}/working_server/scene.xml").getroot()

def setup(client: commands.Bot):
    client.add_cog(Server(client))