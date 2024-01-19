# DOC Referência
# https://developers.google.com/chat/api/guides/v1/messages/create?hl=pt-br#python
# https://developers.google.com/chat/api/guides/v1/messages/private?hl=pt-br

# Bibliotecas 
# pip3 install --upgrade google-api-python-client google-auth


from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build


# Specify required scopes.
SCOPES = ['https://www.googleapis.com/auth/chat.bot']

# Specify service account details.
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    '< SUA SERVICE ACCOUNT AQUI>', SCOPES)

# Build the URI and authenticate with the service account.
chat = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))

# Create a Chat message.
result = chat.spaces().messages().create(

    #Informe aqui o ID do space que sera eviado a mensagem
    parent='spaces/<ID DO GRUPO AQUI>',


    # Envio de Mensagens com texto Simples
    # <users/all> Use este para mensionar todos os usuarios
    # <users/<INFORME O ID DO USUARIO AQUI>> Use este para mensionar somente um unico usuário

    # The message body.
    body={
        #  Mensagem que sera enviada
        'text': 'Este e um teste de envio de mensagem Privada',
        "privateMessageViewer": {
        # Informe abaixo o name do usuario este campo devera ficar semelhante a este aqui "name": "users/117520000043386399"
        "name": "< NAME DO USUARIO AQUI >"
        },

    }

).execute()

print(result)