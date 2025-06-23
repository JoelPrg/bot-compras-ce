from playwright.async_api import async_playwright

async def realizar_login(usuario, senha):
    # inicializa o navegador
    playwright = await async_playwright().start()
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context(ignore_https_errors=True)
    page = await context.new_page()

    # preenche e executa o login
    await page.goto("https://s2gpr.sefaz.ce.gov.br/licita-web/padrao-web/paginas/seguranca/login.seam")
    await page.fill(r"#login\:username", usuario)
    await page.fill(r"#login\:password", senha)
    await page.click(r"#login\:login")

    # retorna tudo pra ser usado depois
    return browser, context, page, playwright





from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

def login():
    # carregando informações de login
    load_dotenv()
    username = os.getenv('LOGIN_USERNAME')
    password = os.getenv('LOGIN_PASSWORD')

    # abertura de mavegador e login
    with sync_playwright() as p:
        # abetura de browser ignorando o SSL
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        page.goto("https://s2gpr.sefaz.ce.gov.br/licita-web/padrao-web/paginas/seguranca/login.seam")

        # inserindo login e senha
        page.get_by_label("login:username").fill(username)
        page.get_by_label("login:password:").fill(password)
        page.get_by_role("login:login").click()