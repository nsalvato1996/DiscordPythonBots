import requests
from datetime import datetime

def get_price(ids):
    r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=' + ids + "&vs_currencies=usd&include_24hr_change=true")
    print(r)
    return r.json()


def main(ticker: str):
    import discord
    import asyncio
    import yaml

    filename = 'config.yaml'
    with open(filename) as f:
        config = yaml.load(f, Loader=yaml.Loader)[ticker]
        del filename

    client = discord.Client()

    

    async def send_update(price, change24Hour, abbreviation):
        status = f'{change24Hour}'
        nickname = f'{abbreviation} ${price}'
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        print(f"Updated name {nickname}")
        print(f"Update status {status}")

        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        guilds = await client.fetch_guilds(limit=150).flatten()
        print("--------Guilds start here--------")

        for guild in guilds:
            await client.get_guild(guild.id).me.edit(nick=nickname)
            await asyncio.sleep(0.5)
            print("Updated: " + str(guild.id))
        print("---------Guilds end here---------")
        print("\n")
        del guilds, status, nickname
        

    @client.event
    async def on_ready():
        print("test")
        while True:
            getData = get_price(ticker)
            price = str(getData[ticker]['usd'])
            print(price)
            price = scientificToFloat(price)
            print(price)
            change24Hour = str(getData[ticker]['usd_24h_change'])
            change24Hour = "24h: " + str(percentStrip(change24Hour)) + "%"

            await send_update(price, change24Hour, config['abbreviation'])
            del getData, price, change24Hour
            await asyncio.sleep(config['updateFreq'])
    print(str(config['discordBotKey']))
    client.run(str(config['discordBotKey']))





def percentStrip(stringToStrip):
    if "-" in stringToStrip:
        trimmedString = stringToStrip[:5]
    else:
        trimmedString = stringToStrip[:4]
    del stringToStrip
    return trimmedString

def scientificToFloat(numberToConvert):
    # if 'e-08' in numberToConvert or 'e-10' in numberToConvert or 'e-09' in numberToConvert:
    #     numberToConvert = float(numberToConvert)
    #     numberToConvert = ("{:.12f}".format(numberToConvert))
    # elif 'e-06' in numberToConvert:
    #     numberToConvert = float(numberToConvert)
    #     numberToConvert = ("{:.8f}".format(numberToConvert))
    # elif 'e-09' in numberToConvert:
    #     numberToConvert = float(numberToConvert)
    #     numberToConvert = ("{:.12f}".format(numberToConvert))
    
    numberToConvert = format(float(numberToConvert), ".12f").rstrip("0")
    
    return numberToConvert


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--ticker',
                        action='store')
                        
    args = parser.parse_args()

    main(ticker=args.ticker)