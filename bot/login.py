import requests
from bs4 import BeautifulSoup

def efetuar_login(USUARIO, SENHA):
    # inicia uma sessão para conseguir manter o fluxo de tarefas
    session = requests.Session()

    # obter o viewstate
    url_login = "http://s2gpr.sefaz.ce.gov.br/cotacao-web/padrao-web/paginas/seguranca/login.seam"
    res = session.get(url_login)
    soup = BeautifulSoup(res.text, "html.parser")
    view_state = soup.find("input", {"name": "javax.faces.ViewState"})["value"]

    # dados do formulário (payload)
    data = {
        "AJAXREQUEST": "_viewRoot",
        "login:username": USUARIO,
        "login:password": SENHA,
        "login:rememberMe": "on",
        "login:login": "login",
        "autoScroll": "",
        "javax.faces.ViewState": view_state
    }

    # dados pra simular mozilla firefox
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0",
        "Referer": url_login
    }

    # efetua de fato o login
    res_post = session.post(url_login, data=data, headers=headers)

    # Testa se o login foi feito
    if "sair" in res_post.text.lower() or "logout" in res_post.text.lower():
        print("Login bem-sucedido!")
    else:
        print("Algo deu errado no login.")
        with open("resposta.html", "w", encoding="utf-8") as f:
            f.write(res_post.text)
