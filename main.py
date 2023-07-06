import discord
import random
from discord.ext import commands
from Data import GetCharactersNames, GetGlidersNames, GetKartsNames, GetWheelsNames, CharacterData, KartData, WheelData, GliderData
activity = discord.Activity(type=discord.ActivityType.watching, name="you while you sleep")
bot = commands.Bot(activity=activity)
TOKEN = 'OTk3NTUwMDU1NTI1NDY2MjEy.Gq3sbM.u-dtaT_LXJdQKJuIkEvhFSGy3ais0ckRz_1jXc'
@bot.event
async def on_message(ctx):
    if ctx.author.id == 987931629685194782 and random.randint(0,100) < 3:
    	await ctx.channel.send('Waffles bad')
    print ("recieved")
    if ctx.author.id == 699320094119166064:
        print ("toad gets destroyed and the bot probably crashes")
        await ctx.add_reaction(":Goodshyguy:1066108921821024286")
        await ctx.add_reaction(":IMG_1443:1049859940459753512")
        await ctx.add_reaction(":badshyguy:1066108822470537277")
        await ctx.add_reaction(":bruhbomb:1080233198681870336")
        await ctx.add_reaction(":cola:1049864677259223050")
        await ctx.add_reaction(":emoji_4:1050214684738994249")
        await ctx.add_reaction(":emoji_5:1050214697758097408")
        await ctx.add_reaction(":emoji_6:1050214712282984498")
        await ctx.add_reaction(":wafflesdum:1066104213177909258")
        await ctx.add_reaction("a:luigi:1049864795119177818")   
@bot.slash_command(name="karttest", guild_ids=[1013085921647792168])
async def first_slash(ctx: discord.ApplicationContext, character: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetCharactersNames)), kart: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetKartsNames)), wheel: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetWheelsNames)), glider: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetGlidersNames))): 
    await ctx.respond("You executed the slash command!")
bot.run(TOKEN)
