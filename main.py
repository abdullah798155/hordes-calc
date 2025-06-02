
import discord
from discord.ext import commands
import requests
import json
import os



intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)

TOKEN='YOUR_TOKEN_HERE'

@client.event
async def on_ready():
    print('hello !')





@client.command()
async def prestige(ctx, nam:str):
    prestige=discord.Embed(title="`--prestige details--`",color=0x39FF14)
    
    prestige.set_image(url="https://media.discordapp.net/attachments/844630736362274826/993550551046426664/Prestige.png")
    url = "https://hordes.io/api/playerinfo/search"
    response = requests.post(url, json={"name":nam,"order":"fame","limit":100,"offset":0})
    json_data = json.loads(response.text)
    
    for t in json_data:
        if nam.lower()==t['name'].lower():
            
            x=t['prestige']
            prestige.add_field(name="```Current prestige :``` ",value=x,inline=False)
            prestige.add_field(name="```Current fame :``` ",value=t['fame'],inline=False)
            res = x-(x/5)
    
  

  
    
  
    
    
    if x<=0:
      prestige.add_field(name="```btw bruh u will never have that prestige in game``` ",value="XD",inline=False)
      
    elif x<=4000:
      prestige.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      
    elif x>4000 and x<=8000:
      prestige.add_field(name="```current rank :```",value="RECRUIT or UNCLEAN",inline=False)
      
      prestige.add_field(name="```current band :```",value="brown band [5 mov speed]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545878751154226/brown_band.png")
      
      
      
      
    elif x>8000 and x<=12000:
      prestige.add_field(name="```current rank : ```",value="NOVICE or BRAWLER",inline=False)
      prestige.add_field(name="```current band :```",value="wooden band,[50 mp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545917745610782/wooden_band.png")
      
      
    elif x>12000 and x<=16000:
      prestige.add_field(name="```current rank : ```",value="SQUIRE or SLAYER",inline=False)
      prestige.add_field(name="```current band :```",value="metal band [15% IF]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545957721518171/metal_band.png")
      
      
    elif x>16000 and x<=20000:
      prestige.add_field(name="```current rank : ```",value="APPRENTICE or RAVAGER",inline=False)
      prestige.add_field(name="```current band :silver band [5 min max dmg]```",value="silver band [5 min max dmg]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545981935239219/silver_band.png")
      
      
    elif x>20000 and x<=24000:
      prestige.add_field(name="```current rank :ADEPT or BREAKER```",value="ADEPT or BREAKER",inline=False)
      prestige.add_field(name="```current band :```",value="golden band [2 hp mp regian/5s]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546001510043668/golden_band.png")
      
     
    elif x>24000 and x<=28000:
      prestige.add_field(name="```current rank: ```",value="FIERCE MASTER or RUTHLESS DEMOLISHER",inline=False)
      prestige.add_field(name="```current crown : ```",value="brown crown [5 move speed]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546031067299840/brown_crown.png")
      
      
    elif x>28000 and x<=32000:
      prestige.add_field(name="```current rank :```",value="VALIANT KNIGHT or SAVAGE MARAUDER",inline=False)
      prestige.add_field(name="```current crown: ```",value="wooden crown [30 hp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546051782983730/wooden_crown.png")
      
      
    elif x>32000 and x<=36000:
      prestige.add_field(name="```current rank :```",value="GALLANT SOLDIER or WILD REAPER",inline=False)
      prestige.add_field(name="```current crown :```",value="metal crown[15% IF]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546074310578268/metal_crown.png")
      
      
    elif x>36000 and x<=40000:
      prestige.add_field(name="```current rank ```",value="FAMOUS VETERAN or DEFIANT LIBERATOR",inline=False)
      prestige.add_field(name="```current crown : ```",value="silver crown [5% crit]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546095202410617/silver_crown.png")
      
      
    elif x>40000 and x<=44000:
      prestige.add_field(name="```current rank :```",value="FEARLESS WARDEN or BOLD CHAMPION",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown [3% haste]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546117738410086/golden_crown_1.png")
      
      
    elif x>44000 and x<=48000:
      prestige.add_field(name="```current rank : ```",value="SUPREME COMMANDER or RESTLESS HERO",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown with blue diamond [30 hp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546138403741776/golden_crown_blue.png")
      
      
    elif x>48000:
      prestige.add_field(name="```current rank :```",value="LORD or CHOSEN",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown with red diamond [5 min max dmg]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993532525303578675/golden_crown.png")
      
      
      
    prestige.add_field(name="------IF U DONT DO PVP FOR A WEEK ------",value="😐",inline=False)
    prestige.add_field(name="Your prestige will be :",value=res,inline=False)
  
  
    
    prestige.add_field(name=" you will lose :",value=res/4,inline=False)
    
    
  
    if res<=0:
      prestige.add_field(name="```btw bruh u will never have that prestige in game``` ",value="XD",inline=False)
      await ctx.send(embed=prestige)
    elif res<=4000:
      prestige.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      await ctx.send(embed=prestige)
    elif res>4000 and res<=8000:
      prestige.add_field(name="```u will be RECRUIT or UNCLEAN ```",value="[brown band] [5 move speed]",inline=False)
      await ctx.send(embed=prestige)
      
      
      
    elif res>8000 and res<=12000:
      prestige.add_field(name="```u will be NOVICE or BRAWLER ```",value="[wooden band] [50 mp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>12000 and res<=16000:
      prestige.add_field(name="```u will be SQUIRE or SLAYER ```",value="[metal band] [15% IF]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>16000 and res<=20000:
      prestige.add_field(name="```u will be APPRENTICE or RAVAGER ```",value="[silver band] [5 min max dmg]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>20000 and res<=24000:
      prestige.add_field(name="```u will be ADEPT or BREAKER ```",value="[golden band] [2 hp mp regain /5s]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>24000 and res<=28000:
      prestige.add_field(name="```u will be FIERCE MASTER or RUTHLESS DEMOLISHER ```",value="[brown crown] [5 move speed]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>28000 and res<=32000:
      prestige.add_field(name="```u will be VALIANT KNIGHT or SAVAGE MARAUDER ```",value="[wooden crown] [30hp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>32000 and res<=36000:
      prestige.add_field(name="```u will be GALLANT SOLDIER or WILD REAPER ```",value="[metal crown] [15% IF]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>36000 and res<=40000:
      prestige.add_field(name="```u will be FAMOUS VETERAN or DEFIANT LIBERATOR ```",value="[silver crown] [5% crit]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>40000 and res<=44000:
      prestige.add_field(name="```u will be FEARLESS WARDEN or BOLD CHAMPION ```",value="[golden crown] [3% haste]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>44000 and res<=48000:
      prestige.add_field(name="```u will be SUPREME COMMANDER or RESTLESS HERO ```",value="[golden crown with blue gem] [30 hp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>48000:
      prestige.add_field(name="```u will be LORD or CHOSEN ```",value="[golden crown with red gem] [5 min max dmg]",inline=False)
      prestige.add_field(name="```congrats! :D u have achieved top rank , mantain it by doing pvp and obelisk```",value="🥳",inline=False)
      
      await ctx.send(embed=prestige) 
        
   

@client.command()
async def p(ctx, nam:str):
    prestige=discord.Embed(title="`--prestige details--`",color=0x39FF14)
    
    prestige.set_image(url="https://media.discordapp.net/attachments/844630736362274826/993550551046426664/Prestige.png")
    url = "https://hordes.io/api/playerinfo/search"
    response = requests.post(url, json={"name":nam,"order":"fame","limit":100,"offset":0})
    json_data = json.loads(response.text)
    for t in json_data:
        if nam==t['name']:
            x=t['prestige']
            prestige.add_field(name="```Current prestige :``` ",value=x,inline=False)
            prestige.add_field(name="```Current fame :``` ",value=t['fame'],inline=False)
    res = x-(x/5)
    
  

  
    
  
    
    
    if x<=0:
      prestige.add_field(name="```btw bruh u will never have that prestige in game``` ",value="XD",inline=False)
      
    elif x<=4000:
      prestige.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      
    elif x>4000 and x<=8000:
      prestige.add_field(name="```current rank :```",value="RECRUIT or UNCLEAN",inline=False)
      
      prestige.add_field(name="```current band :```",value="brown band [5 mov speed]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545878751154226/brown_band.png")
      
      
      
      
    elif x>8000 and x<=12000:
      prestige.add_field(name="```current rank : ```",value="NOVICE or BRAWLER",inline=False)
      prestige.add_field(name="```current band :```",value="wooden band,[50 mp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545917745610782/wooden_band.png")
      
      
    elif x>12000 and x<=16000:
      prestige.add_field(name="```current rank : ```",value="SQUIRE or SLAYER",inline=False)
      prestige.add_field(name="```current band :```",value="metal band [15% IF]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545957721518171/metal_band.png")
      
      
    elif x>16000 and x<=20000:
      prestige.add_field(name="```current rank : ```",value="APPRENTICE or RAVAGER",inline=False)
      prestige.add_field(name="```current band :silver band [5 min max dmg]```",value="silver band [5 min max dmg]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545981935239219/silver_band.png")
      
      
    elif x>20000 and x<=24000:
      prestige.add_field(name="```current rank :ADEPT or BREAKER```",value="ADEPT or BREAKER",inline=False)
      prestige.add_field(name="```current band :```",value="golden band [2 hp mp regian/5s]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546001510043668/golden_band.png")
      
     
    elif x>24000 and x<=28000:
      prestige.add_field(name="```current rank: ```",value="FIERCE MASTER or RUTHLESS DEMOLISHER",inline=False)
      prestige.add_field(name="```current crown : ```",value="brown crown [5 move speed]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546031067299840/brown_crown.png")
      
      
    elif x>28000 and x<=32000:
      prestige.add_field(name="```current rank :```",value="VALIANT KNIGHT or SAVAGE MARAUDER",inline=False)
      prestige.add_field(name="```current crown: ```",value="wooden crown [30 hp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546051782983730/wooden_crown.png")
      
      
    elif x>32000 and x<=36000:
      prestige.add_field(name="```current rank :```",value="GALLANT SOLDIER or WILD REAPER",inline=False)
      prestige.add_field(name="```current crown :```",value="metal crown[15% IF]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546074310578268/metal_crown.png")
      
      
    elif x>36000 and x<=40000:
      prestige.add_field(name="```current rank ```",value="FAMOUS VETERAN or DEFIANT LIBERATOR",inline=False)
      prestige.add_field(name="```current crown : ```",value="silver crown [5% crit]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546095202410617/silver_crown.png")
      
      
    elif x>40000 and x<=44000:
      prestige.add_field(name="```current rank :```",value="FEARLESS WARDEN or BOLD CHAMPION",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown [3% haste]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546117738410086/golden_crown_1.png")
      
      
    elif x>44000 and x<=48000:
      prestige.add_field(name="```current rank : ```",value="SUPREME COMMANDER or RESTLESS HERO",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown with blue diamond [30 hp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546138403741776/golden_crown_blue.png")
      
      
    elif x>48000:
      prestige.add_field(name="```current rank :```",value="LORD or CHOSEN",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown with red diamond [5 min max dmg]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993532525303578675/golden_crown.png")
      
      
      
    prestige.add_field(name="------IF U DONT DO PVP FOR A WEEK ------",value="😐",inline=False)
    prestige.add_field(name="Your prestige will be :",value=res,inline=False)
  
  
    
    prestige.add_field(name=" you will lose :",value=res/4,inline=False)
    
    
  
    if res<=0:
      prestige.add_field(name="```btw bruh u will never have that prestige in game``` ",value="XD",inline=False)
      await ctx.send(embed=prestige)
    elif res<=4000:
      prestige.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      await ctx.send(embed=prestige)
    elif res>4000 and res<=8000:
      prestige.add_field(name="```u will be RECRUIT or UNCLEAN ```",value="[brown band] [5 move speed]",inline=False)
      await ctx.send(embed=prestige)
      
      
      
    elif res>8000 and res<=12000:
      prestige.add_field(name="```u will be NOVICE or BRAWLER ```",value="[wooden band] [50 mp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>12000 and res<=16000:
      prestige.add_field(name="```u will be SQUIRE or SLAYER ```",value="[metal band] [15% IF]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>16000 and res<=20000:
      prestige.add_field(name="```u will be APPRENTICE or RAVAGER ```",value="[silver band] [5 min max dmg]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>20000 and res<=24000:
      prestige.add_field(name="```u will be ADEPT or BREAKER ```",value="[golden band] [2 hp mp regain /5s]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>24000 and res<=28000:
      prestige.add_field(name="```u will be FIERCE MASTER or RUTHLESS DEMOLISHER ```",value="[brown crown] [5 move speed]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>28000 and res<=32000:
      prestige.add_field(name="```u will be VALIANT KNIGHT or SAVAGE MARAUDER ```",value="[wooden crown] [30hp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>32000 and res<=36000:
      prestige.add_field(name="```u will be GALLANT SOLDIER or WILD REAPER ```",value="[metal crown] [15% IF]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>36000 and res<=40000:
      prestige.add_field(name="```u will be FAMOUS VETERAN or DEFIANT LIBERATOR ```",value="[silver crown] [5% crit]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>40000 and res<=44000:
      prestige.add_field(name="```u will be FEARLESS WARDEN or BOLD CHAMPION ```",value="[golden crown] [3% haste]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>44000 and res<=48000:
      prestige.add_field(name="```u will be SUPREME COMMANDER or RESTLESS HERO ```",value="[golden crown with blue gem] [30 hp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>48000:
      prestige.add_field(name="```u will be LORD or CHOSEN ```",value="[golden crown with red gem] [5 min max dmg]",inline=False)
      prestige.add_field(name="```congrats! :D u have achieved top rank , mantain it by doing pvp and obelisk```",value="🥳",inline=False)
      
      await ctx.send(embed=prestige)
  


       

    
    
    
@client.command()
async def gloom(ctx):
  gloom=discord.Embed(title="```--GLOOMFURY WORLD BOSS TIMINGS--```",color=0x7F00FF)
  gloom.add_field(name="`All times based on UTC`",value="`[Coordinated Universal Time]`",inline=False)
  gloom.add_field(name="If u want to convert UTC into other time zones click below 🔽",value="https://savvytime.com/converter/utc",inline=False)
  gloom.set_image(url="https://media.discordapp.net/attachments/844630736362274826/991729935335034972/utc_gloom_border_sharpened.png")
  gloom.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/991563829790126151/unknown.png")
  await ctx.send(embed=gloom)
                      
                      

   
 

@client.command()
async def helpme(ctx):
 
  helpme=discord.Embed(title="Hordes[calc]",description="```COOL DISCORD BOT WHICH EASE YOUR TASK IN CALCULATIONS OF HORDES GAME```",color=0x4dff4d)
  
  
  helpme.set_author(name="Datablaze | Thundrax7",icon_url="https://media.discordapp.net/attachments/844630736362274826/980888307728809994/speedy2.png?width=580&height=580")
  helpme.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/924693581137076225/discord-avatar-512-BU83E.png")
  helpme.add_field(name="```!info <ingame name>```",value="shows player details",inline=False)
  helpme.add_field(name="```!prestige <In game name [case sensitive]> [or] !p <name>```",value="It shows prestige details",inline=False)
  helpme.add_field(name="```!clan <clan tag>```",value="Shows u clan details , players online and clan owner",inline=False)
  helpme.add_field(name="```!defense <enter your def> <incoming dmg> <your hp>```",value="It shows dmg u will take after reduction,also shows if u will be 1 shotted or not",inline=False)
  helpme.add_field(name="```!haste <enter your haste> <enter cast time or cooldown>```",value="shows u remaining cast time or remianing cooldown",inline=False)
  helpme.add_field(name="```!gloom```",value="It shows world boss details",inline=False)
  helpme.add_field(name="```!dps <class name> <min> <max> <haste> <crit>```",value="shows u approx gloom dps",inline=False)
  helpme.add_field(name="```!map```",value="shows u all 3 maps with monster levels",inline=False)
  helpme.add_field(name="```!obe```",value="shows obelisk spots",inline=False)
 
  await ctx.send(embed=helpme)




@client.command()
async def haste(ctx,x:float, y:float):
  t=y
  z=1/(1+(x/100))*100
  p=y*z/100
  
  haste=discord.Embed(title="```--Haste & Cooldown--```",color=0x39FF14)
  haste.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/981582799297458236/hordes_presskit_real.png")
  haste.add_field(name="Entered haste :",value=x,inline=False)
  haste.add_field(name="Entered cooldown or casttime",value=y,inline=False)
  haste.add_field(name="Calculations :",value="",inline=False)
  haste.add_field(name="Remaining cast time or cooldown is :",value=p,inline=False)
  haste.add_field(name="Cast time or cooldown reduced is :",value=t-p,inline=False)
  await ctx.send(embed=haste)
  

@client.command()
async def test(ctx,x:str):
  
  await ctx.send("your text is `{}`".format(x))

@client.command()
async def d(ctx,i:float,j:float,z:float):
  defense=discord.Embed(title="```--Defense Report--```",color=0x39FF14)
  defense.add_field(name="------------------------⚔️-------------------------",value="```--ENTERED DETAILS--```",inline=False)
  defense.add_field(name="Your defense:",value=i,inline=True)
  defense.add_field(name="Entered incoming dmg :",value=j,inline=True)
  defense.add_field(name="Your hp :",value=z,inline=True)
  defense.add_field(name="---------------------------⚔️----------------------",value="```--CALCULATED DETAILS--```",inline=False)
  defense.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/981582799297458236/hordes_presskit_real.png")
  defense.set_footer(text="usage: !defense <enter your def> <incoming damage> <your hp>")
  
  
  
  if(i<=310000):
    l=(1 - (1/(2.71828**(i*0.0022))))*0.87
    def_red=l*100
    
  else:
    await ctx.send("```too much def man ! overflow error 💀```")
    
    
  
  
  reduc=j*(def_red/100)
  inc_dmg=j-reduc
  
  
  g=inc_dmg
  n=def_red
  n=format(n,".2f")
  tk=j-g
  tk=format(tk,".2f")
  g=format(g,".2f")
  defense.add_field(name="Finally u will take [approx]🛡️:",value=g,inline=True)
  
  defense.add_field(name="Dmg reduction [%]:",value=n,inline=True)
  defense.add_field(name="Intake dmg reduced:",value=tk,inline=True)
  
  if (z-inc_dmg)<=0:
    defense.add_field(name="u will be 1 SHOTTED ",value="😭",inline=False)
    shot=(100*z)/(100-def_red)
    shot=format(shot,".2f")
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=shot,inline=False)
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454719215771688/1_shotted_resize_hd_yes.png")
    
    
    
    await ctx.send(embed=defense)
  else:
    k=z-inc_dmg
    inc_dmg=format(inc_dmg,".2f")
    k=format(k,".2f")
    shot=(100*z)/(100-def_red)
    shot=format(shot,".2f")
    defense.add_field(name="U will NOT be 1 shotted 😀[u will be left with below hp]",value=k,inline=False)
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=shot,inline=False)
    
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454744515805266/1_shotted_resize_hd_1_no.png")
    await ctx.send(embed=defense)


@client.command()
async def defense(ctx,i:float,j:float,z:float):
  defense=discord.Embed(title="```--Defense Report--```",color=0x39FF14)
  defense.add_field(name="------------------------⚔️-------------------------",value="```--ENTERED DETAILS--```",inline=False)
  defense.add_field(name="Your defense:",value=i,inline=True)
  defense.add_field(name="Entered incoming dmg :",value=j,inline=True)
  defense.add_field(name="Your hp :",value=z,inline=True)
  defense.add_field(name="---------------------------⚔️----------------------",value="```--CALCULATED DETAILS--```",inline=False)
  defense.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/981582799297458236/hordes_presskit_real.png")
  defense.set_footer(text="usage: !defense <enter your def> <incoming damage> <your hp>")
  
  
  
  if(i<=310000):
    l=(1 - (1/(2.71828**(i*0.0022))))*0.87
    def_red=l*100
    
  else:
    await ctx.send("```too much def man ! overflow error 💀```")
    
    
  
  
  reduc=j*(def_red/100)
  inc_dmg=j-reduc
  
  
  g=inc_dmg
  n=def_red
  n=format(n,".2f")
  tk=j-g
  tk=format(tk,".2f")
  g=format(g,".2f")
  defense.add_field(name="Finally u will take [approx]🛡️:",value=g,inline=True)
  
  defense.add_field(name="Dmg reduction [%]:",value=n,inline=True)
  defense.add_field(name="Intake dmg reduced:",value=tk,inline=True)
  
  if (z-inc_dmg)<=0:
    defense.add_field(name="u will be 1 SHOTTED ",value="😭",inline=False)
    shot=(100*z)/(100-def_red)
    shot=format(shot,".2f")
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=shot,inline=False)
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454719215771688/1_shotted_resize_hd_yes.png")
    
    
    
    await ctx.send(embed=defense)
  else:
    k=z-inc_dmg
    inc_dmg=format(inc_dmg,".2f")
    k=format(k,".2f")
    shot=(100*z)/(100-def_red)
    shot=format(shot,".2f")
    defense.add_field(name="U will NOT be 1 shotted 😀[u will be left with below hp]",value=k,inline=False)
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=shot,inline=False)
    
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454744515805266/1_shotted_resize_hd_1_no.png")
    await ctx.send(embed=defense)

@client.command()
async def map(ctx):
  map=discord.Embed(title="```--NEW WORLD--```",color=0x39FF14)
  map.set_image(url="https://static.miraheze.org/hordesiowiki/thumb/a/aa/World_Map.jpg/1350px-World_Map.jpg")
  await ctx.send(embed=map)
 

@client.command()
async def obe(ctx):
  obe=discord.Embed(title="```OBELISK SPOTS```",color=0x39FF14)
  obe.set_image(url="https://media.discordapp.net/attachments/221772925282287627/1002585345185034340/Obelisk_Spots.png?width=580&height=580")
  await ctx.send(embed=obe)

@client.command()
async def dps(ctx,class1:str,min:float,max:float,haste:float,crit:float):
  
  dps=discord.Embed(title="```APPROX GLOOM DPS```",color=0x39FF14)
  dps.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/991563829790126151/unknown.png")
  
  
  dps.set_footer(text="It depends on many other factors like duration, skill set etc")
  dmg=((min+max)/2)*((100+crit)/100)*((haste+100)/100)
  
  if(class1=="a" or class1=="archer" or class1=="m" or class1=="mage" or class1=="Mage" or class1=="Archer"):
    
    dps.add_field(name="--------------------------------------------------------------------", value="```--Before buffs--```",inline=False)
    dps.add_field(name="Min", value=f"```{min}```",inline=True)
    dps.add_field(name="Max", value=f"```{max}```",inline=True)
    dps.add_field(name="Haste", value=f"```{haste}```",inline=True)
    dps.add_field(name="Crit", value=f"```{crit}```",inline=True)
    dps.add_field(name="----------------------------------------------------------------------------", value="```--After buffs--```",inline=False)
    dps.add_field(name="Min", value=f"```{min+20}```",inline=True)
    dps.add_field(name="Max", value=f"```{max+33}```",inline=True)
    dps.add_field(name="haste [temp+canine]", value=f"```{haste+52}```",inline=True)
    dps.add_field(name="crit", value=f"```{crit+12}```",inline=True)
    
    
    dps.add_field(name="Approx gloom DPS :", value=dmg*3.4,inline=False)
    dps.add_field(name="NOTE: Its just approx DPS", value="Its just to get rough idea",inline=False)
    await ctx.send(embed=dps)
  elif(class1=="w" or class1=="warrior" or class1=="Warrior"):
     dps.add_field(name="------------------------------------------------------------", value="```--Before buffs--```",inline=False)
     dps.add_field(name="Min", value=f"```{min}```",inline=True)
     dps.add_field(name="Max", value=f"```{max}```",inline=True)
     dps.add_field(name="Haste", value=f"```{haste}```",inline=False)
     dps.add_field(name="Crit", value=f"```{crit}```",inline=True)
     dps.add_field(name="--------------------------------------------------------------------------", value="```--After buffs--```",inline=False)
     dps.add_field(name="Min", value=f"```{min+20}```",inline=True)
     dps.add_field(name="Max", value=f"```{max+30}```",inline=True)
     dps.add_field(name="Haste [temp+canine]", value=f"```{haste+52}```",inline=True)
     dps.add_field(name="Crit", value=f"```{crit+12}```",inline=True)
     dps.add_field(name="Approx gloom DPS :", value=f"```{dmg*4.25}```",inline=False)
     dps.add_field(name="NOTE: Its just approx DPS", value="Its just to get rough idea",inline=False)
     await ctx.send(embed=dps)
  elif(class1=="s" or class1=="shaman" or class1=="Shaman"):
    dps.add_field(name="sorry! HPS is cuurently not available", value="😢  ",inline=False)
    await ctx.send(embed=dps)
  
  else:
    dps.add_field(name="Invalid syntax", value="usage : !dps <enter ur class > <min> <max> <haste> <crit>",inline=False)
    await ctx.send(embed=dps)
    
    


@client.command()
async def datablaze(ctx):
    datablaze=discord.Embed(title="```HELLO ITS ME !```",color=0x39FF14)
    datablaze.set_image(url="https://media.discordapp.net/attachments/822116199877181533/1014480517145559100/unknown.png")
    await ctx.send(embed=datablaze)

@client.command()
async def reflect(ctx):
    reflect=discord.Embed(title="```ReflectHub```",url="https://reflecthub.github.io", color=0x39FF14)
    reflect.add_field(name="Reflect ✨ ",value=f"```Read Quran and watch these videos sincerely and reflect upon them deeply, so you may find truth and accept it!```",inline=True)
    reflect.set_thumbnail(url="https://raw.githubusercontent.com/reflecthub/reflecthub.github.io/refs/heads/main/image.png")
    reflect.set_image(url="https://raw.githubusercontent.com/reflecthub/reflecthub.github.io/refs/heads/main/Homepage.png")
    await ctx.send(embed=reflect)
    
@client.command()
async def wyrm(ctx):
    wyrm=discord.Embed(title="```WYRM```",color=0x39FF14)
    wyrm.set_image(url="https://media.discordapp.net/attachments/1003284338454048948/1006497246302445568/unknown.png")
    await ctx.send(embed=wyrm)
    
    
@client.command()
async def yt(ctx):
    yt=discord.Embed(title="```MY YOUTUBE CHANNEL```",url="https://www.youtube.com/channel/UCHk0l3XUXYRHpHo6vI2xYjg",color=0xff0000 )
    yt.add_field(name="Link :", value="https://www.youtube.com/channel/UCHk0l3XUXYRHpHo6vI2xYjg",inline=True)
    yt.set_image(url="https://media.discordapp.net/attachments/822116199877181533/1014418551349706792/unknown.png?width=899&height=580")
    yt.set_thumbnail(url="https://media.discordapp.net/attachments/924626925161422849/929703058437443624/speedy2.png?width=580&height=580")
    yt.set_footer(text="Pls make sure to subscribe :D")
    
    await ctx.send(embed=yt)
    
@client.command()
async def itu(ctx):
    itu=discord.Embed(title="```ITU - SHADOW FIGHT 4: ARENA [LEGENDARY HERO]```",color=0x00ffff )
    itu.add_field(name="Description", value=f"```The desire to comprehend absolute knowledge made Itu an ambassador of infinity itself. He has seen many versions of this world, and fate has chosen him to remember them all. The mysteries he carries cannot be shared with anyone, leaving him alone in his wanderings. But he has learned to embrace it.```",inline=True)
    itu.set_image(url="https://cdn.discordapp.com/attachments/825982981948702740/1250076892007235655/itureal.gif?ex=6669a054&is=66684ed4&hm=d3acf937dd9d5fe7eca1f278745df9a2193e6819539be3e22eef6962bb3f15ba&")
    itu.set_thumbnail(url="https://media.discordapp.net/attachments/825982981948702740/1250062720322113547/itu_sticker.jpg?ex=66699321&is=666841a1&hm=691aa268c74f646976eb306a43b8f2ece816a9fd1ecbe58b07d83e09e4c3262c&=&format=webp&width=407&height=571")
    itu.set_footer(text="Itu is a paragon of discipline. His fighting is impeccable-- as precise and concise as his Shinken sword. He calculates his every move numerous steps ahead. And now Itu, having traversed the very fabric of reality, is able to control the flow of time itself.")
    tl=discord.Embed(title="```TALENTS```",color=0x00ffff )
    tl.set_image(url="https://media1.tenor.com/m/zlhyFffEzKcAAAAd/itu-shadow-fight-behold-the-future-itu.gif")
    tl.add_field(name="Yadomejutsu", value=f"```Itu is able to deflect a ranged attack with a crouch. If the attack cannot be deflected, Itu will dodge it.```",inline=False)
    tl.add_field(name="Shadow Sync ", value=f"```At the start of the round, Itu instantly gains some shadow energy.```",inline=False)
    tl.add_field(name="Paradox ", value=f"```Itu takes no damage during Time Manipulation.```",inline=False)
    tl.add_field(name="Cutting Edge ", value=f"```If the Spacetime Slash fails, Itu leaves an energy impulse that deals damage to the opponent on impact.```",inline=True)
    tl.add_field(name="Quintessence ", value=f"```Itu's successful attacks during Time Manipulation are critical.```",inline=False)
    tl.add_field(name="Metaphysical Calculation", value=f"```Itu restores some health while concentrating before the Spacetime Slash.```",inline=False)
    tl.add_field(name="Ambassador of Infinity", value=f"```Time Manipulation charge accumulates faster if Itu's health is low.```",inline=False)
    tl.add_field(name="Forget The Past ", value=f"```The Spacetime Slash does not need a full bar of shadow energy to be activated.```",inline=False)
    tl.add_field(name="Behold The Future ", value=f"```Upon achieving maximum concentration before the Spacetime Slash, Itu performs an attack that is impossible to evade.```",inline=False)
    
    
    await ctx.send(embed=itu)
    await ctx.send(embed=tl)
    
@client.command()
async def info(ctx,nam:str):
    info=discord.Embed(title="```--Player Info--```",color=0x39FF14)
    c=0
    url = "https://hordes.io/api/playerinfo/search"
    response = requests.post(url, json={"name":nam,"order":"fame","limit":100,"offset":0})
    json_data = json.loads(response.text)
    if json_data==[]:
        await ctx.send("```Player does not exist 🟥```")
        
    else:
         for x in json_data:
                c=c+1
                fl=0
                if nam.lower()==x['name'].lower():
                    a = [0 for _ in range(14)]
                    f = [0 for _ in range(14)]
                    k = 2000
                    b = 0
    
                    i = 0
                    p = 0
     
                    p=x['prestige']
                    for i in range(1, 14):
                        a[i] = k
                        k+=1000
                    h = 4000
                    pos = 0
                    dec = int(p-(p/5))
                    for i in range(1, 13):
                        f[i] = h
                        h+=4000
                    for i in range(1, 13):
                        if f[i]> p:
                            pos = i
                            break
                    for i in range(1, 13):
                        if dec+a[i]> f[pos]:
                            break
                    
                    fl=1
                    await ctx.send("```Player exists 🟩```")
                    role=['Mage','Archer','Shaman','Warrior']
                    icon=discord.Embed(title=f"```--{role[x['pclass']-1]}--```",color=0x39FF14)
                    icon.add_field(name='',value=f'```[🔥 {nam} 🔥]```',inline=False)
                    if x['pclass']==1:
                        info.set_thumbnail(url="https://media.discordapp.net/attachments/822116199877181533/1084009059662962688/Mage.png?width=40&height=40")
                        icon.set_image(url="https://media.discordapp.net/attachments/980518130495402099/1360188936802144356/Mage.png?ex=67fa3629&is=67f8e4a9&hm=8415ef59c0f5551127040bf4b9d1b085a80b067a05003e0819c3728823e26bc8&=&format=webp&quality=lossless&width=661&height=650")
                        info.add_field(name='Class:',value='```Mage```',inline=True)
                    elif x['pclass']==2:
                        info.set_thumbnail(url="https://static.miraheze.org/hordesiowiki/2/29/Archer.png")
                        icon.set_image(url="https://media.discordapp.net/attachments/980518130495402099/1360188959862554674/Archer.png?ex=67fa362f&is=67f8e4af&hm=25bc56db363f16dfc5a05c1eed1a257aa142cc5429c27020e5c19228ffbd7743&=&format=webp&quality=lossless&width=596&height=540")
                        info.add_field(name='Class:',value='```Archer```',inline=True)
                    elif x['pclass']==3:
                        info.set_thumbnail(url="https://static.miraheze.org/hordesiowiki/5/56/Shaman.png")
                        icon.set_image(url="https://media.discordapp.net/attachments/980518130495402099/1360188986563362887/Shaman.png?ex=67fa3635&is=67f8e4b5&hm=9ba67f3a32912f7fd5ba97bf964864020235111f25ad7d4974c92287c25d931c&=&format=webp&quality=lossless&width=508&height=505")
                        info.add_field(name='Class:',value='```Shaman```',inline=True)
                    elif x['pclass']==0:
                        info.set_thumbnail(url="https://static.miraheze.org/hordesiowiki/9/97/Warrior.png")
                        icon.set_image(url="https://media.discordapp.net/attachments/980518130495402099/1360189004779229225/Warrior.png?ex=67fa3639&is=67f8e4b9&hm=ffb6ecf45a978801b64f32c67a596dd0a8cc7a5d24954fb82b0324894b297149&=&format=webp&quality=lossless&width=520&height=468")
                        info.add_field(name='Class:',value='```Warrior```',inline=True)
          
                    info.add_field(name='Name:',value=f"```{nam}```",inline=True) 
                    
                    
                    
                    if x['faction']==1:
                        info.add_field(name="Faction:",value=f"```Bloodlust```",inline=True)
                        info.set_image(url="https://static.miraheze.org/hordesiowiki/1/11/Bloodlust.png")
                    elif x['faction']==0:
                        info.add_field(name="Faction:",value=f"```Vanguard```",inline=True)
                        info.set_image(url="https://static.miraheze.org/hordesiowiki/f/fd/Vanguard.png")
                        
                    
                    info.add_field(name="Level:",value=f"```{x['level']}```",inline=True)
                    info.add_field(name="Gearscore:",value=f"```{x['gs']}```",inline=True)
                    info.add_field(name="Prestige:",value=f"```{x['prestige']}```",inline=True)
                    info.add_field(name="Fame:",value=f"```{x['fame']}```",inline=True)
                    info.add_field(name="Clan:",value=f"```{x['clan']}```",inline=True)
                    info.add_field(name="Arena rating:",value=f"```{x['elo']}```",inline=True)
                 
                    info.add_field(name='Next immediate prestige goal:',value=f"```{f[pos]}```",inline=True)
                    info.add_field(name='Must reach below BRACKET to reach immediate next level:',value=f"```{i}```",inline=True)
             
                    info.add_field(name='Next bracket prestige gain:',value=f"```{a[i]}```",inline=True)
                    url1 = "https://hordes.io/api/pvp/getfactionpercentiles"
                    response1 = requests.get(url1)
                    json_data1 = json.loads(response1.text)
                    vg=json_data1[0]
                    bl=json_data1[1]
                    fame=x['fame']
                    if x['faction']==0:
                        c_b=0
                        it=0
                        for f in vg:
                            it+=1
                            if fame<=f:
                                if it!=13:
                                    c_b=it-1
                                    info.add_field(name="Current Bracket:",value=f"```{it-1}```",inline=True)
                                    info.add_field(name='Must reach below FAME to reach immediate next level:',value=f"```{vg[i]}```",inline=True)
                                    break
                        if it==13 and fame>vg[11] and fame<vg[12]:
                            c_b=12
                            info.add_field(name="Current Bracket:",value=f"```{12}```",inline=True)
                            info.add_field(name='Must reach below FAME to reach immediate next level:',value=f"```{vg[12]}```",inline=True)
                        elif it==13 and vg[12]==fame:
                            c_b=13
                            info.add_field(name="Current Bracket:",value=f"```{13}```",inline=True)
                            info.add_field(name='Must reach below FAME to reach immediate next level:',value=f"```{vg[12]}```",inline=True)
                        elif it==13:
                            c_b=13
                            info.add_field(name="Current Bracket:",value=f"```{13}```",inline=True)
                            info.add_field(name='Must reach below FAME to reach immediate next level',value=f"```{vg[12]}```",inline=True)
                    if x['faction']==1:
                        c_b=0
                        it=0
                        for f in bl:
                            it+=1
                            if fame<=f:
                                if it!=13:
                                    c_b=it-1
                                    info.add_field(name="Current Bracket:",value=f"```{it-1}```",inline=True)
                                    info.add_field(name='Must reach below FAME to reach immediate next level:',value=f"```{bl[i]}```",inline=True)
                                    break
                        if it==13 and fame>bl[11] and fame<bl[12]:
                            c_b=12
                            info.add_field(name="Current Bracket:",value=f"```{12}```",inline=True)
                            info.add_field(name='Must reach below FAME to reach immediate next level:',value=f"```{bl[12]}```",inline=True)
                        elif it==13 and bl[12]==fame:
                            c_b=13
                            info.add_field(name="Current Bracket:",value=f"```{13}```",inline=True)
                            info.add_field(name='Must reach below FAME to reach immediate next level',value=f"```{bl[12]}```",inline=True)
                        elif it==13:
                            c_b=13
                            info.add_field(name="Current Bracket:",value=f"```{13}```",inline=True)
                            info.add_field(name='Must reach below FAME to reach immediate next level:',value=f"```{bl[12]}```",inline=True)
                        
                    if c_b>i:
                        info.add_field(name='You have to climb below brackets:',value=f"```{0}```",inline=True)   
                    else:
                        info.add_field(name='You have to climb below brackets:',value=f"```{abs(i-c_b)}```",inline=True)    
                        
                    
                    info.add_field(name='If u dont pvp for a week ur prestige will be:',value=f"```{x['prestige']-(x['prestige']/5)}```",inline=True)  
                    
                    await ctx.send(embed=icon)
                    await ctx.send(embed=info)
                    break
                
                elif c==len(json_data) and fl==0:
                    await ctx.send("```Player exists with some other info 🟨```")
                    await ctx.send("```Try adding or removing characters ¯\_(ツ)_/¯```")         

 
  


@client.command()
async def clan(ctx,nam:str):
    
    url = "https://hordes.io/api/claninfo/info"
    response = requests.post(url, json={"tag": nam})
    json_data = json.loads(response.text)
    c=0
    
    try:
        clan=discord.Embed(title="```Clan details```",color=0x39FF14)
        
        clan.set_image(url="https://static.miraheze.org/hordesiowiki/0/0d/Clan.png")
        clan.add_field(name='`Online players :`', value=json_data['name'],inline=False)
        
        for x in json_data['members']:
            s=""
            os=""
            if x['online'] == True:
                c += 1
                if x['class']==1:
                    s='Mage'
                elif x['class']==3:
                    s='Shaman'
                elif x['class']==0:
                    s="Warrior"
                else:
                    s="Archer"
                clan.add_field(name=x['name'],value=s,inline=True)
        clan.add_field(name='`Online :`', value=c,inline=True)
        clan.add_field(name='```Owners```', value="",inline=False)
        p=0
        for x in json_data['members']:
           
            if x['clanrole'] == 3:
                p+=1
                if x['class']==1:
                    os='Mage'
                elif x['class']==3:
                    os='Shaman'
                elif x['class']==0:
                    os="Warrior"
                else:
                    os="Archer"
                
                clan.add_field(name=x['name'], value=os,inline=True)
        clan.add_field(name='`No of owners: `', value=p,inline=True)
        await ctx.send(embed=clan)
    except:
        await ctx.send("```Case sensitive Warning!```")
    
    

    



token = os.environ.get("TOKEN")

client.run(TOKEN)
