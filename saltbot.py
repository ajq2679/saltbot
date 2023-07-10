import discord
from discord.ext import commands
import os
from discord.member import Member
from dotenv import load_dotenv
# load token from .env
load_dotenv(override=True)
BOT_TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

saltBot = commands.Bot(command_prefix="%")

@saltBot.event
async def on_ready():
    print("WE RUNNIN BOIS! Logged in as")
    print(saltBot.user.name)
    print(saltBot.user.id)

# Nickname command, by default will add "Boi" to the end of nickname
# Check to see if member does not have member role, if not give them member role
@saltBot.command()
async def nickname(ctx, *nickname):
    # error checking
    if not nickname:
        await ctx.channel.send("um what do you want me to change your name to again?")
        return
    # TODO: Implement error checking for permissions and send to channel if perms are insufficient
    # Force everyone to be a Boi
    separator = " "
    newName = f"{separator.join(nickname)} Boi"
    await ctx.author.edit(nick=newName)
    # add Member role if not present
    role = discord.utils.get(ctx.guild.roles, name="Member")
    if role in ctx.author.roles:
        return
    else:
        await ctx.author.add_roles(role)

@saltBot.command()
async def ping(ctx):
    await ctx.channel.send(f"pongus bongus, latency was {str(saltBot.latency)}ms")

@saltBot.command()
async def die(ctx):
    await ctx.bot.logout()

saltBot.run(BOT_TOKEN)
