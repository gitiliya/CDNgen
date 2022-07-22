import random, httpx, threading, time, pystyle
from pystyle import Center
from discord_webhook import DiscordWebhook

print(Center.XCenter(fr'''
            __
  _________/ /___  ____ ____  ____
 / ___/ __  / __ \/ __ `/ _ \/ __ \
/ /__/ /_/ / / / / /_/ /  __/ / / /
\___/\__,_/_/ /_/\__, /\___/_/ /_/
                /____/
             iliya#1111
'''))

y = int(input(Center.XCenter("\n Threads > ")))

hook = input(Center.XCenter("Webhook > "))

def genlink():
    while True:
        try:
            random.seed(time.time())
            num1 = random.randint(999111111111111111, 999999999999999999)
            num2 = random.randrange(999111111111111111, 999999999999999999)

            link = (f'https://cdn.discordapp.com/attachments/{num1}/{num2}/unknown.png')

            r = httpx.get(link)

            if r.status_code == 200:

                print('FOUND!')

                webhook = DiscordWebhook(url=hook, content=link)
                response = webhook.execute()

                time.sleep(5)

            else:

                print(link)

        except:
            pass

def main():
    for i in range(y):
        t = threading.Thread(target=genlink)
        t.start()
        time.sleep(.1)

if __name__ == "__main__":
    main()
