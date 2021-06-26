import discord
import random
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = 'viro ')
status = cycle(['Protecting the Pangolins', 'Sleeping'])

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Protecting the Pangolins'))
    print('I have awakened, master')

@tasks.loop(hours=12)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left, they (might) be missed.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def suntzu(ctx, *, question):
    responses = ["The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.",
    "All warfare is based on deception.",
    "The supreme art of war is to subdue the enemy without fighting.",
    "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.",
    "If one knows their enemy, and knows themselves they need not fear the result of 100 battles.",
    "Hence to fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemy's resistance without fighting.",
    "Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.",
    "The opportunity to secure ourselves against defeat lies in our own hands, but the opportunity of defeating the enemy is provided by the enemy himself.",
    "Opportunities multiply as they are seized.",
    "There is no instance of a nation benefitting from prolonged warfare."]
    await ctx.send(f'{random.choice(responses)}')

@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


client.run('insert bot token here')
