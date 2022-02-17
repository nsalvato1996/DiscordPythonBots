import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_holdercount():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    r = requests.get('https://etherscan.io/token/0x72e5390edb7727e3d4e3436451dadaff675dbcc0', headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.select('#ContentPlaceHolder1_tr_tokenHolders > div > div.col-md-8 > div > div')
    
    soup = soup[0].text
    soup = soup.split('\n')
    soup = soup[1]
    soup = soup.split(' ')
    soup = soup[0]
    data = soup
    print(data)
    del soup, r, headers
    return data


def main():
    import discord
    import asyncio

    client = discord.Client()

    async def send_update(HolderCount):
        status = f'Ethereum'
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
        

    @client.event
    async def on_ready():
        print("test")
        while True:
            price = get_holdercount()
            await send_update(price)
            del price
            await asyncio.sleep(120)
    client.run('INSERT TOKEN HERE')


if __name__ == '__main__':
    main()