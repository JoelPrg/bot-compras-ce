import asyncio
import os
from bot.login import realizar_login
from dotenv import load_dotenv
load_dotenv()

async def main():
    usuario = os.getenv("LOGIN_USERNAME")
    senha = os.getenv("LOGIN_PASSWORD")

    browser, context, page, playwright = await realizar_login(usuario, senha)

    # Aqui você continua o fluxo com a página logada
    await page.wait_for_timeout(30000)

    await browser.close()
    await playwright.stop()

asyncio.run(main())
