import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "_", description = "Padhna to seekh phle")


@bot.event
async def on_ready():
    print("started as ", bot.user.name)

@bot.event
async def on_member_update(before, after):
    if before.status == discord.Status.online:
        if after.status == discord.Status.offline:
            channel = after.guild.text_channels[-1]
            await channel.send(f"{after.name} is {after.status}")
            

    elif before.status == discord.Status.offline:
        if after.status == discord.Status.online:
            channel = after.guild.text_channels[-1]
            await channel.send(f"{after.name} is {after.status}")


                

@bot.command()
async def info(ctx):
    await ctx.send(f"I am {bot.user.name}\n My Id {bot.user.id}")

@bot.command()
async def start_attendence(ctx):
    emoji = '\N{WHITE HEAVY CHECK MARK}'
    try:
        msg = await ctx.send("Give Your Attendence By reacting")
        await msg.add_reaction(emoji)
    except:
        await ctx.send("Turn on Add Reaction Perm")



bot.run("token")