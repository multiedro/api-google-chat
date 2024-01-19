# DOC Referência
# https://developers.google.com/chat/api/guides/v1/members/list?hl=pt-br#list-memberships-app-auth

# Bibliotecas 
# pip3 install --upgrade google-api-python-client google-auth-oauthlib google-auth

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
# Define your app's authorization scopes.
# When modifying these scopes, delete the file token.json, if it exists.

SCOPES = ["https://www.googleapis.com/auth/chat.memberships.readonly"]

def main():
    '''
    Authenticates with Chat API via user credentials,
    then lists human space members (but not space managers) in a
    specified space.
    '''

    # Specify required scopes.
    SCOPES = ['https://www.googleapis.com/auth/chat.bot']

    # Specify service account details.
    CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
        '< SUA SERVICE ACCOUNT AQUI>', SCOPES)

    # Build a service endpoint for Chat API.
    chat = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))

    # Use the service endpoint to call Chat API.
    result = chat.spaces().members().list(

        # The space for which to list memberships.
        parent = 'spaces/<ID DO GRUPO AQUI>',

        # An optional filter that returns only human space members.
        filter = 'member.type = "HUMAN" AND role = "ROLE_MEMBER"'

    ).execute()

    # Prints details about the created membership.
    print(result)

if __name__ == '__main__':
    main()