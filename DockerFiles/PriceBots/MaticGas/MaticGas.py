import requests
from datetime import datetime
import discord
import asyncio

client = discord.Client()

def get_Matic_Gas():
    r = requests.get('https://gasstation-mainnet.matic.network/').json()

    safeLow = r["safeLow"]
    safeLow = str(safeLow)
    safeLow = safeLow.split(".", 1)

    standard = r["standard"]
    standard = str(standard)
    standard = standard.split(".", 1)

    fast = r["fast"]
    fast = str(fast)
    fast = fast.split(".", 1)

    response = [safeLow[0], standard[0], fast[0]]

    del safeLow, standard, fast, r

    return response

def main():
    

    async def send_update(maticGasPrices):
        nickname = f"⚡{maticGasPrices[2]} 🤔{maticGasPrices[1]} 🐌{maticGasPrices[0]}"
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
            maticGas = get_Matic_Gas()
            await send_update(maticGas)
            del maticGas
            await asyncio.sleep(120)
    client.run('INSERT TOKEN HERE')


if __name__ == '__main__':
    main()