import discord
from discord.ext import commands

TOKEN = "" # Your discord bot token, never leak/share your bot token. You may protect it more secure in a .env file or similar that does not get pushed to github or similar

intents = discord.Intents.default() # Activates default Discord Intents

bot = commands.Bot(command_prefix="!", intents=intents) # Creates the default Bot with Command Prefix

@bot.event
async def on_ready():
    print(f'{bot.user} is ready!')

bot.run(TOKEN)