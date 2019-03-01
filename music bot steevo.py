import discord
import youtube_dl
from discord.ext import commands

TOKEN =
'NTUwMjA2NjU5NzM4MjA2MjA4.D1rQKg.wm6mqX1_QNIBPTtc4QkhQg_0ksI'
client = commands.Bot(command_prefix = '.')

players = {}

@client.event
async def on_ready():
	print('Bot online.')

@client.command(pass_context=True)
async def join(ctx):	
    channel = ctx.message.auther.voice.voice_channel
	await client.join_voice_channel(channel)
	
@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.disconnect()

@client.command(pass_context=True)
asyns def play(ctx, url):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = await voice.client.create_ytdl_player(url)
	players[server.id] = player
	player.start()
	
client.run(TOKEN)