from bs4 import BeautifulSoup
import discord
import asyncio
from datetime import datetime
from requests_html import AsyncHTMLSession


def main():
   client = discord.Client()
   async def send_update(price1):
      status = f'Total Value Deposited'
      nickname = f'{price1}'
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
      # for task in asyncio.all_tasks():
      #    task.cancel()
      

   @client.event
   async def on_ready():
      while True:
         PawPrice = ''
         while PawPrice == '':
            try:
                  
               session = AsyncHTMLSession()
               url = 'https://app.congruent.fi/#/stake'
               r = await session.get(url)
               await r.html.arender(sleep=35, keep_page=True, timeout=60)
               soup = BeautifulSoup(r.html.raw_html, 'html.parser')
               PawPrice = soup.find_all('h4', {'class' : 'MuiTypography-root MuiTypography-h4'})
               PawPrice = PawPrice[1].text
               print(PawPrice)
               await session.close()
               del session, url, r, soup

               
            
               


            except Exception as inst:
               print(inst)

            finally:
               if PawPrice != '':
                  await send_update(PawPrice)
                  # del PawPrice, PawPrice1
               
               await asyncio.sleep(120)
         del PawPrice
   client.run('INSERT TOKEN HERE')

          


if __name__ == '__main__':

    main()