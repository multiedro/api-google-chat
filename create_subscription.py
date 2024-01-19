# DOC Referência
# https://developers.google.com/workspace/events/guides/create-subscription?hl=pt-br


######################## Envie o formulário  para se inscrever no Programa de prévia para desenvolvedores do Google Workspace
######################## Este recurso ainda esta em versão Beta V1 e sera liberado mediante a inscrição no formulario abaixo
# https://developers.google.com/workspace/preview?hl=pt-br#apply



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

# Chat Grupo .
TARGET_RESOURCE = '//chat.googleapis.com/spaces/<ID DO GRUPO AQUI>'


# The types of events to receive.
EVENT_TYPES = [
    'google.workspace.chat.message.v1.created',
    'google.workspace.chat.message.v1.updated',
    'google.workspace.chat.reaction.v1.created',
    'google.workspace.chat.reaction.v1.deleted',
    'google.workspace.chat.reaction.v1.batchChanged',
    'google.workspace.chat.membership.v1.created',
    'google.workspace.chat.membership.v1.updated',
    'google.workspace.chat.membership.v1.deleted',
    'google.workspace.chat.membership.v1.batchChanged',
    'google.workspace.chat.space.v1.updated',
    'google.workspace.chat.space.v1.deleted'
]

# Path do topico do PubSub
TOPIC = '< SEU TOPICO PUBSUB AQUI >'


# Call the Workspace Events API using the service endpoint:
DISCOVERY_SERVICE_URL = 'https://workspaceevents.googleapis.com/$discovery/rest?version=v1beta&labels=DEVELOPER_PREVIEW&key=< SUA CHAVE DE API AQUI >'


service = build(
    'workspaceevents',
    'v1beta',
    credentials=CREDENTIALS,
    discoveryServiceUrl=DISCOVERY_SERVICE_URL,
)

BODY = {
    'target_resource': TARGET_RESOURCE,
    'event_types': EVENT_TYPES,
    'notification_endpoint': {'pubsub_topic': TOPIC},
    'payload_options': {'include_resource': True},
}

response = service.subscriptions().create(body=BODY).execute()
print(response)