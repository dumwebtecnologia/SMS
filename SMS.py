from twilio.rest import Client

# Substitua essas variáveis pelas suas credenciais do Twilio
account_sid = 'sua_account_sid'
auth_token = 'seu_auth_token'
remetente = 'seu_numero_twilio'  # Este deve ser um número Twilio

def enviar_sms(destinatario, mensagem):
    client = Client(account_sid, auth_token)

    mensagem = client.messages.create(
        body=mensagem,
        from_=remetente,
        to=destinatario
    )

    print(f'Mensagem enviada com SID: {mensagem.sid}')

# Exemplo de uso
destinatario = '+1234567890'  # Substitua pelo número de telefone de destino
mensagem = 'Olá! Esta é uma mensagem de teste.'

enviar_sms(destinatario, mensagem)

