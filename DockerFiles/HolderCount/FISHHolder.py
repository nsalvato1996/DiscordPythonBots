import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_holdercount():
    r = requests.get('https://polygonscan.com/token/0x3a3Df212b7AA91Aa0402B9035b098891d276572B')
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find_all('div', {'class' : 'mr-3'})
    soup = soup[0].text
    soup = soup.split('\n')
    soup = soup[1]
    soup = soup.split(' ')
    soup = soup[0]
    data = soup

    del r, soup
    return data


def main():
    import discord
    import asyncio

    client = discord.Client()

    async def send_update(HolderCount):
        status = f'FISH Holders'
        nickname = f'{HolderCount}'
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
        await asyncio.sleep(120)

    @client.event
    async def on_ready():
        print("test")
        while True:
            price = get_holdercount()
            await send_update(price)
            del price
    client.run('INSERT TOKEN HERE')


if __name__ == '__main__':
    main()