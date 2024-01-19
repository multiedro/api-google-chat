# DOC Referência
# https://developers.google.com/chat/api/guides/v1/messages/create?hl=pt-br#python

# Construtor de Cards
# https://addons.gsuite.google.com/uikit/builder?hl=pt-br

# Cards Google Chat
# https://developers.google.com/chat/api/reference/rest/v1/cards?hl=pt-br

# Formatação dos cards
# https://developers.google.com/chat/api/reference/rest/v1/cards?hl=pt-br#TextInput

# Cards Interativas 
# https://developers.google.com/chat/design/interactivity?hl=pt-br
# https://developers.google.com/chat/how-tos/dialogs?hl=pt-br

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


    body = {
        "cardsV2": [{"cardId": "unique-card-id",
              "card":{
                      "header": {
                        "title": "Sistema de Notificações",
                        "subtitle": "New Ticket",
                        "imageUrl": "https://github.com/multiedro/imagens/blob/main/SireneLogo-removebg-preview.png?raw=true",
                        "imageType": "CIRCLE"
                      },
                      "sections": [
                        {
                          "header": "Dados do Ticket",
                          "collapsible": "false",
                          "uncollapsibleWidgetsCount": 1,
                          "widgets": [
                            {
                              "decoratedText": {
                                "icon": {
                                  "knownIcon": "TICKET"
                                },
                                "topLabel": "Ticket",
                                "text": "123456789"
                              }
                            },
                            {
                              "divider": {}
                            },
                            {
                              "decoratedText": {
                                "icon": {
                                  "knownIcon": "DESCRIPTION"
                                },
                                "topLabel": "Descrição do Ticket"
                                
                              }
                            },
                            {
                              "textParagraph": {
                                "text": "Coloque o seu texto aqui, tente ser breve e pode usar a documentação de formatação do texto para formatar a mensagem e colocar um link nela conforme este exemplo aqui <a href=https://developers.google.com/chat/format-messages>Link da Documentação</a> "
                              }
                            }
                          ]
                        }
                      ]
                    }
              
              
              }]              
              }

).execute()

print(result)