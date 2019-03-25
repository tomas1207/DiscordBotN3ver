import discord
from discord.ext import commands
import asyncio
import json
import requests


token = ''

bot = commands.Bot(command_prefix='!')



#url = "http://www.tomasfernandes.pt/Beta/Streams.php"
async def streams(ctx):
    arraystreams = [["Tomas1207", True], ["x01xico",True], ["xtr34mPT",True], ["06murat19",True], ["adaocomtil_a",True], ["Ninja",True]]
    while True:
        for i in arraystreams:
            url = 'https://api.twitch.tv/kraken/streams/' + i[0] + '?client_id=8e6fsz2mnoy60vh1frz7ac12bg2rr4'
            response = requests.get(url).text
            
            json1 = json.loads(response)
            print(json1["stream"])
            if (json1["stream"] != None):
                print(i)
                if (i[1]):
                    game = json1["stream"]["game"]
                    i[1] = False
                    print(i)
                    await ctx.send("@everyone o streamer %s \n Esta a jogar %s" % (i[0], game))
            else:
                i[1] = True
        await asyncio.sleep(6)
@bot.command()
async def setmain(ctx):
    await ctx.send("Ctx: " + str(ctx))
    bot.loop.create_task(streams(ctx))
@bot.command()
async def ping(ctx):
    await ctx.send(':cookies:')

@bot.command()
async def logout(ctx):
    await bot.logout()
bot.run(token)
