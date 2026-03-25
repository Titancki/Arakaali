import os

import discord
from discord import app_commands
from discord.ext import commands


class DoeBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self) -> None:
        self.tree.add_command(doe1)
        self.tree.add_command(doe2)


bot = DoeBot()


@app_commands.command(name="doe1", description="Search poewiki.net")
@app_commands.describe(query="Search query")
async def doe1(interaction: discord.Interaction, query: str) -> None:
    await interaction.response.send_message(
        f"doe1 received query: {query}",
        ephemeral=False,
    )


@app_commands.command(name="doe2", description="Search poe2wiki.net")
@app_commands.describe(query="Search query")
async def doe2(interaction: discord.Interaction, query: str) -> None:
    await interaction.response.send_message(
        f"doe2 received query: {query}",
        ephemeral=False,
    )


def main() -> None:
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set")
    bot.run(token)
