# DOC Referência
# https://developers.google.com/chat/api/guides/v1/spaces/create?hl=pt-br
# https://developers.google.com/chat/api/reference/rest/v1/spaces?hl=pt-br#Space.HistoryState

# DOC Referência - Inclusão de membros 
# https://developers.google.com/chat/api/guides/v1/spaces/set-up?hl=pt-br

# Bibliotecas 
# pip3 install --upgrade google-api-python-client google-auth-oauthlib


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define your app's authorization scopes.
# When modifying these scopes, delete the file token.json, if it exists.
SCOPES = ["https://www.googleapis.com/auth/chat.spaces.create"]

def main():
    '''
    Authenticates with Chat API via user credentials,
    then creates a Chat space.
    '''

    # Authenticate with Google Workspace
    # and get user authorization.
    flow = InstalledAppFlow.from_client_secrets_file(
                      '< CREDENCIAL DE USUARIO AQUI >', SCOPES)
    creds = flow.run_local_server()

    # Build a service endpoint for Chat API.
    chat = build('chat', 'v1', credentials=creds)

    # Use the service endpoint to call Chat API.
    result = chat.spaces().create(

      # Details about the space to create.
      body = {

        # Consulte a Documentação abaixo para planejar melhor a criação do seu Space 
        # Existem variaveis importantes que precisam de atenção durante o processo de criação
        # https://developers.google.com/chat/api/reference/rest/v1/spaces?hl=pt-br#Space.HistoryState
        "spaceThreadingState":"GROUPED_MESSAGES",
        "externalUserAllowed": 'false',
        "displayName": "Criação de Space via API - Magalu",
        "singleUserBotDm": 'false',
        "spaceType": "SPACE",
        "name": "Space criado via API - 3",
        "spaceDetails": {
            "description": "Descrição do Space Criado via API - 3",
            "guidelines": "guidelines Teste criação API"
        }
      }

      ).execute()

    # Prints details about the created membership.
    print(result)

if __name__ == '__main__':
    main()