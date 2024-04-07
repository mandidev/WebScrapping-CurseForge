from curses.ascii import isdigit
from webdriver import WebDriver
from pyrogram import Client, filters
from download_files import download

BOT_TOKEN = "6393853527:AAGJp2_Yj_9sel4NC_rf0TzHuKxxVHjCPJs"
app = Client(name='TelegramBot', api_hash="ff9d2b13d574fd0206a14bd3ceac7502", api_id=23053083, bot_token=BOT_TOKEN)

page_size = 1

@app.on_message(filters.command("start"))
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


@app.on_message(filters.regex('/page '))
async def download_mods(client, message):
    if isdigit( message.text.split(" ")[-1] ):
        page_number = message.text.split(" ")[-1]
    else:
        await message.reply("**Comando Incorrecto**")
        return 1
    
    webdriver = WebDriver()
    data = webdriver.search_mod(f"https://www.curseforge.com/minecraft/search?page={page_number}&pageSize={page_size}&sortBy=popularity&class=mc-mods&version=1.20.1")
    download(data)
    webdriver.driver.quit()

if __name__ == '__main__':
    print("BOT INICIADO")
    app.run()