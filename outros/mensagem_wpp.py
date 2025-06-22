import requests

def enviar_mensagem_whatsapp(numero_telefone, mensagem, chave_api):
    # URL base da API
    url = "https://api.callmebot.com/whatsapp.php"
    
    # Parâmetros da requisição
    parametros = {
        'phone': numero_telefone,
        'text': mensagem,
        'apikey': chave_api
    }
    
    try:
        # Fazendo a requisição GET
        resposta = requests.get(url, params=parametros)
        
        # Verificando se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar mensagem. Status code: {resposta.status_code}")
            print("Resposta:", resposta.text)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    # Substitua pelos seus dados
    numero = "558591876412"  # Número de telefone no formato internacional
    mensagem = "Esta é uma mensagem de teste enviada via pelo robô do Joel!"
    api_key = "8799652"  # Substitua pela sua chave API real
    
    enviar_mensagem_whatsapp(numero, mensagem, api_key)