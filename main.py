import discord
import random
from discord.ext import commands
from Data import GetCharactersNames, GetGlidersNames, GetKartsNames, GetWheelsNames, CharacterData, KartData, WheelData, GliderData
activity = discord.Activity(type=discord.ActivityType.watching, name="you while you sleep")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(activity=activity, intents=intents)

TOKEN = '' # welcome to todays episode of jopes accidentally publishes his bot token to github again

@bot.event
@bot.event
async def on_message(message):
    if message.author.id == 987931629685194782 and random.randint(0, 100) < 3:
        await message.channel.send('Waffles bad')
    if message.content.lower() in ['karttest', '/karttest', 'charactertest', '/charactertest']:
        target_channel = message.guild.get_channel(1013170155162972222)  # Get the channel object using the ID
        if target_channel is not None:
            await message.channel.purge(limit=1)
            await message.channel.send(f"Hey {message.author.mention}, please go to {target_channel.mention} to use that command. Thanks!")
    if message.author.id == 699320094119166064:
        print("toad gets destroyed and the bot probably crashes")
        await message.add_reaction("<:Goodshyguy:1066108921821024286>")
        await message.add_reaction("<:IMG_1443:1049859940459753512>")
        await message.add_reaction("<:badshyguy:1066108822470537277>")
        await message.add_reaction("<:bruhbomb:1080233198681870336>")
        await message.add_reaction("<:cola:1049864677259223050>")
        await message.add_reaction("<:emoji_4:1050214684738994249>")
        await message.add_reaction("<:emoji_5:1050214697758097408>")
        await message.add_reaction("<:emoji_6:1050214712282984498>")
        await message.add_reaction("<:wafflesdum:1066104213177909258>")
        await message.add_reaction("<a:luigi:1049864795119177818>")
    await bot.process_commands(message)
@bot.event
async def on_member_update(before, after):
    newNick = str(after.nick)
    oldNick = str(before.nick)
    if after.guild.id == 1013085921647792168:
        if after.id == 561627319345741845 and newNick != "Ignore this individual":
            print("Mac Detected")
            await after.edit(nick="Ignore this individual")
    print(newNick)
    if "pirate" in newNick.lower():
        if after.guild.id == 722086066596741144:
            guild = bot.get_guild(722086066596741144)
            role = discord.utils.find(lambda r: r.name == 'Pirate', guild.roles)
            if not role in after.roles:
                await after.add_roles(role)
    else:
        if after.guild.id == 722086066596741144:
            guild = bot.get_guild(722086066596741144)
            role = discord.utils.find(lambda r: r.name == 'Pirate', guild.roles)
            if role in after.roles:
                await after.remove_roles(role)
    
@bot.slash_command(name="charactertest")
async def Char_slash(ctx: discord.ApplicationContext, character: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetCharactersNames))):
    weight = 0
    best = {
        'Weight': weight,
        "kart": 'NA',
        "wheel": 'NA',
        "glider": 'NA',
        "speed": 0,
        "MiniTurbo": 0
    }
    for KRT in range(len(list(await GetKartsNames(ctx)))):
        for WHL in range(len(list(await GetWheelsNames(ctx)))):
            for GLD in range(len(list(await GetGlidersNames(ctx)))):
                Aspeed = (CharacterData[character]['Speed']+KartData[list(await GetKartsNames(ctx))[KRT]]['Speed']+WheelData[list(await GetWheelsNames(ctx))[WHL]]['Speed']+GliderData[list(await GetGlidersNames(ctx))[GLD]]['Speed'])
                Aminiturbo = (CharacterData[character]['MiniTurbo']+KartData[list(await GetKartsNames(ctx))[KRT]]['MiniTurbo']+WheelData[list(await GetWheelsNames(ctx))[WHL]]['MiniTurbo']+GliderData[list(await GetGlidersNames(ctx))[GLD]]['MiniTurbo'])
                x = (Aspeed-.75)*4 #speed = x
                y = (Aminiturbo-.75)*4#miniturbo = y
                weight = round(((1+(.006*y))*((((.005*y)*((x*.025)+7.45))*((8.9*((y*1)+20))+(8.8*((y*2)+70))+(2.7*((y*3)+120))))+(((8.9*(y*1))+(8.8*(y*2))+(2.7*(y*3)))*(((1.05+(.005*y))*((x*.025)+7.45)))-((x*.025)+7.45))+(((y*1)+15)*((.05*y)*((x*.025)+7.45)))+((y*1)*((.05*y+(1.30))*((x*.025)+7.45)))))+(.88*(8640*(.025*x))))
                if weight > best["Weight"]:
                    best = {
                        "kart": str(list(await GetKartsNames(ctx))[KRT]),
                        "wheel": str(list(await GetWheelsNames(ctx))[WHL]),
                        "glider": str(list(await GetGlidersNames(ctx))[GLD]),
                        "speed": x,
                        "MiniTurbo": y,
                        "Weight": weight
                    }
    x = best['speed']
    y = best['MiniTurbo']
    weight = best['Weight']
    kart = best['kart']
    wheel = best['wheel']
    glider = best['glider']
    weightpercentile = round((weight-4699)/48.69)
    embed=discord.Embed(title="Character Test", description= character + CharacterData[character]['Emojii'], color=0x00ffaa)
    embed.add_field(name="Parts:", value='Kart: ' + kart + KartData[kart]['Emojii'] + '   Wheel: ' + wheel + WheelData[wheel]['Emojii'] + '   Glider: ' + glider + GliderData[glider]['Emojii'], inline=False)
    embed.add_field(name="Score:", value="Speed: " + str(round(x)) + '\nMiniTurbo: ' + str(round(y)) +'\n\n**Weight: ' + str(weight) +'**', inline=True)
    embed.add_field(name="Percentile: " + str(weightpercentile), value=('\n(out of 100 karts this one would be better than ' + str(weightpercentile) + '\nof them)'), inline=True)
    embed.set_footer(text="Developed by Jopes on Youtube")
    await ctx.respond(embed=embed)
    
@bot.slash_command(name="karttest")
async def first_slash(ctx: discord.ApplicationContext, character: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetCharactersNames)), kart: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetKartsNames)), wheel: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetWheelsNames)), glider: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(GetGlidersNames))): 
    Aspeed = (CharacterData[character]['Speed']+KartData[kart]['Speed']+WheelData[wheel]['Speed']+GliderData[glider]['Speed'])
    Aminiturbo = (CharacterData[character]['MiniTurbo']+KartData[kart]['MiniTurbo']+WheelData[wheel]['MiniTurbo']+GliderData[glider]['MiniTurbo'])
    x = (Aspeed-.75)*4 #speed = x
    y = (Aminiturbo-.75)*4#miniturbo = y
    weight = round(((1+(.006*y))*((((.005*y)*((x*.025)+7.45))*((8.9*((y*1)+20))+(8.8*((y*2)+70))+(2.7*((y*3)+120))))+(((8.9*(y*1))+(8.8*(y*2))+(2.7*(y*3)))*(((1.05+(.005*y))*((x*.025)+7.45)))-((x*.025)+7.45))+(((y*1)+15)*((.05*y)*((x*.025)+7.45)))+((y*1)*((.05*y+(1.30))*((x*.025)+7.45)))))+(.88*(8640*(.025*x))))
    weightpercentile = round((weight-5293)/42.75)
    embed=discord.Embed(title="KartTest", description=CharacterData[character]['Emojii']+KartData[kart]['Emojii']+WheelData[wheel]['Emojii']+GliderData[glider]['Emojii'], color=0x00ffaa)
    embed.add_field(name="Parts:", value="Character: " + character + CharacterData[character]['Emojii'] + '   Kart: ' + kart + KartData[kart]['Emojii'] + '   Wheel: ' + wheel + WheelData[wheel]['Emojii'] + '   Glider: ' + glider + GliderData[glider]['Emojii'], inline=False)
    embed.add_field(name="Score:", value="Speed: " + str(round(x)) + '\nMiniTurbo: ' + str(round(y)) +'\n\n**Weight: ' + str(weight) +'**', inline=True)
    embed.add_field(name="Percentile: " + str(weightpercentile), value=('\n(out of 100 karts this one would be better than ' + str(weightpercentile) + '\nof them)'), inline=True)
    embed.set_footer(text="Developed by Jopes on Youtube")
    await ctx.respond(embed=embed)
bot.run(TOKEN)
