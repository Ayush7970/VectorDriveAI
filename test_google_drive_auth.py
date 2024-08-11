import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from llama_index.readers.google import GoogleDriveReader

def authenticate_google_drive():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    CLIENT_SECRET_FILE = '/Users/ayushbhardwaj/Downloads/research/client_secret.json'
    
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('drive', 'v3', credentials=creds)
    
    # Assuming 'web' application type for client config
    client_config = {
        "web": {
            "client_id": creds.client_id,
            "project_id": "your-project-id",  # Replace with your actual project ID
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": creds.client_secret,
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
        }
    }
    
    return service, client_config

def find_file_in_folder(service, folder_name="research_check", file_name="drivefile2.pdf"):
    try:
        folder_query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
        folder_results = service.files().list(q=folder_query, spaces='drive',
                                             fields='nextPageToken, files(id, name)').execute()
        folders = folder_results.get('files', [])
        
        if not folders:
            print('Folder not found.')
            return None
        folder_id = folders[0]['id']

        # Search for the specific file within the folder
        file_query = f"'{folder_id}' in parents and name='{file_name}'"
        file_results = service.files().list(q=file_query, spaces='drive',
                                            fields='nextPageToken, files(id, name)').execute()
        files = file_results.get('files', [])
        if not files:
            print('File not found.')
            return None
        return files[0]['id']  # Return the file ID of the found file
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def read_file_contents(service, client_config, file_id):
    try:
        # Read file content using GoogleDriveReader
        reader = GoogleDriveReader(file_ids=[file_id], service=service, client_config=client_config)
        documents = reader.load_data()
        for document in documents:
            print(f"Content in {document.doc_id}:")
            print(document.text)  # Print the complete content of the document
    except HttpError as error:
        print(f'An error occurred: {error}')

def main():
    service, client_config = authenticate_google_drive()
    file_id = find_file_in_folder(service, folder_name="research_check", file_name="drivefile2.txt")
    if file_id:
        read_file_contents(service, client_config, file_id)

if __name__ == '__main__':
    main()
