# DOC Referência
# https://developers.google.com/chat/api/guides/v1/spaces/update?hl=pt-br
# https://developers.google.com/chat/api/reference/rest/v1/spaces?hl=pt-br#Space.HistoryState

# DOC Referência - Inclusão de membros 
# https://developers.google.com/chat/api/guides/v1/spaces/set-up?hl=pt-br

# Bibliotecas 
# pip3 install --upgrade google-api-python-client google-auth-oauthlib


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define your app's authorization scopes.
# When modifying these scopes, delete the file token.json, if it exists.
SCOPES = ["https://www.googleapis.com/auth/chat.spaces"]

def main():
    '''
    Authenticates with Chat API via user credentials,
    then updates the specified space description and guidelines.
    '''

    # Authenticate with Google Workspace
    # and get user authorization.
    flow = InstalledAppFlow.from_client_secrets_file(
                      '< CREDENCIAL DE USUARIO AQUI >', SCOPES)
    creds = flow.run_local_server()

    # Build a service endpoint for Chat API.
    chat = build('chat', 'v1', credentials=creds)

    # Use the service endpoint to call Chat API.
    result = chat.spaces().patch(

      # The space to update, and the updated space details.
      #
      # Replace {space} with a space name.
      # Obtain the space name from the spaces resource of Chat API,
      # or from a space's URL.
      name='spaces/<ID DO GRUPO AQUI>',
      updateMask='spaceDetails',
      body={

        'spaceHistoryState': 'HISTORY_OFF',
        'spaceDetails': {
          'description': 'This description was updated with Chat API!',
          'guidelines': 'These guidelines were updated with Chat API!'
        }

      }

    ).execute()

    # Prints details about the created membership.
    print(result)

if __name__ == '__main__':
    main()