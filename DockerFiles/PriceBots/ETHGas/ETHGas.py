import requests
from datetime import datetime
import discord
import asyncio

client = discord.Client()

def getETHGas():
    r = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=6a061999716ebfa281f273c35d85b6dbc11a924c7e5abedc2fa256af35eb').json()
    print(r)

    safeLow = r["safeLow"]
    safeLow = safeLow / 10
    safeLow = str(safeLow)

    standard = r["average"]
    standard = standard / 10
    standard = str(standard)

    fast = r["fastest"]
    fast = fast / 10
    fast = str(fast)
    response = [safeLow, standard, fast]

    del safeLow, standard, fast, r

    return response

def main():
    

    async def send_update(ETHGasPrices):
        nickname = f"⚡{ETHGasPrices[2]} 🤔{ETHGasPrices[1]} 🐌{ETHGasPrices[0]}"
        status = "Fast, Avg, Slow"
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        del status
        print(f"Updated name {nickname}")

        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        guilds = await client.fetch_guilds(limit=150).flatten()
        print("--------Guilds start here--------")

        for guild in guilds:
            await client.get_guild(guild.id).me.edit(nick=nickname)
            await asyncio.sleep(0.5)
            print("Updated: " + str(guild.id))
        print("---------Guilds end here---------")
        print("\n")
        del nickname, guilds

    @client.event
    async def on_ready():
        while True:
            ETHGas = getETHGas()
            await send_update(ETHGas)
            del ETHGas
            await asyncio.sleep(120)
    client.run('INSERT TOKEN HERE')


if __name__ == '__main__':
    main()