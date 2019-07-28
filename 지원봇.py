import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("두군두군 벹연시!")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("지원아 안녕"):
        await message.channel.send("안냥ㅇ!")


access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
