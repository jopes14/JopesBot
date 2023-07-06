import discord
import random
from discord.ext import commands
from Data import GetCharactersNames, GetGlidersNames, GetKartsNames, GetWheelsNames, CharacterData, KartData, WheelData, GliderData
activity = discord.Activity(type=discord.ActivityType.watching, name="you while you sleep")
bot = commands.Bot(activity=activity)
TOKEN = 'OTk3NTUwMDU1NTI1NDY2MjEy.G7Gm8Y.TaulUkHaJJIHF7LGeppm8FLRFPgLTkjVfmaCOU'
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
    Aspeed = (CharacterData[character]['Speed']+KartData[kart]['Speed']+WheelData[wheel]['Speed']+GliderData[glider]['Speed'])
    Aminiturbo = (CharacterData[character]['MiniTurbo']+KartData[kart]['MiniTurbo']+WheelData[wheel]['MiniTurbo']+GliderData[glider]['MiniTurbo'])
    x = (Aspeed-.75)*4 #speed = x
    y = (Aminiturbo-.75)*4#miniturbo = y
    weight = round((1.006*((((.005*y)*((x*.025)+7.45))*((8.9*((y*1)+20))+(8.8*((y*2)+70))+(2.7*((y*3)+120))))+(((8.9*(y*1))+(8.8*(y*2))+(2.7*(y*3)))*((1.05+(.005*y))*((x*.025)+7.45)))+(((y*1)+15)*((.05*y)*((x*.025)+7.45)))+((y*1)*((.05*y+(1.30))*((x*.025)+7.45)))))+(.88*(8640*(.025*x))))
    weightpercentile = round((weight-4875)/38.84)
    embed=discord.Embed(title="KartTest", description=CharacterData[character]['Emojii']+KartData[kart]['Emojii']+WheelData[wheel]['Emojii']+GliderData[glider]['Emojii'], color=0x00ffaa)
    embed.add_field(name="Parts:", value="Character: " + character + CharacterData[character]['Emojii'] + '   Kart: ' + kart + KartData[kart]['Emojii'] + '   Wheel: ' + wheel + WheelData[wheel]['Emojii'] + '   Glider: ' + glider + GliderData[glider]['Emojii'], inline=False)
    embed.add_field(name="Score:", value="Speed: " + str(x) + '\nMiniTurbo: ' + str(y) +'\n\n**Weight: ' + str(weight) +'**', inline=True)
    embed.add_field(name="Percentile: " + str(weightpercentile), value=('\n(out of 100 karts this one would be better than ' + str(weightpercentile) + '\nof them)'), inline=True)
    embed.set_footer(text="Developed by Jopes on Youtube")
    await ctx.respond(embed=embed)
bot.run(TOKEN)
