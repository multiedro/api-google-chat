# DOC Referência
# https://developers.google.com/chat/api/guides/v1/messages/list?hl=pt-br
# https://developers.google.com/chat/api/guides/auth?hl=pt-br


# Bibliotecas 
# pip3 install --upgrade google-api-python-client google-auth-oauthlib


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


# Este codigo utiliza o Tipo de Autenticação do Usuario consulte a documentação abaixo para maiores detalhes
# https://developers.google.com/chat/api/guides/auth?hl=pt-br 
# Define your app's authorization scopes.
# When modifying these scopes, delete the file token.json, if it exists.
SCOPES = ["https://www.googleapis.com/auth/chat.messages.readonly"]

def main():
    '''
    Authenticates with Chat API via user credentials,
    then lists messages in a space sent after March 16, 2023.
    '''

    flow = InstalledAppFlow.from_client_secrets_file('< CREDENCIAL DE USUARIO AQUI >', SCOPES)

    creds = flow.run_local_server()

    # Build a service endpoint for Chat API.
    chat = build('chat', 'v1', credentials=creds)

    # Use the service endpoint to call Chat API.
    result = chat.spaces().messages().list(

          # The space for which to list messages.
          parent = 'spaces/<ID DO GRUPO AQUI>',

          # An optional filter that returns messages
          # created after March 16, 2023.
          filter = 'createTime > "2023-03-16T00:00:00-00:00"'

      ).execute()

    # Prints details about the created membership.
    print(result)

if __name__ == '__main__':
    main()