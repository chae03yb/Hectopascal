import nextcord
from nextcord.ext import commands

class ModuleManager(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.command(name="load-module")
    async def load_module(self, ctx: commands.Context, module: str) -> None:
        try:
            self.client.load_extension(module)
            await ctx.message.add_reaction("👍")
        except commands.errors.ExtensionAlreadyLoaded:
            await ctx.send("Extension already loaded.")
        except commands.errors.ExtensionNotFound:
            await ctx.send("Extension not found.")
    
    @commands.command(name="unload-module")
    async def unload_module(self, ctx: commands.Context, module: str) -> None:
        if module == "ModuleManager":
            await ctx.send("Can't unload this module")
            return
            
        try:
            self.client.unload_extension(module)
            await ctx.message.add_reaction("👍")
        except commands.errors.ExtensionNotLoaded:
            await ctx.send("Extension not loaded.")
        except commands.errors.ExtensionNotFound:
            await ctx.send("Extension not found.")

    @commands.command(name="reload-module")
    async def reload_module(self, ctx: commands.Context, module: str) -> None:
        if module == "ModuleManager":
            await ctx.send("Can't reload this module")
            return
            
        try:
            self.client.reload_extension(module)
            await ctx.message.add_reaction("👍")
        except commands.errors.ExtensionNotLoaded:
            await ctx.send("Extension not loaded.")
        except commands.errors.ExtensionNotFound:
            await ctx.send("Extension not found.")

def setup(client: commands.Bot):
    client.add_cog(ModuleManager(client))