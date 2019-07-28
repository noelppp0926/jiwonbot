import discord

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


client.run("NTAwNjgyODM0OTQ4Nzg0MTI4.XT3DZA.XaJ4IYrIxldKc0e38fn1Y0vA6ps")
