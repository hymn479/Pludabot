import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("botstart")
    game = discord.Game("맞장뜨실")
    await client.change_presence(status=discord.Status.idle, activity=game)

    @client.event
    async def on_message(message):
        if message.content.startswith("지니바보"):
            await message.channel.send("어쩔안물")
        if message.content.startswith("!강화"):
            await message.channel.send("45%의 확률로 Lv1>Lv5로 강화됬습니다! 강화대기시간:30초")







access_token = os.environ["NTUwODgxNzAxNTQ3NzM3MDg4.XcZJwA.Httg_Du9AxiF4CRcBLEFd5ZCsYU"]
client.run(access_token)



            
