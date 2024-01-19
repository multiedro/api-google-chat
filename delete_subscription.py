# DOC Referência
# https://developers.google.com/workspace/events/guides/delete-subscription?hl=pt-br


# Bibliotecas 
# pip3 install --upgrade google-api-python-client google-auth-oauthlib

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Specify required scopes.
SCOPES = [
                'https://www.googleapis.com/auth/meetings.space.created',
                'https://www.googleapis.com/auth/meetings.space.readonly',
                'https://www.googleapis.com/auth/drive.readonly',
                'https://www.googleapis.com/auth/cloud-platform',
                'https://www.googleapis.com/auth/service.management',
                'https://www.googleapis.com/auth/pubsub',
                'https://www.googleapis.com/auth/contacts.readonly',
                'https://www.googleapis.com/auth/contacts',
                'https://www.googleapis.com/auth/userinfo.profile',
                'https://www.googleapis.com/auth/chat.memberships',
                'https://www.googleapis.com/auth/chat.memberships.readonly',
                'https://www.googleapis.com/auth/chat.spaces',
                'https://www.googleapis.com/auth/chat.spaces.readonly',
                'https://www.googleapis.com/auth/chat.messages',
                'https://www.googleapis.com/auth/chat.messages.readonly',
                'https://www.googleapis.com/auth/chat.messages.reactions',
                'https://www.googleapis.com/auth/chat.messages.reactions.readonly'
            ]

# Authenticate with Google Workspace and get user authentication.
flow = InstalledAppFlow.from_client_secrets_file('< CREDENCIAL DE USUARIO AQUI >', SCOPES)
CREDENTIALS = flow.run_local_server()

# Call the Workspace Events API using the service endpoint.
DISCOVERY_SERVICE_URL = 'https://workspaceevents.googleapis.com/$discovery/rest?version=v1beta&labels=DEVELOPER_PREVIEW&key=< SUA CHAVE DE API AQUI >'
service = build(
    'workspaceevents',
    'v1beta',
    credentials=CREDENTIALS,
    discoveryServiceUrl=DISCOVERY_SERVICE_URL,
)
# Informe o subscriptions aqui ele devera ter a seguinte aparencia 'subscriptions/chat-spaces-czpBQUFBWEt3MkJTODoxMTc1Mjg0NDA1MjM2NDMzODYzOTk6MTAzODk3MzE3NTgxMTIyMjkzNzIz'
NAME = '< SUBSCRIPTIONS NAME AQUI >'
response = service.subscriptions().delete(name=NAME).execute()
print(response)