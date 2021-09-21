# import required dependicies
from logging import error
import nextcord
from nextcord import channel
from nextcord import Client
from nextcord import activity
from nextcord.ext import commands
from nextcord.user import User
from nextcord import FFmpegPCMAudio
import math
import sqlite3
import json
import random
import asyncio
import os
from random import choice
from nextcord import Member
import pickle
from nextcord.ext.commands import Bot
from nextcord.ext.commands.core import has_permissions


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]



intents = nextcord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix='=', intents=intents)
client.remove_command('help')




determine_flip = [1, 0]


@ client.group(invoke_without_command=True)
async def help(ctx):
    em = nextcord.Embed(
        title="Help Menu", description="Use =help <command>, made with love! **Read below for more information.**", color=ctx.author.color)

    em.add_field(name="__Regular Commands__ *(lowercase)*",
                 value=" 8ball  •   food •  goodbye  •   help  •   join  •   kick  •   leave  •  selfcare  •  staff •  support  • hotlines,    **Made with love by slumber#9279**")
    em.add_field(name="__Our docs & github.__",
                value="https://github.com/slumbees/papa-bee-docs")
    em.add_field(name="How to access our commands in depth:",
                value="You can access it in depth by doing __=help <command>__")
    em.add_field(name="__Moderation Commands__ *(lowercase)*",
                value="kick • ban • purge • ping • channels")
    em.add_field(name="__Fun Commands__ *(lowercase)*",
                value="selfcare • food • 8ball • avatar • coinflip • goodbye • hello • tictactoe")
    em.add_field(name="__Utility Commands__ *(lowercase)*",
                value="help • staff • support • hotlines • userinfo • leave • join ")
    await ctx.send(embed=em)



@ help.command()
async def ping(ctx):
    em = nextcord.Embed(
        title="Ping", description="Sends latency from the bot. Pong!", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=ping")

    await ctx.send(embed=em)


@ help.command()
async def _8ball(ctx):
    em = nextcord.Embed(
        title="8Ball", description="Offers a series of answers to your question!", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=8ball <question>")

    await ctx.send(embed=em)


@ help.command()
async def food(ctx):
    em = nextcord.Embed(
        title="Food", description="Offers a series of answers to food choices!", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=food <question>")

    await ctx.send(embed=em)



@ help.command()
async def selfcare(ctx):
    em = nextcord.Embed(
        title="selfcare", description="Offers a series of suggestions for self care choices.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=selfcare <question>")

    await ctx.send(embed=em)


@ help.command()
async def hotlines(ctx):
    em = nextcord.Embed(
        title="hotlines", description="Showcases a link for the international hotlines. If you are struggling, please seek a professional.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=hotlines")

    await ctx.send(embed=em)


@ help.command()
async def userinfo(ctx):
    em = nextcord.Embed(
        title="userinfo", description="Showcases info about you or a user you mention.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=userinfo <member>")

    await ctx.send(embed=em)


@ help.command()
async def avatar(ctx):
    em = nextcord.Embed(
        title="avatar", description="Shows off your cool profile picture, or someone elses!", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=avatar <member>")

    await ctx.send(embed=em)


@ help.command()
async def userinf(ctx):
    em = nextcord.Embed(
        title="userinfo", description="Showcases info about you or a user you mention.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=userinfo <member>")

    await ctx.send(embed=em)


@ help.command()
async def join(ctx):
    em = nextcord.Embed(
        title="join", description="Joins the VC and plays lofi.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=join (must be in a vc)")

    await ctx.send(embed=em)



@ help.command()
async def goodbye(ctx):
    em = nextcord.Embed(
        title="goodbye", description="Says goodbye to the bot, and they respond back!", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=goodbye")

    await ctx.send(embed=em)


@ help.command()
async def channels(ctx):
    em = nextcord.Embed(
        title="channels", description="Shows verification info if you require verification in your server.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=channels")

    await ctx.send(embed=em)


@ help.command()
async def ban(ctx):
    em = nextcord.Embed(
        title="ban", description="Bans a user.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=ban <member> <reason>")

    await ctx.send(embed=em)


@ help.command()
async def kick(ctx):
    em = nextcord.Embed(
        title="kick", description="Kicks a user.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=kick <member> <reason>")

    await ctx.send(embed=em)


@ help.command()
async def leave(ctx):
    em = nextcord.Embed(
        title="leave", description="Makes the bot leave the VC.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=leave")

    await ctx.send(embed=em)

@ help.command()
async def support(ctx):
    em = nextcord.Embed(
        title="leave", description="Shows the support server and website for the bot.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=support")

    await ctx.send(embed=em)


@ help.command()
async def coinflip(ctx):
    em = nextcord.Embed(
        title="coinflip", description="Flips a coin.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=coinflip")

    await ctx.send(embed=em)

@ help.command()
async def purge(ctx):
    em = nextcord.Embed(
        title="coinflip", description="Purges the chat.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=purge | =purge <amount>")

    await ctx.send(embed=em)


@ help.command()
async def tictactoe(ctx):
    em = nextcord.Embed(
        title="coinflip", description="Purges the chat.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=tictactoe <member> <member> THEN =place <number> Two people must be playing.")

    await ctx.send(embed=em)


@ help.command()
async def mute(ctx):
    em = nextcord.Embed(
        title="mute", description="Mutes a user.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=mute <member> <reason>")

    await ctx.send(embed=em)


@ help.command()
async def unmute(ctx):
    em = nextcord.Embed(
        title="unmuted", description="Unmutes a user.", color=ctx.author.color)

    em.add_field(name="Command",
                 value="=unmute <member> <reason>")

    await ctx.send(embed=em)




@client.event
async def on_ready():
    print("The bot is ready to be used! Code on.")
    print("------------------")
    await client.change_presence(status=nextcord.Status.idle, activity=nextcord.Streaming(name='=help | discord.gg/e6fxnfPHd9', url='https://twitch.tv/slumbees'))




@client.command()
async def tictactoe(ctx, p1: nextcord.Member, p2: nextcord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")



@client.command()
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=20)
    await ctx.send("Channel has recently been purged.", delete_after=1.0)


@client.command()
async def hotlines(ctx):
    await ctx.send("Here's the international hotline list: https://www.apa.org/topics/crisis-hotlines ")



@client.command()
async def userinfo(ctx, member: nextcord.Member):

    roles = [role for role in member.roles]

    embed = nextcord.Embed(colour=member.color,
                          timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(
        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID.:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime(
        "%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime(
        "%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)


@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = nextcord.Embed(title="Coinflip | Beehive",
                              description=f"{ctx.author.mention} Flipped coin, we got Heads!")
        await ctx.send(embed=embed)

    else:
        embed = nextcord.Embed(title="Coinflip | Beehive",
                              description=f"{ctx.author.mention} Flipped coin, we got Tails!")
        await ctx.send(embed=embed)


@ client.command()
async def avatar(ctx, member: nextcord.Member):
    show_avatar = nextcord.Embed(
        color=nextcord.Color.dark_gray()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)



@client.command()
async def hello(ctx):
    await ctx.send("Hello, how are you?")


@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye, have a wonderful day!")




@client.command(aliases=['selfcare'])
async def _selfcare(ctx, *, question):
    responses = ['Take a shower!',
                 'Wash your face!',
                 'Eat a snack!',
                 'Watch your favorite series/video!',
                 'Listen to music!',
                 'Dance around your room!',
                 'Go on a walk!',
                 'Journal how you feel today.',
                 'Do some stretches, or yoga!',
                 'Pursue that one hobby you left off months ago.',
                 'Surround yourself around a positive enviornment!',
                 'Check on your friends and ask how they have been.',
                 'Take a break from the thing stressing you out.', ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def staff(ctx):
    await ctx.send("You can see who our staff members are by looking on the list!")

@client.command()
async def support(ctx):
    await ctx.send("You can find our support server at https://discord.gg/e6fxnfPHd9 | And our docs here: https://github.com/slumbees/papa-bee-docs")


@client.command()
async def music(ctx):
    await ctx.send("Music feature is currently in beta. Check back later for more!")


@client.command()
async def channels(ctx):
    await ctx.send("If you're unable to see the channels, you might be missing a role, if not, contact a staff member.")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('convert.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You are not in a voice channel! Please join one to run this command.")


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I have left the VC.")
    else:
        await ctx.send("I am not in a voice channel!")


@client.command(pass_context=True)
async def pause(ctx):
    voice = nextcord.utils.get(client.voice_client, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("I have paused the music.")


@client.command(pass_context=True)
async def resume(ctx):
    voice = nextcord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("I have resumed the music!")


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: nextcord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'user {member} has been thrown into the nether!')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permission to kick! >_>")


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: nextcord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'user {member} has been killed by the Ender Dragon.')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permission to ban! Dummy.")

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: nextcord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = nextcord.utils.get(guild.roles, name="Muted 2.0")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted 2.0")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = nextcord.Embed(title="muted", description=f"{member.mention} was muted ", colour=nextcord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")



@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: nextcord.Member):
   mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted 2.0")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = nextcord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=nextcord.Colour.light_gray())
   await ctx.send(embed=embed)





@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidely so',
                 'Without a doubt',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 "Don't count on it",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook is not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=['food'])
async def _food(ctx, *, question):
    responses = ['Yogurt',
                 'Cereal',
                 'Chips',
                 'Ramen',
                 'Pasta',
                 'Pizza',
                 'Leftovers',
                 'Fast Food',
                 'Healthy Foods',
                 'Candy',
                 'Microwavable Foods',
                 'Frozen Foods',
                 'Nothing, stop asking me.', ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('')
