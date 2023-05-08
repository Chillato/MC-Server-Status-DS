import traceback

import discord
import requests
from discord import app_commands, Intents, Client, Interaction
from discord.ext import commands

bot = "" # token

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("on")
    try:
        f = await client.tree.sync()
        print(f"commands : {len(f)}")
    except Exception as e:
        print(e)


@client.tree.command(name="java", description="check server java")
@app_commands.describe(ip="send ip server")
async def getbedrock(interaction: discord.Interaction, ip: str):
    try:
        java = requests.get(f"https://api.mcsrvstat.us/2/{ip}").json()
        ipserver = java["ip"]
        port = java["port"]
        host = java["hostname"]
        verison = java["version"]
        protocol = java["protocol"]
        online = java["players"]["online"]
        playermax = java["players"]["max"]
        embed = discord.Embed(title=f"ℹ️ | STATUS {host}")
        embed.add_field(name="🖋 IP", value=f"`{ipserver}`", inline=True)
        embed.add_field(name="🚪 PORT", value=f"`{port}`", inline=True)
        embed.add_field(name="✅ VERSION", value=f"`{verison}`", inline=True)
        embed.add_field(name="🅿️ PROTOCOL", value=f"`{protocol}`", inline=True)
        embed.add_field(name="🟢 Players", value=f"`{online}/{playermax}`", inline=True)
        embed.set_thumbnail(url="https://store-images.s-microsoft.com/image/apps.63471.14247769038588514.c32b7f8c-cb4d-4859-a2a8-4c02692f8838.3f807f20-cfcb-4a4a-aa27-32a9c7f72e9a?w=120")
        await interaction.response.send_message(embed=embed)
    except:
        await interaction.response.send_message("❗️Error, the host may be unreachable or invalid.")


@client.tree.command(name="bedrock", description="check server bedrock")
@app_commands.describe(ip="send ip server")
async def getbedrock(interaction: discord.Interaction, ip: str):
    try:
        bedrock = requests.get(f"https://api.mcsrvstat.us/bedrock/2/{ip}").json()
        ipserver = bedrock["ip"]
        port = bedrock["port"]
        host = bedrock["hostname"]
        software = bedrock["software"]
        verison = bedrock["version"]
        protocol = bedrock["protocol"]
        online = bedrock["players"]["online"]
        playermax = bedrock["players"]["max"]
        embed = discord.Embed(title=f"ℹ️ | STATUS {host}")
        embed.add_field(name="🖋 IP", value=f"`{ipserver}`", inline=True)
        embed.add_field(name="🚪 PORT", value=f"`{port}`", inline=True)
        embed.add_field(name="✅ VERSION", value=f"`{verison}`", inline=True)
        embed.add_field(name="🅿️ PROTOCOL", value=f"`{protocol}`", inline=True)
        embed.add_field(name="💻 SOFTWARE", value=f"`{software}`", inline=True)
        embed.add_field(name="🟢 Players", value=f"`{online}/{playermax}`", inline=True)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft/images/2/26/Minecraft-windows10-tile.png/revision/latest?cb=20170706080700")
        await interaction.response.send_message(embed=embed)
    except:
        traceback.print_exc()
        await interaction.response.send_message("❗️Error, the host may be unreachable or invalid.")

client.run(bot)
