import discord
import random
from discord.ext import commands
from Data import GetCharactersNames, GetGlidersNames, GetKartsNames, GetWheelsNames, CharacterData, KartData, WheelData, GliderData
activity = discord.Activity(type=discord.ActivityType.watching, name="you while you sleep")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
bot = commands.Bot(activity=activity, intents=intents)

TOKEN = '' # welcome to todays episode of jopes accidentally publishes his bot token to github again
class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Click To Verify", style=discord.ButtonStyle.primary, emoji="<:iconnobackground:1255228642934657086>", custom_id="verify_button")
    async def button_callback(self, button, interaction):
        guild = bot.get_guild(1013085921647792168)
        role = discord.utils.find(lambda r: r.name == 'Member', guild.roles)
        mem = guild.get_member(interaction.user.id)
        if role not in mem.roles:
            await mem.add_roles(role)
            await interaction.response.send_message("Verified", ephemeral=True)
        else:
            await interaction.response.send_message("You already have the member role", ephemeral=True)
        
@bot.event
async def on_message(message): #AC EMBED SENDER HERE
    if message.author.id == 650744537517522984 and message.content == "$ac":
        #1
        await message.channel.send("# Royal Raceway")
        await message.channel.send("https://media.discordapp.net/attachments/1301344785063477248/1302280327309430804/1.png?ex=673b5111&is=6739ff91&hm=686260d239ab83d2d89ec60a6c63a8de5f604a1742187dade756fff3b1408767&=&format=webp&quality=lossless\n")
        
        await message.channel.send("At the first turn to the left, over the lake\n⠀")
        await message.channel.send("[**Normal**](https://www.youtube.com/watch?v=hgKvnvulwtM&t=57s)\nDifficulty: ⭐⭐\n⠀")
        await message.channel.send("[**Shroomless**](https://youtu.be/IJHu8iyKnbE)\nDifficulty: ⭐⭐⭐⭐⭐")
        #2
        await message.channel.send("⠀\n⠀\n# Music Park")
        await message.channel.send("https://media.discordapp.net/attachments/1301344785063477248/1302280326965362778/3.png?ex=673b5111&is=6739ff91&hm=154a78f1679cd6a53214cfc1ab79ef5efd5af71631698fc51e01a3774e3abf06&=&format=webp&quality=lossless\n")
        
        await message.channel.send("At the turn before the drum\n⠀")
        await message.channel.send("[**Normal**](https://youtu.be/tOHvlULD1W0?si=XmX1qIWXfRY8CxKd&t=99)\nDifficulty: ⭐⭐⭐")
        #3
        await message.channel.send("⠀\n⠀\n# Sunshine Airport")
        await message.channel.send("https://media.discordapp.net/attachments/1301344785063477248/1302280327636451362/2.png?ex=673b5111&is=6739ff91&hm=d79c64794831d41c92b1dd51de60041540a78a8dc1d0d721d6827f92993ef0dd&=&format=webp&quality=lossless\n")
        
        await message.channel.send("At the final turn before the glider, over the water\n⠀")
        await message.channel.send("[**Normal**](https://youtu.be/P-JSI5qQEtU?si=X7P1P9BAj3BBm32U&t=66)\nDifficulty: ⭐⭐⭐⭐")
        #4
        await message.channel.send("⠀\n⠀\n# DK Jungle (Pre Wave 4 - Ver. 2.3.0)")
        await message.channel.send("https://media.discordapp.net/attachments/1013170145176338493/1307889763713552475/2024-17-11--20-06-44.png?ex=673bf2c3&is=673aa143&hm=cfe1bb1f1eb7b3451132349c7fe58661c8339f6638f0af7214717d711f277252&=&format=webp&quality=lossless\n")
        
        await message.channel.send("At the very end of the course\n⠀")
        await message.channel.send("[**Normal - Shroomless**](https://youtu.be/J07l5BO90lo?si=UKhibxk2EWV45a0X&t=37)\nDifficulty: ⭐⭐")
        #End
        await message.channel.send("⠀\n⠀\n⠀\n[**Candidate Document**](https://docs.google.com/document/d/1uh4SNfDFyjWt6TBAvXfTzniUP5s5Ee4O3az-Ol4o7F8/edit?usp=sharing)\nContains a list of every single corner in Mario Kart 8 Deluxe that has potential for an AntiCut")
        
        
    if message.author.id == 650744537517522984 and message.content == "$verinit":
        await message.channel.send(view=MyView())
    if message.author.id == 987931629685194782 and random.randint(0, 100) < 3:
        await message.channel.send('Waffles bad')
    if message.content.lower() in ['karttest', '/karttest', 'charactertest', '/charactertest']:
        target_channel = message.guild.get_channel(1013170155162972222)  # Get the channel object using the ID
        if (target_channel is not None) and (target_channel != message.channel) and (message.guild.id == 1013085921647792168): #there may be two checks in here that do the exact same fucking thing but I'm too scared of 2023 Jopes's coding abilities trust it to function properly
            await message.channel.purge(limit=1)
            await message.channel.send(f"Hey {message.author.mention}, please go to {target_channel.mention} to use that command. Thanks!")
    if message.author.id == 783176177162518551:
        print("id")
        await message.add_reaction('🐟')
    await bot.process_commands(message)
    
@bot.event
async def on_presence_update(before, after):
    if after.id == (650744537517522984):
        guild = bot.get_guild(1013085921647792168)
        Davy = guild.get_member(864409664208240663)
        if Davy is None:
            print("Davy is not found in the guild.")
            return
        role = discord.utils.find(lambda r: r.name == 'Admin', guild.roles)
        if role is None:
            print("Admin role not found.")
            return
        if after.status == discord.Status.offline:
            await Davy.remove_roles(role)
        else:
            await Davy.add_roles(role)
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
    if(ctx.guild.id == 1013085921647792168 and ctx.channel.id !=1013170155162972222):
        await ctx.respond(f"Hey {ctx.author.mention}, please go to {ctx.guild.get_channel(1013170155162972222).mention} to use that command. Thanks!")
    else:
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
@bot.event
async def on_ready():
    bot.add_view(MyView())
bot.run(TOKEN)
