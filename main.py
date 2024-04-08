from curses.ascii import isdigit
from webdriver import WebDriver
from pyrogram import Client, filters
from download_files import download
from concurrent.futures import ThreadPoolExecutor

BOT_TOKEN = "6393853527:AAGJp2_Yj_9sel4NC_rf0TzHuKxxVHjCPJs"
app = Client(name='TelegramBot', api_hash="ff9d2b13d574fd0206a14bd3ceac7502", api_id=23053083, bot_token=BOT_TOKEN)

page_size = 1

@app.on_message(filters.command("start"))
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")

# @app.on_message(filters.text)
# def ver_id(client, message):
#     message.reply(message.chat.id)    


@app.on_message(filters.regex('/page '))
def download_mods(client, message):
    page_size = 50

    page_number = message.text.split(" ")[-1]
    num1 = 1
    num2 = 2

    try:
        num1, num2 = page_number.split('-')
        num1 = int(num1)
        num2 = int(num2)
    except:
        return 1

    webdriver = WebDriver()
    
    for page in range(num1, num2+1):
        url_all = f"https://www.curseforge.com/minecraft/search?page={page}&pageSize={page_size}&sortBy=relevancy&class=mc-mods&gameVersionTypeId=1"
        data = webdriver.search_mod(url_all)
        print(f"\n\33[1;31m[*] PAGINA {page}\33[0m")
        with ThreadPoolExecutor() as executor:
            futures = []
            for mod in data.items():
                futures.append( executor.submit( download, mod, client, message ) )

    webdriver.driver.quit()

if __name__ == '__main__':
    print("BOT INICIADO")
    app.run()