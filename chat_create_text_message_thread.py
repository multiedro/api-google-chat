# DOC Referência
# https://developers.google.com/chat/api/guides/v1/messages/create?hl=pt-br#python
# https://developers.google.com/chat/api/guides/v1/messages/create?hl=pt-br#create-message-thread

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

    # Informe aqui o ID do space que sera eviado a mensagem
    parent='spaces/<ID DO GRUPO AQUI>',

    # DOC para este tema
    # https://developers.google.com/chat/api/reference/rest/v1/spaces.messages/create?hl=pt-br#messagereplyoption
    # Ativa para caso a Thread não exista ele vai criar uma nova.
    messageReplyOption='REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD',

    # Envio de Mensagens com texto Simples
    # <users/all> Use este para mensionar todos os usuarios
    # <users/<INFORME O ID DO USUARIO AQUI>> Use este para mensionar somente um unico usuário

    # The message body.
    body={

        # Mensagem que sera enviada
        'text': 'Boa Noite em que posso te ajudar.',

        # DOC para este tema
        # https://developers.google.com/chat/api/guides/v1/messages/create?hl=pt-br#create-message-thread
        'thread': {
            
            # Utilize o thread.name para responder a uma mensagem postada pelo usuario ou bot
            # Utilize o thread.threadkey para especificar um nome personalizado para a sua Threadkey
            # Para responder a uma conversa, envie uma mensagem que especifique o campo threadKey ou name da conversa. 
            # Se a conversa foi criada por uma pessoa ou por outro app do Chat, use o campo thread.name.
            # Exemplo de como deve ficar a linha abaixo "name":"spaces/AAzAXKw2BS8/threads/qFnSk9aaxBE"
            "name":"< NAME DA SUA THREAD AQUI >"
        }
    }

).execute()
print(result)