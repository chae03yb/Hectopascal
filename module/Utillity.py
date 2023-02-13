import nextcord
from nextcord.ext import commands

from typing import Optional

class Utillity(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client: commands.Bot = client

    def _calculate_fuel(self, small: int = 0, medium: int = 0, large: int = 0) -> float:
        return small*31.25 + medium*187.5 + large*703.125

    @nextcord.slash_command(name="calculate_fuel")
    async def calculate_fuel(
        self, 
        interaction: nextcord.Interaction, 
        type_small: Optional[int] = nextcord.SlashOption(
            name="type-small", 
            description="number of fuel tank small",
            required=False,
            min_value=0,
            default=0
        ), 
        type_medium: Optional[int] = nextcord.SlashOption(
            name="type-medium", 
            description="number of fuel tank medium",
            required=False,
            min_value=0,
            default=0
        ), 
        type_large: Optional[int] = nextcord.SlashOption(
            name="type-large", 
            description="number of fuel tank large",
            required=False,
            min_value=0,
            default=0
        )
    ) -> None:
        await interaction.response.send_message(
            f"fuel capacity: {self._calculate_fuel(type_small, type_medium, type_large)}"
        )

def setup(client: commands.Bot) -> None:
    client.add_cog(Utillity(client))